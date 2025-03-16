# Using VS Code's Git Integration

Here's how to manage your GitHub repository using VS Code's built-in Git tools:

## Initial Setup
1. Open your project folder in VS Code
   - Go to File > Open Folder and navigate to your GitHub repository folder

2. Make sure Git is initialized
   - The Source Control icon in the left sidebar (looks like a branch) will show the number of changes
   - If not initialized, open VS Code's terminal (View > Terminal) and run `git init`

## Saving Changes to GitHub

1. **Make and save changes to your files**
   - Edit your files as needed (such as adding `chapter-to-source-index.rtf` to the `project-docs/` folder)
   - Save the files with Ctrl+S (Cmd+S on Mac)

2. **View your changes**
   - Click the Source Control icon in the sidebar (branch icon)
   - You'll see a list of changed files

3. **Stage your changes**
   - Hover over a file and click the + icon to stage it
   - Or stage all changes by clicking the + icon at the top of the Changes section

4. **Commit your changes**
   - Type a commit message in the text box at the top of the Source Control panel
   - Click the checkmark icon (✓) or press Ctrl+Enter (Cmd+Enter on Mac) to commit

5. **Push to GitHub**
   - Click the "..." menu in the Source Control panel
   - Select "Push"
   - Or click the cloud upload icon at the bottom of the VS Code window

## Additional Helpful Features

- **View differences**: Click on any changed file in the Source Control panel to see what changed
- **Create branches**: Click the branch name in the status bar (bottom left) to create or switch branches
- **Pull changes**: Use the "..." menu and select "Pull" to get updates from GitHub
- **View history**: Right-click on a file and select "View File History"

## Checking Status

- The status bar at the bottom of VS Code shows:
  - Current branch (bottom left)
  - Number of pending changes (to be pushed to GitHub)
  - Sync indicators (up/down arrows) showing if you need to push or pull

If you encounter any authentication issues, VS Code will typically prompt you to sign in to your GitHub account through a browser window.

Would you like more detailed information about any of these steps?