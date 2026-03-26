# LeetCode Solutions

Welcome to my personal repository of LeetCode solutions!

## Overview
This repository contains my programming solutions to various LeetCode problems, categorized by date and month (e.g., `daily/jan`, `daily/feb`, `daily/mar`). It serves to track my problem-solving progress and maintain a history of algorithmic approaches over time.

## Repository Structure
- `daily/`: Solutions organized by month
  - `jan/`: January solutions
  - `feb/`: February solutions
  - `mar/`: March solutions
- `auto-push.ps1`: PowerShell script for automated Git operations
- `README.md`: This file
- `.gitignore`: Git ignore rules

## Automation
I use scripts to automatically watch the directory for any file changes, add them, commit them with a timestamp, and push them to my remote GitHub repository. This removes the manual step of committing every solution.

### PowerShell Script (`auto-push.ps1`)
For Windows environments.

### Bash Script (`auto-push.sh`)
For WSL/Linux environments. Requires `inotify-tools` to be installed.

To run:
```bash
./auto-push.sh &
```

### How it works
1. **File Watcher**: Listens for any file creation, changes, renames, or deletions in the directory (excluding .git).
2. **Debounce / Timeout**: Waits briefly (1.5 seconds) to batch multiple operations together.
3. **Commit & Push**: Commits everything with the message "LeetCode auto update YYYY-MM-DD HH:mm:ss" and pushes it to `origin main`.

## Languages Used
- Python (.py)
- C++ (.cpp)
- Java (.java)

## Contributing
This is a personal repository for tracking my LeetCode progress. Feel free to explore the solutions, but please note that they are for learning purposes.
