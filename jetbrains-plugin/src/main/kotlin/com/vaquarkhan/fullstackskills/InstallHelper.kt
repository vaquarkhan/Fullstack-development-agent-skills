package com.vaquarkhan.fullstackskills

import com.intellij.notification.NotificationGroupManager
import com.intellij.notification.NotificationType
import com.intellij.openapi.project.Project
import com.intellij.openapi.ui.popup.JBPopupFactory
import com.intellij.openapi.ui.popup.PopupStep
import com.intellij.openapi.ui.popup.util.BaseListPopupStep
import com.intellij.execution.configurations.GeneralCommandLine
import com.intellij.execution.process.OSProcessHandler
import com.intellij.execution.process.ProcessTerminatedListener
import com.intellij.openapi.wm.ToolWindowManager
import java.io.File

object InstallHelper {

    fun installFullToolkit(project: Project) {
        val count = SkillsInstaller.installPaths(project, SkillsConstants.CORE_SKILLS)
        val adapterCount = SkillsInstaller.installPaths(project, SkillsConstants.ADAPTER_PATHS)
        val mcpCount = SkillsInstaller.installPaths(project, SkillsConstants.MCP_PATHS)
        notify(project, "Full toolkit installed ($count skills, $adapterCount adapters, $mcpCount MCP templates)")
    }

    fun installCoreSkills(project: Project) {
        val count = SkillsInstaller.installPaths(project, SkillsConstants.CORE_SKILLS)
        notify(project, "Core skills installed ($count items)")
    }

    fun installPreset(project: Project) {
        val presets = SkillsConstants.PRESETS.keys.toList()
        showSelector(project, "Select Platform Preset", presets) { selected ->
            val path = SkillsConstants.PRESETS[selected] ?: return@showSelector
            val count = SkillsInstaller.installDirectory(project, path)
            notify(project, "Preset '$selected' installed ($count files)")
        }
    }

    fun installStarterPack(project: Project) {
        val packs = SkillsConstants.STARTER_PACKS.keys.toList()
        showSelector(project, "Select Starter Pack", packs) { selected ->
            val path = SkillsConstants.STARTER_PACKS[selected] ?: return@showSelector
            val success = SkillsInstaller.installFile(project, path)
            if (success) {
                notify(project, "Starter pack '$selected' installed")
            } else {
                notify(project, "Failed to install '$selected'", NotificationType.WARNING)
            }
        }
    }

    fun installAdapters(project: Project) {
        val count = SkillsInstaller.installPaths(project, SkillsConstants.ADAPTER_PATHS)
        notify(project, "Agent adapters installed ($count items)")
    }

    fun installMCP(project: Project) {
        val count = SkillsInstaller.installPaths(project, SkillsConstants.MCP_PATHS)
        notify(project, "MCP templates installed ($count items)")
    }

    fun runSessionHook(project: Project) {
        val basePath = project.basePath ?: return
        val hookFile = File(basePath, "hooks/session-start.sh")

        if (!hookFile.exists()) {
            notify(project, "No session-start.sh hook found. Install hooks first.", NotificationType.WARNING)
            return
        }

        try {
            val cmd = GeneralCommandLine("bash", hookFile.absolutePath)
            cmd.workDirectory = File(basePath)
            val handler = OSProcessHandler(cmd)
            ProcessTerminatedListener.attach(handler)
            handler.startNotify()
            notify(project, "Session hook started")
        } catch (e: Exception) {
            notify(project, "Failed to run hook: ${e.message}", NotificationType.ERROR)
        }
    }

    private fun showSelector(project: Project, title: String, items: List<String>, onSelect: (String) -> Unit) {
        val step = object : BaseListPopupStep<String>(title, items) {
            override fun onChosen(selectedValue: String, finalChoice: Boolean): PopupStep<*>? {
                onSelect(selectedValue)
                return FINAL_CHOICE
            }
        }
        JBPopupFactory.getInstance().createListPopup(step).showCenteredInCurrentWindow(project)
    }

    private fun notify(project: Project, message: String, type: NotificationType = NotificationType.INFORMATION) {
        NotificationGroupManager.getInstance()
            .getNotificationGroup("Fullstack Agent Skills")
            .createNotification(message, type)
            .notify(project)
    }
}
