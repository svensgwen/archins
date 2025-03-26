from dataclasses import dataclass, field
from typing import List

@dataclass
class DistributionPackages:
    common: List[str] = field(default_factory=list)

@dataclass
class Packages:
    pacman: DistributionPackages = field(default_factory=DistributionPackages)
    aur: DistributionPackages = field(default_factory=DistributionPackages)

DRIVERS = {
	"intel": Packages(
		pacman=DistributionPackages(
			common=[
				"lib32-mesa", "vulkan-intel", "lib32-vulkan-intel", 
				"vulkan-icd-loader", "lib32-vulkan-icd-loader", "intel-media-driver",
				"libva-intel-driver", "xf86-video-intel"
			]
		)
	),
	"amd": Packages(
		pacman=DistributionPackages(
			common=[
				"lib32-mesa", "vulkan-radeon", "lib32-vulkan-radeon", 
				"vulkan-icd-loader", "lib32-vulkan-icd-loader"
			]
		)
	),
	"nvidia": Packages(
		pacman=DistributionPackages(
			common=[
				"nvidia-dkms", "nvidia-utils", "lib32-nvidia-utils",
				"nvidia-settings", "vulkan-icd-loader", "lib32-vulkan-icd-loader",
				"lib32-opencl-nvidia", "opencl-nvidia", "libxnvctrl"
			]
		)
	)
}