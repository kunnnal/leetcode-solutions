#!/bin/bash

# Auto-push script for WSL/Linux
# Equivalent to auto-push.ps1 for PowerShell

REPO_PATH="$(pwd)"
BRANCH="main"
REMOTE="origin"
QUIET_PERIOD=1.5

echo "Starting auto-push watcher in $REPO_PATH"
echo "Watching for file changes... (Ctrl+C to stop)"

while true; do
    # Wait for file system events
    inotifywait -r -e modify,create,delete,move "$REPO_PATH" --exclude '\.git' 2>/dev/null

    # Debounce period
    sleep $QUIET_PERIOD

    # Check if it's a git repository
    if ! git -C "$REPO_PATH" status --short >/dev/null 2>&1; then
        echo "Warning: Not a git repository or git error"
        continue
    fi

    # Add all changes
    git -C "$REPO_PATH" add --all >/dev/null 2>&1

    # Create timestamp
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

    # Commit if there are changes
    if git -C "$REPO_PATH" commit -m "LeetCode auto update $TIMESTAMP" >/dev/null 2>&1; then
        # Push to remote
        if git -C "$REPO_PATH" push "$REMOTE" "$BRANCH" >/dev/null 2>&1; then
            echo "Pushed changes at $TIMESTAMP"
        else
            echo "Warning: git push failed"
        fi
    else
        echo "No changes to commit at $TIMESTAMP"
    fi
done