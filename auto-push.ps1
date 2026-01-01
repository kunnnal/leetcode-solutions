$repoPath = Get-Location

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $repoPath
$watcher.Filter = "*.*"
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true

$action = {
    Start-Sleep -Milliseconds 1000
    git add .
    git commit -m "LeetCode auto update $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" 2>$null
    git push origin main
}

Register-ObjectEvent $watcher Created -Action $action | Out-Null
Register-ObjectEvent $watcher Changed -Action $action | Out-Null
Register-ObjectEvent $watcher Deleted -Action $action | Out-Null
Register-ObjectEvent $watcher Renamed -Action $action | Out-Null

Write-Host "Auto GitHub upload is running..."
while ($true) {
    Start-Sleep 5
}
