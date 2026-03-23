# LeetCode Solutions

Welcome to my personal repository of LeetCode solutions! 

## Overview
This workspace `kunnnal/leetcode-solutions` contains my programming solutions to various LeetCode problems, categorized by date/month (e.g. `daily/mar`). It serves to track my problem-solving progress and keep a history of algorithmic approaches over time.

## Automation (`auto-push.ps1`)
I use a PowerShell script (`auto-push.ps1`) to automatically watch the directory for any file changes, add them, commit them with a timestamp, and push them to my remote GitHub repository. This removes the manual step of committing every solution.

### How it works
1. **File Watcher**: Listens for any file creation, changes, renames, or deletions in the directory.
2. **Debounce / Timeout**: Waits briefly (1.5 seconds) to batch multiple operations together.
3. **Commit & Push**: Commits everything with the message "LeetCode auto update YYYY-MM-DD HH:mm:ss" and pushes it to `origin main`.
