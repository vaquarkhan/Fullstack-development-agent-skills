import * as vscode from "vscode";
import * as path from "path";

export function activate(context: vscode.ExtensionContext): void {
  const installAll = vscode.commands.registerCommand(
    "fullstackAgentSkills.installAll",
    async () => {
      const workspace = vscode.workspace.workspaceFolders?.[0];
      if (!workspace) {
        vscode.window.showErrorMessage("Open a workspace folder before installing skills.");
        return;
      }

      const target = workspace.uri.fsPath;
      const repoRoot = path.resolve(context.extensionPath, "..");
      const message = [
        "Install toolkit assets into workspace:",
        target,
        "",
        "Suggested command:",
        `scripts/install.sh all "${target}"`,
        "",
        `Source repo: ${repoRoot}`,
      ].join("\n");

      await vscode.window.showInformationMessage(message, { modal: true });
    }
  );

  const openSkillsIndex = vscode.commands.registerCommand(
    "fullstackAgentSkills.openSkillsIndex",
    async () => {
      const doc = await vscode.workspace.openTextDocument(
        vscode.Uri.file(path.resolve(context.extensionPath, "../skills-index.md"))
      );
      await vscode.window.showTextDocument(doc);
    }
  );

  context.subscriptions.push(installAll, openSkillsIndex);
}

export function deactivate(): void {}
