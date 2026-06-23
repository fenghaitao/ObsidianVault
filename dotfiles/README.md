# dotfiles

Snippets that aren't part of the wiki — they're shell/editor configuration that
travels with the vault so we can apply the same setup on every machine where
Obsidian + Lean Terminal is installed.

## `powershell/Microsoft.PowerShell_profile.snippet.ps1`

PSReadLine color overrides for the Lean Terminal Obsidian plugin (Solarized Light
theme). Without these, `git pull --rebase` and friends render with a grey
`Command`/`Parameter` token that's nearly unreadable against the cream
background.

### Apply on a new machine

1. Open PowerShell 7 (`pwsh`) — the same shell Lean Terminal spawns on Windows.

2. Locate your profile:
   ```powershell
   $PROFILE
   ```
   Typical paths:
   - `~\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`
   - `~\OneDrive\Documents\PowerShell\Microsoft.PowerShell_profile.ps1` (if Documents is OneDrive-redirected)
   - `~\OneDrive - <Org>\Documents\PowerShell\Microsoft.PowerShell_profile.ps1` (Intel-style enterprise redirect)

3. Make sure the directory exists, then append the snippet:
   ```powershell
   New-Item -ItemType Directory -Force -Path (Split-Path $PROFILE) | Out-Null
   Get-Content "<vault>\dotfiles\powershell\Microsoft.PowerShell_profile.snippet.ps1" |
     Add-Content $PROFILE
   ```

4. Restart the Lean Terminal pane (close it fully — the trash icon, not just
   hide the panel — so `node-pty` releases the pwsh process), then open a fresh
   terminal.

### Verify it took

```powershell
(Get-PSReadLineOption).CommandColor
# Expect an ANSI escape containing 38;2;38;139;210  (RGB for #268bd2)
```

### Tweaking

Each line in the `Set-PSReadLineOption -Colors` block has a comment explaining
what token it paints. Swap the hex on any line and reload the profile
(`. $PROFILE`) — no restart needed.

Solarized accent palette for reference:

| Hex       | Name    |
|-----------|---------|
| `#dc322f` | red     |
| `#cb4b16` | orange  |
| `#b58900` | yellow  |
| `#859900` | green   |
| `#2aa198` | cyan    |
| `#268bd2` | blue    |
| `#6c71c4` | violet  |
| `#d33682` | magenta |
| `#073642` | base02 (near-black, high contrast on cream bg) |
| `#586e75` | base01 (medium grey — visible but clearly "secondary") |
