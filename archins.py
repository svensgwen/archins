import os
import inquirer
from loguru import logger
from colorama import Fore, Style, init

# Custom Modules
from modules.logger import customize_logger
from modules.yay import install_yay

customize_logger()

init(autoreset=True)
logger.success("The program has been launched successfully. Starting the Installer.")
        
def get_installed_packages():
    pacman_list = os.popen("pacman -Qq").read().splitlines()
    return set(pacman_list)

def install_packages(packages):
    if not packages:
        logger.error("No packages selected. Exiting...")
        return
    
    installed_packages = get_installed_packages()
    packages_to_install = [pkg for pkg in packages if pkg not in installed_packages]
    
    if not packages_to_install:
        logger.success("All selected packages are already installed.")
        return
    
    pacman_packages = []
    aur_packages = []
    
    for pkg in packages_to_install:
        if os.system(f"pacman -Si {pkg} > /dev/null 2>&1") == 0:
            pacman_packages.append(pkg)
        else:
            aur_packages.append(pkg)
    
    if pacman_packages:
        logger.info(Fore.CYAN + "Installing official repository packages with pacman...")
        os.system(f"sudo pacman -S --noconfirm {' '.join(pacman_packages)}")
    
    if aur_packages:
        logger.info(Fore.MAGENTA + "Installing AUR packages with yay...")
        os.system(f"yay -S --noconfirm {' '.join(aur_packages)}")

def main():
    install_yay()
    
    default_packages = [
        "vlc", "audacious", "htop", "gwenview", "timeshift", "flatpak", "fastfetch", "kitty",
        "neofetch", "curl"
    ]
    
    if default_packages:
        logger.success(Fore.BLUE + "Installing default packages...")
        install_packages(default_packages)
    
    package_categories = {
        "Development": ["python", "visual-studio-code-bin"],
        "Multimedia": ["gimp", "inkscape", "audacity", "obs-studio"],
        "Productivity": ["libreoffice", "thunderbird"],
        "Browsers": ["google-chrome", "brave-bin", "vivaldi"],
        "Online Media": ["spotify", "discord"],
        "Advanced Users": ["starship","qbittorrent"],
        "Security & Networking": ["openvpn"],
        "Gaming": ["steam"]
    }
    
    category_question = [
        inquirer.Checkbox(
            "categories", 
            message="Select package categories:", 
            choices=list(package_categories.keys())
        )
    ]
    selected_categories = inquirer.prompt(category_question)["categories"]
    
    selected_packages = []
    for category in selected_categories:
        package_question = [
            inquirer.Checkbox(
                "packages", 
                message=f"Select packages from {category}:", 
                choices=package_categories[category]
            )
        ]
        selected = inquirer.prompt(package_question)["packages"]
        selected_packages.extend(selected)
    
    confirm = inquirer.confirm("Confirm installation of selected packages?", default=True)
    if confirm:
        install_packages(selected_packages)
    else:
        logger.error("Installtion Cancelled!")

if __name__ == "__main__":
    main()
