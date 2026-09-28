$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $projectRoot
try {
    uv sync
    if ($LASTEXITCODE -ne 0) {
        throw "uv sync failed with exit code $LASTEXITCODE"
    }

    # Albumentations installs a headless OpenCV wheel. Reinstall the matching
    # desktop wheel last because notebooks under C:\codes use cv2.imshow.
    uv pip install `
        --python ".venv\Scripts\python.exe" `
        --reinstall `
        --no-deps `
        "opencv-python==5.0.0.93"
    if ($LASTEXITCODE -ne 0) {
        throw "OpenCV GUI reinstall failed with exit code $LASTEXITCODE"
    }
}
finally {
    Pop-Location
}
