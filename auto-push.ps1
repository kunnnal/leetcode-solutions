$global:autoPushRepoPath = (Get-Location).Path
$branch = "main"
$remote = "origin"
$quietPeriodMs = 1500

$global:autoPushState = [hashtable]::Synchronized(@{
    Pending = $false
    LastChange = Get-Date
    IsProcessing = $false
})

function Invoke-AutoPush {
    param(
        [string]$RepoPath,
        [string]$Branch,
        [string]$Remote
    )

    Push-Location $RepoPath
    try {
        git status --short | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Warning "Git status failed. Check the repository before retrying."
            return
        }

        git add --all
        if ($LASTEXITCODE -ne 0) {
            Write-Warning "git add failed."
            return
        }

        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        git commit -m "LeetCode auto update $timestamp" | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Host "No commit created. Nothing new to push."
            return
        }

        git push $Remote $Branch
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Pushed changes at $timestamp"
        }
        else {
            Write-Warning "git push failed."
        }
    }
    finally {
        Pop-Location
    }
}

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $global:autoPushRepoPath
$watcher.Filter = "*"
$watcher.IncludeSubdirectories = $true
$watcher.NotifyFilter = [System.IO.NotifyFilters]'FileName, DirectoryName, LastWrite, CreationTime'
$watcher.EnableRaisingEvents = $true

$markPending = {
    $fullPath = $Event.SourceEventArgs.FullPath
    if ($fullPath -like "$global:autoPushRepoPath\.git*") {
        return
    }

    $global:autoPushState.Pending = $true
    $global:autoPushState.LastChange = Get-Date
}

$subscriptions = @(
    Register-ObjectEvent $watcher Created -SourceIdentifier "AutoPush.Created" -Action $markPending
    Register-ObjectEvent $watcher Changed -SourceIdentifier "AutoPush.Changed" -Action $markPending
    Register-ObjectEvent $watcher Deleted -SourceIdentifier "AutoPush.Deleted" -Action $markPending
    Register-ObjectEvent $watcher Renamed -SourceIdentifier "AutoPush.Renamed" -Action $markPending
)

Write-Host "Auto GitHub upload is running for $global:autoPushRepoPath"

try {
    while ($true) {
        Start-Sleep -Milliseconds 500

        if (-not $global:autoPushState.Pending -or $global:autoPushState.IsProcessing) {
            continue
        }

        $elapsedMs = ((Get-Date) - $global:autoPushState.LastChange).TotalMilliseconds
        if ($elapsedMs -lt $quietPeriodMs) {
            continue
        }

        $global:autoPushState.Pending = $false
        $global:autoPushState.IsProcessing = $true

        try {
            Invoke-AutoPush -RepoPath $global:autoPushRepoPath -Branch $branch -Remote $remote
        }
        finally {
            $global:autoPushState.IsProcessing = $false
        }
    }
}
finally {
    foreach ($subscription in $subscriptions) {
        Unregister-Event -SourceIdentifier $subscription.SourceIdentifier -ErrorAction SilentlyContinue
        Remove-Job -Id $subscription.Id -Force -ErrorAction SilentlyContinue
    }

    $watcher.Dispose()
}
