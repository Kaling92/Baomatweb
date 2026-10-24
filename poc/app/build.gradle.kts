plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "edu.example.a11ylab"
    compileSdk = 35

    defaultConfig {
        applicationId = "edu.example.a11ylab"
        minSdk = 26
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"
    }
}
