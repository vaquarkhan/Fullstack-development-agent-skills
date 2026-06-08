package com.vaquarkhan.fullstackskills.actions

import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.vaquarkhan.fullstackskills.InstallHelper

class InstallFullToolkitAction : AnAction() {
    override fun actionPerformed(e: AnActionEvent) {
        val project = e.project ?: return
        InstallHelper.installFullToolkit(project)
    }
}
