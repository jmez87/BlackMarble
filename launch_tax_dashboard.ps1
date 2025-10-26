# BLACK MARBLE Tax Strategy Dashboard Launcher
# PowerShell script for Windows users

# Set console encoding to UTF-8 to handle Unicode characters
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "================================================================" -ForegroundColor Blue
Write-Host "  BLACK MARBLE Tax Strategy Dashboard" -ForegroundColor Cyan
Write-Host "  Maximize Your Tax Savings" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Blue
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[SUCCESS] Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python not found. Please install Python first." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if pip is available
try {
    pip --version | Out-Null
    Write-Host "[SUCCESS] pip is available" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] pip not found. Please ensure pip is installed." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "[INFO] Installing/updating required packages..." -ForegroundColor Yellow

# Install requirements
try {
    pip install -r requirements.txt.txt --quiet
    Write-Host "[SUCCESS] Dependencies installed successfully" -ForegroundColor Green
} catch {
    Write-Host "[WARNING] Some packages may already be installed" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "[INFO] Launching Tax Strategy Dashboard..." -ForegroundColor Cyan
Write-Host "[INFO] The dashboard will open in your default web browser" -ForegroundColor White
Write-Host "[INFO] Use Ctrl+C to stop the server when done" -ForegroundColor White
Write-Host ""

# Launch the Streamlit app
try {
    streamlit run scripts/tax_strategy_dashboard.py --server.headless false --server.port 8501
} catch {
    Write-Host ""
    Write-Host "[ERROR] Error launching dashboard. Please check the error messages above." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "[SUCCESS] Dashboard stopped. Thanks for using BLACK MARBLE Tax Strategy!" -ForegroundColor Green
Read-Host "Press Enter to exit"