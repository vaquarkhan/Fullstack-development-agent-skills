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
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "copilot" {
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "codex" {
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "generic" {
    Copy-IfExists "skills" (Join-Path $Target "skills")
    Copy-IfExists "presets" (Join-Path $Target "presets")
    Copy-IfExists "references" (Join-Path $Target "references")
    Copy-IfExists "templates" (Join-Path $Target "templates")
    Copy-IfExists "starter-packs" (Join-Path $Target "starter-packs")
  }
  "all" {
    Copy-IfExists ".cursor" (Join-Path $Target ".cursor")
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
    throw "Unsupported tool '$Tool'. Supported tools: cursor, claude, copilot, codex, generic, all"
  }
}

Write-Host "Installed '$Tool' assets into $Target"
