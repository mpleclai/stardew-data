import shutil
import subprocess
import sys
import requests
import zipfile
import os

XNB_HACK_VERSION = "1.1.0"
# NEW_XNB_HACK = MACOS_DEFAULT_PATH+"StardewXnbHack"

def main():

    unpacked_dir = f"{get_game_install_dir()}/Content (unpacked)"
    if os.path.exists(unpacked_dir):
        print("Content is already unpacked! Do you want to continue? (Y/n)")
        yn_input = input()
        if yn_input.lower() != "y":
            print("Exiting...")
            exit()

    # Find current platform
    if sys.platform.startswith("darwin"):
        platform_string = "macOS"
    elif sys.platform.startswith("linux"):
        platform_string = "Linux"
    else:
        raise Exception(f"Unsupported platform: {sys.platform}")
    
    # Download latest version of StardewXnbHack for current platform
    print(f"Downloading StardewXnbHack for {platform_string}...")
    response = requests.get(f"https://github.com/Pathoschild/StardewXnbHack/releases/download/{XNB_HACK_VERSION}/StardewXnbHack-{XNB_HACK_VERSION}-for-{platform_string}.zip")
    if response.status_code != 200:
        raise Exception(f"Failed to download StardewXnbHack. Response code: {response.status_code}")

    # Save downloaded zip to temporary directory
    if os.path.exists("./tmp"):
        print("Removing old ./tmp directory...")
        shutil.rmtree("./tmp")
        
    print("Creating ./tmp directory...")
    os.mkdir("./tmp")

    with open("./tmp/xnb_hack.zip", "w+b") as xnb_hack:
        print("Writing downloaded zip to ./tmp/xnb_hack.zip ...")
        xnb_hack.write(response.content)

    # Unzip StardewXnbHack
    with open("./tmp/xnb_hack.zip", "rb") as zip_file:
        with zipfile.ZipFile(zip_file, "r") as zip:
            print("Unzipping ./tmp/xnb_hack.zip to ./tmp/xnb_hack/ ...")
            zip.extractall("./tmp/xnb_hack")

    # Move binary to game install directory
    downloaded_binary_path = f"./tmp/xnb_hack/StardewXnbHack {XNB_HACK_VERSION} for {platform_string}/StardewXnbHack"
    installed_binary_path = f"{get_game_install_dir()}/StardewXnbHack"

    try:
        if os.path.exists(installed_binary_path):
            print("Removing old StardewXnbHack...")
            os.remove(installed_binary_path)

        print(f"Moving {downloaded_binary_path} to {installed_binary_path} ...")
        shutil.move(downloaded_binary_path, installed_binary_path)
        os.chmod(installed_binary_path, 0o755) # chmod +x
    except Exception as e:
        raise Exception(f"Failed to move StardewXnbHack. Error: {e}")
    

    # Run StardewXnbHack
    print("Running StardewXnbHack...")
    code = subprocess.call(installed_binary_path, cwd="./tmp")
    if code != 0:
        raise Exception(f"Failed to run StardewXnbHack. Exit code: {code}")
    
    # General cleanup
    print("Removing ./tmp directory...")
    shutil.rmtree("./tmp")

    # Translate resources into readable format -- Parsing Script
    print("[TODO] Translating resources...")
    # TODO: Implement

    # Deposit output into iOS + Android Projects
    print("[TODO] Depositing output into iOS + Android Projects...")
    # TODO: Implement

def get_game_install_dir():
    GAME_INSTALL_DIR_MACOS="~/Library/Application Support/Steam/steamapps/common/Stardew Valley/Contents/MacOS"
    GAME_INSTALL_DIR_LINUX="~/.steam/steam/steamapps/common/Stardew Valley"

    if sys.platform.startswith("darwin"):
        return os.path.expanduser(GAME_INSTALL_DIR_MACOS)
    elif sys.platform.startswith("linux"):
        return os.path.expanduser(GAME_INSTALL_DIR_LINUX)
    else:
        raise Exception(f"Unsupported platform: {sys.platform}")

if __name__ == "__main__":
    main()
