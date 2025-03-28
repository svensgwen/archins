#!/bin/bash

# Check if script is running as root
if [[ $EUID -ne 0 ]]; then
   echo "❌ This script must be run as root!"
   exit 1
fi

# Check if system is in UEFI mode
if [[ ! -d "/sys/firmware/efi" ]]; then
    echo "❌ UEFI mode not detected! This script is for EFI systems only."
    exit 1
fi

# Install necessary packages
echo "🔹 Installing GRUB and efibootmgr..."
pacman -S --noconfirm grub efibootmgr

# Identify EFI partition
EFI_PART=$(lsblk -lp | grep "part /boot/efi" | awk '{print $1}')
if [[ -z "$EFI_PART" ]]; then
    echo "❌ EFI partition not found! Make sure /boot/efi is mounted."
    exit 1
fi

# Install GRUB
echo "🔹 Installing GRUB to EFI partition..."
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB

# Generate GRUB config
echo "🔹 Generating GRUB configuration..."
grub-mkconfig -o /boot/grub/grub.cfg

echo "✅ GRUB installation complete! Reboot your system."
