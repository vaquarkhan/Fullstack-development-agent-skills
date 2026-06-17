package com.vaquarkhan.fullstackskills

import com.intellij.openapi.project.Project
import com.intellij.openapi.wm.ToolWindow
import com.intellij.openapi.wm.ToolWindowFactory
import com.intellij.ui.content.ContentFactory
import javax.swing.*
import java.awt.*

class SkillsToolWindowFactory : ToolWindowFactory {

    override fun createToolWindowContent(project: Project, toolWindow: ToolWindow) {
        val panel = createPanel(project)
        val content = ContentFactory.getInstance().createContent(panel, "Skills", false)
        toolWindow.contentManager.addContent(content)
    }

    private fun createPanel(project: Project): JPanel {
        val panel = JPanel(BorderLayout())

        val headerPanel = JPanel().apply {
            layout = BoxLayout(this, BoxLayout.Y_AXIS)
            border = BorderFactory.createEmptyBorder(12, 12, 12, 12)

            add(JLabel("<html><b>Fullstack Agent Skills</b></html>").apply {
                font = font.deriveFont(16f)
                alignmentX = Component.LEFT_ALIGNMENT
            })
            add(Box.createVerticalStrut(4))
            add(JLabel("<html><i>117 skills (72 core + 45 packs) for fullstack AI delivery</i></html>").apply {
                foreground = Color.GRAY
                alignmentX = Component.LEFT_ALIGNMENT
            })
        }

        val buttonsPanel = JPanel().apply {
            layout = BoxLayout(this, BoxLayout.Y_AXIS)
            border = BorderFactory.createEmptyBorder(8, 12, 12, 12)
        }

        val actions = listOf(
            "▶ Install Full Toolkit" to { InstallHelper.installFullToolkit(project) },
            "▶ Install Core Skills" to { InstallHelper.installCoreSkills(project) },
            "▶ Install Platform Preset" to { InstallHelper.installPreset(project) },
            "▶ Install Starter Pack" to { InstallHelper.installStarterPack(project) },
            "▶ Install Agent Adapters" to { InstallHelper.installAdapters(project) },
            "▶ Install MCP Templates" to { InstallHelper.installMCP(project) },
            "▶ Run Session Hook" to { InstallHelper.runSessionHook(project) }
        )

        for ((label, action) in actions) {
            val btn = JButton(label).apply {
                alignmentX = Component.LEFT_ALIGNMENT
                maximumSize = Dimension(Int.MAX_VALUE, 36)
                addActionListener { action() }
            }
            buttonsPanel.add(btn)
            buttonsPanel.add(Box.createVerticalStrut(6))
        }

        panel.add(headerPanel, BorderLayout.NORTH)
        panel.add(JScrollPane(buttonsPanel), BorderLayout.CENTER)

        return panel
    }
}
