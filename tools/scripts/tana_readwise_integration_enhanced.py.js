#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { program } = require('commander');

program
  .option('-i, --input <path>', 'Input file path')
  .option('-o, --output <path>', 'Output file path')
  .option('-v, --verbose', 'Verbose output for debugging')
  .parse(process.argv);

const options = program.opts();

if (!options.input || !options.output) {
  console.error('Error: Input and output file paths are required');
  program.help();
  process.exit(1);
}

// Define content type tags and their corresponding Readwise types
const contentTypeMap = {
  // Legacy system
  '#permanent_note': 'note',
  '#claim': 'note',
  '#question': 'question',
  '#evidence': 'note',
  '#quote': 'quote',
  
  // New SN(A)CK system
  '#highlight': 'highlight',
  '#summary': 'note',
  '#note': 'note',
  '#analysis': 'note',
  '#connection': 'note',
  '#key': 'note'
};

// Define priority order for content types (for when multiple types are present)
const contentTypePriority = [
  // New SN(A)CK system (higher priority)
  '#highlight',
  '#summary',
  '#note',
  '#analysis',
  '#connection',
  '#key',
  
  // Legacy system
  '#quote',
  '#evidence',
  '#claim',
  '#question',
  '#permanent_note'
];

// Function to log verbose messages
function verboseLog(message) {
  if (options.verbose) {
    console.log(`[INFO] ${message}`);
  }
}

// Function to extract tags from content
function extractTags(content) {
  // Pattern for both legacy tags and new SN(A)CK format tags
  const tagPattern = /#[a-zA-Z0-9_/-]+(?:\s+SN\(A\)CK)?/g;
  return content.match(tagPattern) || [];
}

// Function to determine the content type based on tags
function determineContentType(tags) {
  // Process tags to handle SN(A)CK format
  const processedTags = tags.map(tag => {
    if (tag.includes('SN(A)CK')) {
      return tag.split(' ')[0]; // Get the tag part before SN(A)CK
    }
    return tag;
  });
  
  // Find all matching content type tags
  const contentTypes = processedTags.filter(tag => Object.keys(contentTypeMap).includes(tag));
  
  // If multiple content types are found, use priority order
  if (contentTypes.length > 1) {
    for (const type of contentTypePriority) {
      if (contentTypes.includes(type)) {
        return contentTypeMap[type];
      }
    }
  }
  
  // If one content type is found, use it
  if (contentTypes.length === 1) {
    return contentTypeMap[contentTypes[0]];
  }
  
  // Default to note if no content type tag is found
  return 'note';
}

// Function to clean content by removing tags
function cleanContent(content) {
  // Replace legacy tags
  let cleaned = content.replace(/#[a-zA-Z0-9_/-]+/g, '');
  
  // Replace SN(A)CK format tags
  cleaned = cleaned.replace(/#[a-zA-Z0-9_/-]+\s+SN\(A\)CK/g, '');
  
  return cleaned.trim();
}

// Function to get topic tags (non-content-type tags)
function getTopicTags(tags) {
  return tags
    .filter(tag => {
      // For legacy tags
      if (Object.keys(contentTypeMap).includes(tag)) {
        return false;
      }
      
      // For SN(A)CK format
      if (tag.includes('SN(A)CK')) {
        const baseTag = tag.split(' ')[0];
        return !Object.keys(contentTypeMap).includes(baseTag);
      }
      
      return true;
    })
    .map(tag => {
      // Handle SN(A)CK format by removing SN(A)CK part
      if (tag.includes('SN(A)CK')) {
        return tag.split(' ')[0].substring(1);
      }
      return tag.substring(1); // Remove # prefix for regular tags
    });
}

// Function to parse a line or block into a Readwise-compatible object
function parseContentBlock(block) {
  const tags = extractTags(block);
  const contentType = determineContentType(tags);
  const highlightText = cleanContent(block);
  const topicTags = getTopicTags(tags);
  
  return {
    text: highlightText,
    tags: topicTags,
    note: '',
    location: 0,
    location_type: '',
    highlighted_at: new Date().toISOString(),
    highlight_type: contentType
  };
}

// Function to process multi-line blocks and handle block quotes
function processContentBlocks(content) {
  const lines = content.split('\n');
  const blocks = [];
  let currentBlock = [];
  let inBlockQuote = false;
  
  verboseLog(`Processing ${lines.length} lines of content`);
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmedLine = line.trim();
    
    // Skip empty lines
    if (trimmedLine === '') {
      // If we were building a block, finish it
      if (currentBlock.length > 0) {
        blocks.push(currentBlock.join('\n'));
        currentBlock = [];
        inBlockQuote = false;
      }
      continue;
    }
    
    // Handle block quotes
    const isBlockQuoteLine = trimmedLine.startsWith('>');
    
    // Check if this is the start of a new block or continuation
    if (currentBlock.length === 0 || 
        (isBlockQuoteLine && !inBlockQuote) || 
        (!isBlockQuoteLine && inBlockQuote)) {
      // If we were building a block, finish it
      if (currentBlock.length > 0) {
        blocks.push(currentBlock.join('\n'));
        currentBlock = [];
      }
      
      // Start a new block
      currentBlock.push(trimmedLine);
      inBlockQuote = isBlockQuoteLine;
    } else {
      // Continue current block
      currentBlock.push(trimmedLine);
    }
    
    // Check if this line has content tags
    const hasTags = extractTags(trimmedLine).some(tag => {
      // For legacy tags, direct comparison works
      if (Object.keys(contentTypeMap).includes(tag)) {
        return true;
      }
      
      // For SN(A)CK format, check if any content type is included
      if (tag.includes('SN(A)CK')) {
        const baseTag = tag.split(' ')[0]; // Get the tag part before SN(A)CK
        return Object.keys(contentTypeMap).includes(baseTag);
      }
      
      return false;
    });
    
    // If we find a line with content tags and it's not part of a block quote,
    // it might indicate the end of the current block
    if (hasTags && !isBlockQuoteLine && currentBlock.length > 1) {
      // If the previous line didn't have tags, split here
      const prevLineHasTags = i > 0 && 
                             extractTags(lines[i-1]).some(tag => 
                               Object.keys(contentTypeMap).includes(tag));
      
      if (!prevLineHasTags) {
        blocks.push(currentBlock.slice(0, -1).join('\n'));
        currentBlock = [trimmedLine];
      }
    }
  }
  
  // Don't forget the last block
  if (currentBlock.length > 0) {
    blocks.push(currentBlock.join('\n'));
  }
  
  verboseLog(`Identified ${blocks.length} content blocks`);
  return blocks;
}

// Function to process an entire file
function processFile(inputPath, outputPath) {
  try {
    // Read the input file
    const content = fs.readFileSync(inputPath, 'utf8');
    verboseLog(`Read ${content.length} characters from ${inputPath}`);
    
    // Process the content into blocks
    const contentBlocks = processContentBlocks(content);
    
    // Parse each block into a Readwise-compatible object
    const highlights = contentBlocks
      .filter(block => block.trim() !== '')
      .map(block => parseContentBlock(block));
    
    // Prepare the output object
    const output = {
      highlights
    };
    
    // Write the output file
    const outputDir = path.dirname(outputPath);
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }
    
    fs.writeFileSync(outputPath, JSON.stringify(output, null, 2));
    verboseLog(`Wrote ${highlights.length} highlights to ${outputPath}`);
    
    console.log(`✅ Successfully processed ${highlights.length} highlights`);
    console.log(`Output written to: ${outputPath}`);
    
  } catch (error) {
    console.error(`Error processing file: ${error.message}`);
    process.exit(1);
  }
}

// Additional function to handle nested hierarchical tags
function expandNestedTags(tags) {
  const expandedTags = [];
  
  tags.forEach(tag => {
    // Remove the # prefix
    const cleanTag = tag.substring(1);
    
    // Check if it's a hierarchical tag
    if (cleanTag.includes('/')) {
      // Add the full tag
      expandedTags.push(cleanTag);
      
      // Add each level of the hierarchy
      const parts = cleanTag.split('/');
      let current = '';
      
      for (let i = 0; i < parts.length; i++) {
        if (i === 0) {
          current = parts[i];
        } else {
          current += '/' + parts[i];
        }
        
        // Add each level if it's not already included
        if (current !== cleanTag && !expandedTags.includes(current)) {
          expandedTags.push(current);
        }
      }
    } else {
      // Non-hierarchical tag
      expandedTags.push(cleanTag);
    }
  });
  
  return expandedTags;
}

// Enhanced version of getTopicTags to handle nested tags
function getTopicTags(tags) {
  const topicTags = tags.filter(tag => !Object.keys(contentTypeMap).includes(tag));
  return expandNestedTags(topicTags);
}

// Process the file
processFile(options.input, options.output);
