# Android SDK Setup Script for Windows

$AndroidHome = "$env:USERPROFILE\AppData\Local\Android\Sdk"
$NDKVersion = "25.2.9519653"
$SDKVersion = "33"

Write-Host "Setting up Android SDK and NDK..." -ForegroundColor Green

# Create Android directory
if (-not (Test-Path $AndroidHome)) {
    New-Item -ItemType Directory -Path $AndroidHome -Force | Out-Null
    Write-Host "Created $AndroidHome"
}

# Download Android SDK Command-line Tools
$ToolsUrl = "https://dl.google.com/android/repository/commandlinetools-win-9477386_latest.zip"
$ToolsZip = "$env:TEMP\cmdline-tools.zip"

Write-Host "Downloading Android SDK Command-line Tools..."
Invoke-WebRequest -Uri $ToolsUrl -OutFile $ToolsZip

# Extract to cmdline-tools
$CmdlineToolsPath = "$AndroidHome\cmdline-tools\latest"
New-Item -ItemType Directory -Path $CmdlineToolsPath -Force | Out-Null
Expand-Archive -Path $ToolsZip -DestinationPath "$AndroidHome\cmdline-tools" -Force

# Move contents
Move-Item -Path "$AndroidHome\cmdline-tools\cmdline-tools\*" -Destination $CmdlineToolsPath -Force
Remove-Item -Path "$AndroidHome\cmdline-tools\cmdline-tools" -Force

# Set environment variables
[Environment]::SetEnvironmentVariable("ANDROID_SDK_ROOT", $AndroidHome, "User")
[Environment]::SetEnvironmentVariable("ANDROID_HOME", $AndroidHome, "User")
$env:ANDROID_SDK_ROOT = $AndroidHome
$env:ANDROID_HOME = $AndroidHome

Write-Host "ANDROID_SDK_ROOT set to: $AndroidHome" -ForegroundColor Green

# Accept licenses
Write-Host "Accepting Android SDK licenses..."
$sdkmanager = "$CmdlineToolsPath\bin\sdkmanager.bat"

# Create licenses directory
New-Item -ItemType Directory -Path "$AndroidHome\licenses" -Force | Out-Null

# Accept all licenses
@(
    "android-sdk-license",
    "android-sdk-preview-license",
    "google-android-ndk-license",
    "google-play-services-license",
    "mpl2-license"
) | ForEach-Object {
    $licenseFile = "$AndroidHome\licenses\$_"
    if (-not (Test-Path $licenseFile)) {
        "24333f8a63b6825ea9c5514f83c2829b004d1fee" | Out-File -FilePath $licenseFile -Encoding ASCII
    }
}

Write-Host "Licenses accepted" -ForegroundColor Green

# Install SDK packages
Write-Host "Installing Android SDK packages..."
& $sdkmanager --install "platforms;android-$SDKVersion" "build-tools;33.0.0" "ndk;25.2.9519653"

Write-Host "Android SDK setup complete!" -ForegroundColor Green
Write-Host "You may need to restart your terminal for environment variables to take effect."
