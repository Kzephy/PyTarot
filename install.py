import subprocess
import sys
import os
import shutil

def install_dependencies():
    # Install dependencies from requirements.txt
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

    # Compile code using PyInstaller for the current platform
    if sys.platform.startswith('linux'):
        compile_command = ["pyinstaller", "--onefile", "--dispath=.", "PyTarotGUI.py"]
    elif sys.platform.startswith('win'):
        compile_command = ["pyinstaller", "--onefile", "--distpath=.", "PyTarotGUI.py"]
    else:
        print("Unsupported platform:", sys.platform)
        return
    
    # Run compilation command
    subprocess.run(compile_command)

    # Clean up the build folder
    cleanup_build_folder()

def cleanup_build_folder():
    build_folder = "build"
    spec_file = "PyTarotGUI.spec"
    if os.path.exists(build_folder):
        shutil.rmtree(build_folder)
        print(f"Build folder '{build_folder}' deleted.")
    else:
        print(f"Build folder '{build_folder}' does not exist.")
    
    if os.path.exists(spec_file):
        os.remove(spec_file)
        print(f"Spec file '{spec_file}' deleted.")
    else:
        print(f"Spec file '{spec_file}' does not exist.")

if __name__ == "__main__":
    install_dependencies()
