import * as vscode from "vscode";
import * as fs from "fs";
import * as path from "path";

const REPO_URL = "https://github.com/vaquarkhan/Fullstack-development-agent-skills";

interface AssetGroup {
  label: string;
  description: string;
  paths: string[];
}

const ASSET_GROUPS: Record<string, AssetGroup> = {
  core: {
    label: "Core Skills Pack",
    description: "Essential fullstack workflow skills",
    paths: [
      "skills/using-fullstack-agent-skills",
      "skills/fullstack-product-specification",
      "skills/react-nextjs-frontend-architecture",
      "skills/nodejs-nestjs-backend-microservices",
      "skills/authentication-and-authorization-fullstack",
      "skills/fullstack-testing-and-quality-gates",
      "skills/fullstack-observability-and-release-engineering",
    ],
  },
  adapters: {
    label: "Agent Adapters",
    description: "Multi-agent configuration files",
    paths: [
      ".cursor/commands",
      ".claude/commands",
      ".gemini/commands",
      ".kiro/steering",
      ".opencode",
      "AGENTS.md",
      "CLAUDE.md",
    ],
  },
  mcp: {
    label: "MCP Templates",
    description: "Model Context Protocol configurations",
    paths: ["mcp"],
  },
  examples: {
    label: "Architecture Examples",
    description: "End-to-end architecture blueprints",
    paths: ["examples"],
  },
  hooks: {
    label: "Operational Hooks",
    description: "Session and release guardrails",
    paths: ["hooks"],
  },
};

const PRESETS = [
  { label: "React / Next.js Frontend", path: "presets/react-nextjs-frontend" },
  { label: "Fullstack TypeScript Monorepo", path: "presets/fullstack-typescript-monorepo" },
  { label: "Angular Frontend", path: "presets/angular-frontend" },
  { label: "Vue / Nuxt Frontend", path: "presets/vue-nuxt-frontend" },
  { label: "Node.js Microservices", path: "presets/nodejs-microservices" },
  { label: "Java Spring Boot Microservices", path: "presets/java-spring-boot-microservices" },
  { label: ".NET / ASP.NET Core Microservices", path: "presets/dotnet-aspnet-core-microservices" },
  { label: "AWS Fullstack Development", path: "presets/aws-fullstack-development" },
  { label: "Azure Fullstack Development", path: "presets/azure-fullstack-development" },
  { label: "GCP Fullstack Development", path: "presets/gcp-fullstack-development" },
  { label: "AWS Serverless Fullstack", path: "presets/aws-serverless-fullstack" },
  { label: "Azure Serverless Fullstack", path: "presets/azure-serverless-fullstack" },
  { label: "GCP Serverless Fullstack", path: "presets/gcp-serverless-fullstack" },
  { label: "Kubernetes Fullstack Platform", path: "presets/kubernetes-fullstack-platform" },
  { label: "Vercel / Jamstack", path: "presets/vercel-nextjs-jamstack" },
];

const STARTER_PACKS = [
  { label: "Fullstack MVP Starter", file: "starter-packs/fullstack-mvp-starter.yaml" },
  { label: "Enterprise Modernization", file: "starter-packs/enterprise-modernization-starter.yaml" },
  { label: "Platform Reliability", file: "starter-packs/platform-reliability-starter.yaml" },
  { label: "SaaS Multi-Tenant", file: "starter-packs/saas-multi-tenant-starter.yaml" },
  { label: "Payments & Subscriptions", file: "starter-packs/payments-and-subscriptions-starter.yaml" },
  { label: "Incident Hardening & SLO", file: "starter-packs/incident-hardening-and-slo-starter.yaml" },
  { label: "Microservice Patterns & Edge Security", file: "starter-packs/microservice-patterns-and-edge-security-starter.yaml" },
  { label: "Microservices Architecture Modernization", file: "starter-packs/microservices-architecture-modernization-starter.yaml" },
  { label: "Identity, Edge & Global Delivery", file: "starter-packs/identity-edge-and-global-delivery-starter.yaml" },
  { label: "UI Production Excellence", file: "starter-packs/ui-production-excellence-starter.yaml" },
  { label: "AWS Serverless Fullstack", file: "starter-packs/aws-serverless-fullstack-starter.yaml" },
  { label: "Azure Serverless Fullstack", file: "starter-packs/azure-serverless-fullstack-starter.yaml" },
  { label: "GCP Serverless Fullstack", file: "starter-packs/gcp-serverless-fullstack-starter.yaml" },
  { label: "Multi-Cloud Platform", file: "starter-packs/multi-cloud-fullstack-platform-starter.yaml" },
  { label: "Data Platform & Events", file: "starter-packs/data-platform-and-events-starter.yaml" },
  { label: "Compliance & Privacy", file: "starter-packs/compliance-privacy-starter.yaml" },
  { label: "AI Features", file: "starter-packs/ai-features-starter.yaml" },
  { label: "Mobile Fullstack", file: "starter-packs/mobile-fullstack-starter.yaml" },
  { label: "Chaos & SRE", file: "starter-packs/chaos-sre-starter.yaml" },
  { label: "GitOps CI/CD", file: "starter-packs/gitops-cicd-starter.yaml" },
];

export function activate(context: vscode.ExtensionContext): void {
  const extensionRoot = context.extensionPath;

  // Install Full Toolkit
  context.subscriptions.push(
    vscode.commands.registerCommand("fullstackSkills.installFullToolkit", async () => {
      const target = await getTargetFolder();
      if (!target) return;

      const groups = ["core", "adapters", "mcp", "examples", "hooks"];
      for (const group of groups) {
        await copyAssetGroup(extensionRoot, target, group);
      }

      // Copy all skills and packs
      await copyDirectory(path.join(extensionRoot, "skills"), path.join(target, "skills"));
      await copyDirectory(path.join(extensionRoot, "skill-packs"), path.join(target, "skill-packs"));
      // Copy all presets
      await copyDirectory(path.join(extensionRoot, "presets"), path.join(target, "presets"));
      // Copy starter packs
      await copyDirectory(path.join(extensionRoot, "starter-packs"), path.join(target, "starter-packs"));
      // Copy references
      await copyDirectory(path.join(extensionRoot, "references"), path.join(target, "references"));
      // Copy scripts
      await copyDirectory(path.join(extensionRoot, "scripts"), path.join(target, "scripts"));

      vscode.window.showInformationMessage(
        `✅ Fullstack Agent Skills toolkit installed to: ${target}`
      );
    })
  );

  // Install Core Pack
  context.subscriptions.push(
    vscode.commands.registerCommand("fullstackSkills.installCorePack", async () => {
      const target = await getTargetFolder();
      if (!target) return;
      await copyAssetGroup(extensionRoot, target, "core");
      vscode.window.showInformationMessage("✅ Core skills pack installed.");
    })
  );

  // Install Agent Adapters
  context.subscriptions.push(
    vscode.commands.registerCommand("fullstackSkills.installAgentAdapters", async () => {
      const target = await getTargetFolder();
      if (!target) return;
      await copyAssetGroup(extensionRoot, target, "adapters");
      vscode.window.showInformationMessage("✅ Agent adapters installed.");
    })
  );

  // Install Starter Pack
  context.subscriptions.push(
    vscode.commands.registerCommand("fullstackSkills.installStarterPack", async () => {
      const target = await getTargetFolder();
      if (!target) return;

      const picked = await vscode.window.showQuickPick(
        STARTER_PACKS.map((sp) => ({ label: sp.label, detail: sp.file })),
        { placeHolder: "Select a starter pack" }
      );
      if (!picked) return;

      const src = path.join(extensionRoot, picked.detail!);
      const dest = path.join(target, picked.detail!);
      await ensureDir(path.dirname(dest));
      fs.copyFileSync(src, dest);
      vscode.window.showInformationMessage(`✅ Starter pack "${picked.label}" installed.`);
    })
  );

  // Install MCP Templates
  context.subscriptions.push(
    vscode.commands.registerCommand("fullstackSkills.installMCPTemplates", async () => {
      const target = await getTargetFolder();
      if (!target) return;
      await copyAssetGroup(extensionRoot, target, "mcp");
      vscode.window.showInformationMessage("✅ MCP templates installed.");
    })
  );

  // Install Examples
  context.subscriptions.push(
    vscode.commands.registerCommand("fullstackSkills.installExamples", async () => {
      const target = await getTargetFolder();
      if (!target) return;
      await copyAssetGroup(extensionRoot, target, "examples");
      vscode.window.showInformationMessage("✅ Architecture examples installed.");
    })
  );

  // Install Platform Preset
  context.subscriptions.push(
    vscode.commands.registerCommand("fullstackSkills.installPreset", async () => {
      const target = await getTargetFolder();
      if (!target) return;

      const picked = await vscode.window.showQuickPick(
        PRESETS.map((p) => ({ label: p.label, detail: p.path })),
        { placeHolder: "Select a platform preset" }
      );
      if (!picked) return;

      const src = path.join(extensionRoot, picked.detail!);
      const dest = path.join(target, picked.detail!);
      await copyDirectory(src, dest);
      vscode.window.showInformationMessage(`✅ Preset "${picked.label}" installed.`);
    })
  );

  // Open Skills Index
  context.subscriptions.push(
    vscode.commands.registerCommand("fullstackSkills.openSkillsIndex", async () => {
      const indexPath = path.join(extensionRoot, "skills-index.md");
      if (fs.existsSync(indexPath)) {
        const doc = await vscode.workspace.openTextDocument(vscode.Uri.file(indexPath));
        await vscode.window.showTextDocument(doc, { preview: true });
      } else {
        vscode.env.openExternal(vscode.Uri.parse(`${REPO_URL}#skill-pack`));
      }
    })
  );

  // Run Session Hook
  context.subscriptions.push(
    vscode.commands.registerCommand("fullstackSkills.runSessionHook", async () => {
      const workspace = vscode.workspace.workspaceFolders?.[0];
      if (!workspace) {
        vscode.window.showWarningMessage("Open a workspace folder first.");
        return;
      }

      const hookPath = path.join(workspace.uri.fsPath, "hooks", "session-start.sh");
      if (!fs.existsSync(hookPath)) {
        vscode.window.showWarningMessage("No session-start.sh hook found. Install hooks first.");
        return;
      }

      const terminal = vscode.window.createTerminal("FS Skills: Session Hook");
      terminal.show();
      terminal.sendText(`bash "${hookPath}"`);
    })
  );
}

async function getTargetFolder(): Promise<string | undefined> {
  const workspace = vscode.workspace.workspaceFolders?.[0];
  if (workspace) {
    return workspace.uri.fsPath;
  }

  const selected = await vscode.window.showOpenDialog({
    canSelectFiles: false,
    canSelectFolders: true,
    canSelectMany: false,
    openLabel: "Select Target Folder",
  });

  return selected?.[0]?.fsPath;
}

async function copyAssetGroup(
  extensionRoot: string,
  target: string,
  groupKey: string
): Promise<void> {
  const group = ASSET_GROUPS[groupKey];
  if (!group) return;

  for (const assetPath of group.paths) {
    const src = path.join(extensionRoot, assetPath);
    const dest = path.join(target, assetPath);

    if (!fs.existsSync(src)) continue;

    const stat = fs.statSync(src);
    if (stat.isDirectory()) {
      await copyDirectory(src, dest);
    } else {
      await ensureDir(path.dirname(dest));
      fs.copyFileSync(src, dest);
    }
  }
}

async function copyDirectory(src: string, dest: string): Promise<void> {
  if (!fs.existsSync(src)) return;
  await ensureDir(dest);

  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);

    if (entry.isDirectory()) {
      await copyDirectory(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

async function ensureDir(dir: string): Promise<void> {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

export function deactivate(): void {}
