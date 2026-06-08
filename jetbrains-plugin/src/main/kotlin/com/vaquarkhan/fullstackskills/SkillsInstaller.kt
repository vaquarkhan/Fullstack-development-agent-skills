package com.vaquarkhan.fullstackskills

import com.intellij.openapi.project.Project
import com.intellij.openapi.vfs.LocalFileSystem
import java.io.File
import java.io.InputStream
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.StandardCopyOption

object SkillsInstaller {

    fun installPaths(project: Project, paths: List<String>): Int {
        val basePath = project.basePath ?: return 0
        val targetDir = File(basePath)
        var count = 0

        for (relativePath in paths) {
            val resourceStream = getResourceStream(relativePath)
            if (resourceStream != null) {
                val targetFile = File(targetDir, relativePath)
                targetFile.parentFile?.mkdirs()
                Files.copy(resourceStream, targetFile.toPath(), StandardCopyOption.REPLACE_EXISTING)
                resourceStream.close()
                count++
            } else {
                // Try as directory - copy all files within
                count += copyResourceDirectory(relativePath, targetDir)
            }
        }

        // Refresh VFS
        LocalFileSystem.getInstance().refresh(true)
        return count
    }

    fun installDirectory(project: Project, dirPath: String): Int {
        val basePath = project.basePath ?: return 0
        val targetDir = File(basePath)
        return copyResourceDirectory(dirPath, targetDir)
    }

    fun installFile(project: Project, filePath: String): Boolean {
        val basePath = project.basePath ?: return false
        val targetFile = File(basePath, filePath)
        val resourceStream = getResourceStream(filePath) ?: return false

        targetFile.parentFile?.mkdirs()
        Files.copy(resourceStream, targetFile.toPath(), StandardCopyOption.REPLACE_EXISTING)
        resourceStream.close()

        LocalFileSystem.getInstance().refresh(true)
        return true
    }

    private fun getResourceStream(path: String): InputStream? {
        return SkillsInstaller::class.java.classLoader.getResourceAsStream("skills/$path")
    }

    private fun copyResourceDirectory(dirPath: String, targetDir: File): Int {
        val indexStream = getResourceStream("$dirPath/.index") ?: return 0
        val files = indexStream.bufferedReader().readLines().filter { it.isNotBlank() }
        indexStream.close()

        var count = 0
        for (file in files) {
            val fullPath = "$dirPath/$file"
            val stream = getResourceStream(fullPath) ?: continue
            val target = File(targetDir, fullPath)
            target.parentFile?.mkdirs()
            Files.copy(stream, target.toPath(), StandardCopyOption.REPLACE_EXISTING)
            stream.close()
            count++
        }
        return count
    }
}
