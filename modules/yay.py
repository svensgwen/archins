import os
from loguru import logger

def install_yay():
    if os.system("command -v yay > /dev/null 2>&1") != 0:
        logger.warning("Yay not found. Installing yay...")
        os.system("sudo pacman -S --needed --noconfirm base-devel git")
        os.system("git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si --noconfirm")
        os.system("rm -rf yay")
    else:
        logger.success("Yay is already installed.")