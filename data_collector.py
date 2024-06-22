import shutil
import subprocess
import requests
import zipfile
import os

MACOS_DEFAULT_PATH="/Users/madelineleclair/Library/Application Support/Steam/steamapps/common/Stardew Valley/Contents/MacOS/"
BINARY_EXTRACT_DIRECTORY="./xnb_hack"
STARDEW_XNB_HACK="https://github.com/Pathoschild/StardewXnbHack/releases/download/1.1.0/StardewXnbHack-1.1.0-for-macOS.zip"
XNB_HACK_ZIP="xnb_hack.zip"
XNB_HACK_BINARY="xnb_hack/StardewXnbHack 1.1.0 for macOS/StardewXnbHack"
NEW_XNB_HACK=MACOS_DEFAULT_PATH+"StardewXnbHack"

def main():
    # Download latest version of StardewXnbHack
    response = requests.get(STARDEW_XNB_HACK)
    with open(XNB_HACK_ZIP, "xb") as xnb_hack:
        xnb_hack.write(response.content)
    
    os.makedirs(BINARY_EXTRACT_DIRECTORY, exist_ok=True)

    # Unzip StardewXnbHack
    with open(XNB_HACK_ZIP, "rb") as zip_file:
        with zipfile.ZipFile(zip_file, "r") as zip:
            zip.extractall(BINARY_EXTRACT_DIRECTORY)

    # Move binary to game install directory     
    shutil.move(XNB_HACK_BINARY, NEW_XNB_HACK)

    # Run StardewXnbHack
    os.chmod(NEW_XNB_HACK, 755)
    subprocess.call(NEW_XNB_HACK)

    # Translate resources into readable format -- Parsing Script

    # Deposit output into iOS + Android Projects

if __name__ == "__main__":
    main()