plugins {
    id("java")
    id("org.jetbrains.kotlin.jvm") version "1.9.22"
    id("org.jetbrains.intellij") version "1.17.2"
}

group = "com.vaquarkhan"
version = "0.4.0"

repositories {
    mavenCentral()
}

intellij {
    version.set("2023.3")
    type.set("IC")
    plugins.set(listOf())
}

tasks {
    withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile> {
        kotlinOptions.jvmTarget = "17"
    }

    patchPluginXml {
        sinceBuild.set("233")
        untilBuild.set("243.*")
        changeNotes.set("""
            <h3>0.2.0</h3>
            <ul>
                <li>Install Full Toolkit command</li>
                <li>Install Core Skills command</li>
                <li>Install Platform Preset (with selector)</li>
                <li>Install Starter Pack (with selector)</li>
                <li>Install Agent Adapters</li>
                <li>Install MCP Templates</li>
                <li>Run Session Hook</li>
                <li>53+ fullstack workflow skills</li>
                <li>15 platform presets</li>
                <li>14 starter packs</li>
            </ul>
        """.trimIndent())
    }

    buildSearchableOptions {
        enabled = false
    }

    signPlugin {
        enabled = false
    }
}
