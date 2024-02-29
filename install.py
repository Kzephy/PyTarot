import subprocess
import sys
import os

def install_dependencies():
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
    if sys.platform.startswith('linux'):
        subprocess.run(["pyinstaller", "PyTarotGUI.py"])
    elif sys.platform.startswith('win'):
        subprocess.run(["pyinstaller", "--onefile", "PyTarotGUI.py"])
    else:
        print("Unsupported platform:", sys.platform)

if __name__ == "__main__":
    install_dependencies()
