# Tax Strategy Dashboard Launcher

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import streamlit
        import pandas
        import numpy
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        return True

def launch_dashboard():
    """Launch the tax strategy dashboard"""
    print("🚀 Launching BLACK MARBLE Tax Strategy Dashboard...")
    print("📊 The dashboard will open in your default web browser")
    print("💡 Use Ctrl+C to stop the server when done")
    
    # Change to the scripts directory
    script_path = os.path.join(os.path.dirname(__file__), "tax_strategy_dashboard.py")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", script_path,
            "--server.headless", "false",
            "--server.port", "8501"
        ])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped. Thanks for using BLACK MARBLE Tax Strategy!")

if __name__ == "__main__":
    print("=" * 60)
    print("🏛️  BLACK MARBLE Tax Strategy Dashboard")
    print("💰 Maximize Your Tax Savings")
    print("=" * 60)
    
    if check_dependencies():
        launch_dashboard()