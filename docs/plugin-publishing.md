# Plugin Publishing

This repository includes VS Code and JetBrains extensions for installing the full toolkit (117 skills: 72 core + 45 packs).

## Prerequisites

Set GitHub repository secrets for automated marketplace publish:

| Secret | Used for | How to obtain |
| --- | --- | --- |
| `VSCE_PAT` | VS Code Marketplace | [Azure DevOps PAT](https://dev.azure.com/) with **Marketplace > Manage** scope; run `npx vsce login ViquarKhan` locally to verify |
| `PUBLISH_TOKEN` | JetBrains Marketplace | [JetBrains Plugin Portal](https://plugins.jetbrains.com/author/me) → Authentication → Generate token |

## Bundle Assets

Both plugins bundle skills from the repo root before packaging:

```bash
python scripts/bundle-plugin-assets.py
```

## VS Code Extension

```bash
cd vscode-extension
npm install
npm run package    # creates fullstack-development-agent-skills-<version>.vsix
npm run publish    # requires VSCE_PAT env var or vsce login
```

Publish `.vsix` files through [GitHub Releases](https://github.com/vaquarkhan/Fullstack-development-agent-skills/releases) and the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ViquarKhan.fullstack-development-agent-skills).

## JetBrains Plugin

```bash
cd jetbrains-plugin
./gradlew buildPlugin   # ZIP in build/distributions/
PUBLISH_TOKEN=... ./gradlew publishPlugin
```

Publish `.zip` from `build/distributions/` to the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/32167-fullstack-development-agent-skills).

## CI Publish

Workflow `.github/workflows/publish-plugins.yml` runs on GitHub **Release published** or **workflow_dispatch** when secrets are configured.

## Version Alignment

Keep extension versions aligned with `registry/assets.json` (currently v0.5.0). Run:

```bash
python scripts/validate-version-sync.py
```

## Suggested Release Checklist

- Run `python scripts/bundle-plugin-assets.py`
- Validate install on VS Code, Cursor, and JetBrains IDEs
- Verify full toolkit installs `skills/` and `skill-packs/`
- Update plugin READMEs with latest skill counts
- Tag `v0.5.0` and attach `.vsix` + `.zip` to GitHub Release
- Run publish workflow or `vsce publish` / `gradlew publishPlugin` with tokens
