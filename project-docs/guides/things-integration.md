# Integrating Things 3 with Your Book Publishing Workflow

Things 3 is a powerful task management application for macOS that can enhance your book publishing workflow. This guide explains how to integrate Things with Claude, GitHub, Tana, VS Code, and Scrivener.

## Setting Up Things 3 for Your Book Project

### Project Structure

1. **Create a Book Project**
   - Open Things 3
   - Click "+" in the bottom-left corner → "New Project"
   - Name it "MAGA Christianism Book"
   - Optionally add a deadline date
   - Set to "Today" focus if currently your main project

2. **Create Areas**
   - Click "+" → "New Area"
   - Create the following areas:
     - "Book Writing" (for the main creative process)
     - "Publishing" (for tasks related to publishing platforms)
     - "Marketing" (for promotion tasks)

3. **Set Up Project Hierarchy**
   - Within the "MAGA Christianism Book" project, create the following projects:
     - "Part I: Foundations"
     - "Part II: Primitive Biblicism"
     - "Part III: Practical Atheism"
     - "Part IV: Binary Apocalypticism"
     - "Research Tasks"
     - "Editorial Tasks"
     - "Substack Publication"
     - "KDP Publication"

### Tag System

Create the following tags to align with your workflow:

1. Right-click on "Tags" in the sidebar → "New Tag"
2. Create these tags:
   - `#writing` - For drafting tasks
   - `#editing` - For revision tasks
   - `#research` - For source research
   - `#claude` - For AI assistance tasks
   - `#github` - For version control tasks
   - `#tana` - For organizational tasks
   - `#vscode` - For coding/formatting tasks
   - `#scrivener` - For compilation tasks
   - `#substack` - For Substack publishing
   - `#kdp` - For Amazon publishing
   - `#urgent` - For high-priority items
   - `#waiting` - For tasks awaiting external input

## Integration with Your Workflow

### Linking Things with VS Code

1. **Using Things URL Scheme**
   - Create a VS Code snippet that generates Things URLs
   - Add to `.vscode/markdown.code-snippets`:

```json
"Create Things Task": {
  "prefix": "things-task",
  "body": [
    "<!-- TASK: things:///add?title=${1:Task%20Title}&notes=${2:Task%20Notes}&tags=${3:writing} -->"
  ],
  "description": "Create a link to add a task to Things"
}
```

2. **VS Code Extension**
   - Install "Tasks" extension for VS Code
   - Configure to create tasks in Things 3 via AppleScript

### Linking Things with Tana

1. **Using URL Field**
   - Add a "thingsURL" field to your Tana #Task Super Tag
   - Generate Things URLs in the format: `things:///show?id=task-id`
   - Click the URL to open the specific task in Things

2. **Daily Export**
   - Create a Tana export template for Things tasks
   - Run this export daily to update your Things inbox

### GitHub Integration via Hooks

Create a post-commit hook that adds a reminder to Things:

1. Create a file `.git/hooks/post-commit`:

```bash
#!/bin/bash

COMMIT_MSG=$(git log -1 HEAD --pretty=format:%s)
osascript <<EOD
tell application "Things3"
    set newToDo to make new to do with properties {name:"Review: $COMMIT_MSG", notes:"Recent commit to review"}
    set tag names of newToDo to {"github", "writing"}
end tell
EOD
```

2. Make the hook executable:

```bash
chmod +x .git/hooks/post-commit
```

### Claude to Things Workflow

Create a script to extract actions from Claude conversations:

```applescript
-- Extract TODOs from Claude conversation
tell application "System Events"
    set clipboardContent to the clipboard
    set todosList to paragraphs of clipboardContent
    
    tell application "Things3"
        repeat with todoItem in todosList
            if todoItem contains "TODO:" then
                set todoText to text 6 thru -1 of todoItem
                make new to do with properties {name:todoText, notes:"From Claude conversation", tag names:{"claude"}}
            end if
        end repeat
    end tell
end tell
```

## Task Management Workflow

### Daily Writing Schedule

1. **Morning Review**
   - Review "Today" in Things
   - Process any items in Inbox
   - Tag highest priority items with `#urgent`

2. **Chapter Planning**
   - Create a task for each chapter section
   - Include deadlines aligned with publication schedule
   - Add checklist items for research, drafting, and editing

3. **Tracking Progress**
   - Use Things' progress pie chart to track chapter completion
   - Add headings to organize subtasks under each chapter

### Publishing Tasks

For Substack publishing:

1. Create recurring tasks for each publication date
2. Include checklists for:
   - Final editing
   - SEO optimization
   - Image preparation
   - Scheduling
   - Promotion

For Amazon KDP:

1. Create a project with sequential tasks:
   - Format verification
   - Cover design review
   - Metadata preparation
   - Upload and validation
   - Pricing and distribution settings
   - Launch promotion

## Automation with AppleScript

### VS Code to Things

Save this as `addChapterTask.scpt`:

```applescript
on run {chapterTitle, dueDate}
    tell application "Things3"
        set newToDo to make new to do with properties {name:"Write " & chapterTitle, due date:date dueDate}
        set project of newToDo to project "MAGA Christianism Book" of area "Book Writing"
        set tag names of newToDo to {"writing"}
    end tell
end run
```

### Scrivener to Things

Save this as `addEditingTasks.scpt`:

```applescript
on run {documentName}
    tell application "Things3"
        set newToDo to make new to do with properties {name:"Edit " & documentName}
        set tag names of newToDo to {"editing", "scrivener"}
        set notes of newToDo to "Final review before compilation"
    end tell
end run
```

## Advanced Things 3 Features for Book Projects

### Using Headings for Structure

Within each part project, use headings to organize:

1. Create a new heading by typing a title and pressing Alt+Shift+N
2. Create headings like:
   - "First Draft"
   - "Revisions"
   - "Final Edits"
   - "Ready for Publication"

### Using the Logbook for Progress Tracking

1. Complete tasks to move them to the Logbook
2. Review the Logbook weekly to track productivity
3. Use the "Today" view to focus on immediate priorities

### Keyboard Shortcuts for Efficiency

Master these shortcuts for quick task management:

- Space: Complete/incomplete a task
- Cmd+N: New to-do
- Cmd+Shift+N: New project
- Cmd+K: Add a tag
- Cmd+Shift+D: Set a deadline
- Cmd+S: Show in sidebar
- Cmd+.: Enter Times (quick entry from any app)

## Syncing Across Devices

If you use Things on multiple devices:

1. Ensure Things Cloud is enabled
2. Use Things on iOS to review tasks on the go
3. Add quick ideas via the Things Quick Entry feature
4. Review completed tasks on the Mac for your weekly progress report

## Practical Tips

1. **Use Scheduled Start Dates** rather than just deadlines to plan your writing pipeline

2. **Create Repeating Tasks** for regular activities like:
   - Weekly chapter submissions
   - Monthly progress reviews
   - Regular backups

3. **Use the "This Evening" Section** to separate deep writing work (Today) from lighter review tasks (Evening)

4. **Leverage the "Upcoming" View** to visualize your publication timeline

5. **Consider Things Mail Integration** to forward important publishing correspondence directly to your Things inbox

This integration creates a smooth workflow where your task management in Things seamlessly connects to your content creation and publishing tools, keeping all aspects of your book project organized and on track.
