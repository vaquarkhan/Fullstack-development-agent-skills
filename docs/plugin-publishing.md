# Plugin Publishing

This repository includes VS Code and JetBrains extensions for installing the full toolkit (106 skills: 72 core + 34 packs).

## VS Code Extension

```bash
cd vscode-extension
npm install
npm run package
```

Publish `.vsix` files through GitHub Releases and the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ViquarKhan.fullstack-development-agent-skills).

## JetBrains Plugin

```bash
cd jetbrains-plugin
./gradlew buildPlugin
```

Publish `.zip` from `build/distributions/` to the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/32167-fullstack-development-agent-skills).

## Version Alignment

Keep extension versions aligned with `registry/assets.json` (currently v0.4.0). Run:

```bash
python scripts/validate-version-sync.py
```

## Suggested Release Checklist

- Validate install on VS Code, Cursor, and JetBrains IDEs
- Verify command palette / menu installers for skills, skill packs, and starter packs
- Update `vscode-extension/README.md` and `jetbrains-plugin/README.md` with latest counts
- Regenerate `registry/assets.json` and `skills-index.md`
- Run full validation suite before tagging
