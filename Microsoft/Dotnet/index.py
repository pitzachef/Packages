import os
import subprocess
import urllib.request
import winreg
import tempfile

def is_dotnet48_installed():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full")
        release, _ = winreg.QueryValueEx(key, "Release")
        winreg.CloseKey(key)
        return release >= 528040  # .NET Framework 4.8
    except Exception:
        return False

def download_dotnet48_installer(dest_path):
    url = "https://go.microsoft.com/fwlink/?linkid=2088631"  # Official offline installer
    print("Downloading .NET Framework 4.8 installer...")
    urllib.request.urlretrieve(url, dest_path)

def install_dotnet48(installer_path):
    print("Installing .NET Framework 4.8...")
    subprocess.run([installer_path, "/quiet", "/norestart"], check=True)

def main():
    if is_dotnet48_installed():
        print(".NET Framework 4.8 is already installed.")
        return

    temp_dir = tempfile.gettempdir()
    installer_path = os.path.join(temp_dir, "ndp48-installer.exe")

    download_dotnet48_installer(installer_path)
    install_dotnet48(installer_path)

    if is_dotnet48_installed():
        print(".NET Framework 4.8 installed successfully.")
    else:
        print("Installation failed.")

if __name__ == "__main__":
    main()
