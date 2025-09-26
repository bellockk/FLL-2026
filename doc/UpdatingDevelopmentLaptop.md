# [Updating Development Laptop](../README.md)

## Windows

Windows is available to allow access to the official Lego Education software suites for programming the robots with scratch and python.

## Windows Updates

Press `Windows + i` and click on the "Windows Update" icon.  Click "Check Now" if it is not already running and allow all updates to install.  Reboot, and repeat until windows update says the computer is up to date.

## Chrome and VSCode

Open Chrome and VSCode, and if an update is available, they will automatically install and ask you to restart the application when the update is complete.

## Lego Education Edition

Download the latest versions and double click them to install.  We usually manually uninstall the previous version and reboot prior to installation to make sure the install is clean.

## Linux

Linux is the preferred operating system for development as it is faster, and will not auto-update during competitions and practice.

### Updating Packages (Chrome, VSCode)

Run the following command periodically to update to the latest system packages.  This will include updates to Google Chrome and VSCode.

```bash
sudo dnf -y update --refresh
```

### Updating Linux Operating System

The development laptop uses the Fedora Operating System for linux.  Every six months the latest version of the operating system is released, and the laptop can be updated in place with the following command:

---

Note: Update the releasever for the operating system before executing the next line.

---

```bash
sudo -c 'dnf -y system-upgrade download --releasever=42 && dnf -y system-upgrade reboot'
```

## Updating Python Packages on Linux and Windows

On both windows and linux, the packages for PyBricks can be updated with the following commands.

---

Note:  It is recommended to only do the following at the beginning of a new season as it can change the way the robot code executes.  An update to `PyBricks` or `PyBricksDev` may necessitate a firmware flash to the robots.

---

```bash
conda activate fll
conda update -y panel
pip install --upgrade pybricks pybricksdev
```
