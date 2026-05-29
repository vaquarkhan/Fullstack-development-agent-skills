# Plugin Publishing

This repository includes a VS Code extension scaffold in `vscode-extension/`.

## Build Extension Package

```bash
cd vscode-extension
npm install
npm run package
```

## Release Artifacts

- Publish `.vsix` files through GitHub Releases
- Keep extension versioning aligned with `registry/assets.json`

## Suggested Release Checklist

- Validate install on VS Code and Cursor
- Verify command palette installers for skills and starter packs
- Update `vscode-extension/README.md` with latest capabilities
