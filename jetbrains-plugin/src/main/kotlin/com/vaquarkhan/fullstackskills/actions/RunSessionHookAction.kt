package com.vaquarkhan.fullstackskills.actions

import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.vaquarkhan.fullstackskills.InstallHelper

class RunSessionHookAction : AnAction() {
    override fun actionPerformed(e: AnActionEvent) {
        val project = e.project ?: return
        InstallHelper.runSessionHook(project)
    }
}
