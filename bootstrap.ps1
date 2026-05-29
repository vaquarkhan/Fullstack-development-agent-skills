param(
  [string]$Target = ".",
  [string]$Tool = "all"
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "Installing fullstack agent skills ($Tool) into $Target"
& (Join-Path $ScriptDir "install.ps1") -Tool $Tool -Target $Target
Write-Host "Done. Start with skills/using-fullstack-agent-skills/SKILL.md"
