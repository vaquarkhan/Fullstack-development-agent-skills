plugins {
    id("java")
    id("org.jetbrains.kotlin.jvm") version "1.9.22"
    id("org.jetbrains.intellij") version "1.17.2"
}

group = "com.vaquarkhan"
version = "0.5.0"

repositories {
    mavenCentral()
}

intellij {
    version.set("2023.3")
    type.set("IC")
    plugins.set(listOf())
}

tasks.register<Exec>("bundlePluginAssets") {
    group = "build"
    description = "Copy repository skills and assets into plugin resources"
    workingDir = rootProject.projectDir.parentFile
    commandLine("python", "scripts/bundle-plugin-assets.py")
}

tasks.named("processResources") {
    dependsOn("bundlePluginAssets")
}

tasks {
    withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile> {
        kotlinOptions.jvmTarget = "17"
    }

    patchPluginXml {
        sinceBuild.set("233")
        untilBuild.set("243.*")
        changeNotes.set("""
            <h3>0.5.0</h3>
            <ul>
                <li>117 skills (72 core + 45 stack packs)</li>
                <li>Full toolkit install: skills, skill-packs, presets, starter packs, references, examples</li>
                <li>20 starter packs and 15 platform presets</li>
                <li>NestJS, .NET, Rust, Kotlin, Flutter, MongoDB, Elasticsearch, LangChain, Vercel AI SDK packs</li>
            </ul>
            <h3>0.4.0</h3>
            <ul>
                <li>Skill packs for Java Spring Boot, Python, Go, PHP, Ruby</li>
            </ul>
        """.trimIndent())
    }

    buildSearchableOptions {
        enabled = false
    }

    signPlugin {
        enabled = false
    }

    publishPlugin {
        dependsOn("bundlePluginAssets")
        token.set(System.getenv("PUBLISH_TOKEN"))
        channels.set(listOf("default"))
    }
}
