# =============================================================================
# Lean Terminal / PSReadLine color fix
# =============================================================================
# Problem: PSReadLine overrides terminal colors on the command line with its own
# palette. On light themes (e.g. Lean Terminal's Solarized Light), the default
# greys for Command/Parameter/InlinePrediction tokens wash out against the cream
# background and become hard to read.
#
# Fix: pin the relevant token colors to crisp Solarized accents. The terminal
# theme's `foreground` only governs raw program output (e.g. `echo hello`); the
# command line you're typing is owned by PSReadLine.
#
# Apply: paste this block at the end of $PROFILE
#   (typically:  Documents\PowerShell\Microsoft.PowerShell_profile.ps1
#    or under OneDrive\Documents\... if Documents is OneDrive-redirected)
# =============================================================================

if (Get-Module -ListAvailable PSReadLine) {
  Import-Module PSReadLine
  Set-PSReadLineOption -Colors @{
    InlinePrediction = '#073642'   # solarized base02 - prediction ghost text
    Default          = '#073642'   # base02 - typed text fallback
    Command          = '#268bd2'   # blue    - command name (git, ls, ...)
    Parameter        = '#859900'   # green   - flags (--rebase, -la, ...)
    String           = '#2aa198'   # cyan    - quoted strings
    Number           = '#d33682'   # magenta - numeric literals
  }
}
