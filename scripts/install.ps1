param(
  [Parameter(Mandatory = $true)]
  [string]$Tool,
  [Parameter(Mandatory = $true)]
  [string]$Target
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not (Test-Path $Target)) {
  New-Item -ItemType Directory -Path $Target | Out-Null
}

function Copy-IfExists {
  param(
    [string]$SourcePath,
    [string]$DestinationPath
  )
  if (Test-Path $SourcePath) {
    $parent = Split-Path -Parent $DestinationPath
    if (-not (Test-Path $parent)) {
      New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }
    Copy-Item -Path $SourcePath -Destination $DestinationPath -Recurse -Force
  }
}

switch ($Tool) {
  "cursor" {
    Copy-IfExists ".cursor" (Join-Path $Target ".cursor")
    Copy-IfExists "skills" (Join-Path $Target "skills")
  }
  "claude" {
    Copy-IfExists ".claude" (Join-Path $Target ".claude")
    Copy-IfExists "CLAUDE.md" (Join-Path $Target "CLAUDE.md")
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "gemini" {
    Copy-IfExists ".gemini" (Join-Path $Target ".gemini")
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "kiro" {
    Copy-IfExists ".kiro" (Join-Path $Target ".kiro")
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "opencode" {
    Copy-IfExists ".opencode" (Join-Path $Target ".opencode")
    Copy-IfExists "AGENTS.md" (Join-Path $Target "AGENTS.md")
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "windsurf" {
    Copy-IfExists ".windsurfrules.example" (Join-Path $Target ".windsurfrules.example")
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "copilot" {
    Copy-IfExists "AGENTS.md" (Join-Path $Target "AGENTS.md")
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "codex" {
    Copy-IfExists "AGENTS.md" (Join-Path $Target "AGENTS.md")
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "generic" {
    Copy-IfExists "AGENTS.md" (Join-Path $Target "AGENTS.md")
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "all" {
    Copy-IfExists ".cursor" (Join-Path $Target ".cursor")
    Copy-IfExists ".claude" (Join-Path $Target ".claude")
    Copy-IfExists ".gemini" (Join-Path $Target ".gemini")
    Copy-IfExists ".kiro" (Join-Path $Target ".kiro")
    Copy-IfExists ".opencode" (Join-Path $Target ".opencode")
    Copy-IfExists ".windsurfrules.example" (Join-Path $Target ".windsurfrules.example")
    Copy-IfExists "AGENTS.md" (Join-Path $Target "AGENTS.md")
    Copy-IfExists "CLAUDE.md" (Join-Path $Target "CLAUDE.md")
    Copy-IfExists "agents" (Join-Path $Target "agents")
    Copy-IfExists "docs" (Join-Path $Target "docs")
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
    Copy-IfExists "registry" (Join-Path $Target "registry")
  }
  default {
    throw "Unsupported tool '$Tool'. Supported tools: cursor, claude, gemini, kiro, opencode, windsurf, copilot, codex, generic, all"
  }
}

Write-Host "Installed '$Tool' assets into $Target"
