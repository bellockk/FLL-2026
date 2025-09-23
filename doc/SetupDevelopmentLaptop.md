# [Setting Up a Development Laptop for FLL](../README.md)

The following guide presents a method to create a team laptop that supports both coding with scratch or python using the Lega Education software suites, and PyBricks on either Linux or Windows. Many users will be familiar with the Windows environment, but if only cheap donated laptops/computers are available to the team, the Linux install can turn a very old laptop into a very capable development machine for a team.

1. Create Installation Media
    * Follow [this guide to create a Windows 11 Install USB stick](https://support.microsoft.com/en-us/windows/create-installation-media-for-windows-99a58364-8c02-206f-aa6f-40c3b507420d) - referred to as the "pink USB stick" in the following sections.
    * Follow [this guide to create a Fedora install USB stick](https://docs.fedoraproject.org/en-US/quick-docs/creating-and-using-a-live-installation-image/) - referred to as the "blue USB stick" in the following sections.
    
1. Install Windows.

    * Connect the pink USB stick to the laptop.
    ---
    ***Note: It will be helpful to plug in a usb mouse for the following steps as the touchpad will not work until all windows updates have been installed.***

    ---
    * Press the power button, then hit the escape key repeatedly till the boot menu comes up.
    ---
    ***Note: On the first boot after the laptop has been off for a while, you may get an error that the CMOS checksum is invalid.  This seems to happen when the battery gets completely discharged.  You can hit any key to proceed past this screen.***

    ---
    * When the "Startup Menu", which will appear as a blue box with text in it, is visible, press "F9" to go to the "Boot Menu".
    * Using the up/down arrow keys select "USB Hard Drive(UEFI)" and press "Enter".
    * On the "Select language settings" page, click "Next".
    * On the "Select keyboard settings" page, click "Next".
    * Ensure "Install Windows 11" is selected, click the checkbox labeled "I agree everything will be deleted including files, apps, and settings" and click "Next".
    * When asked which partition to install on, delete all partitions, then create a new partition with half the size of the available disk, and select the new partition to intall Windows on.
    * On the page titled "Applicable notices and license terms" click "Accept".
    * On the page titled "Select location to install Windows 11", click the "Load Driver" button.
    * Click the "Browse" button.
    * Open the "ESD-USB (C:)" folder, click to highlight the "HP-IntelRapidStorageTechnologyDriver", and click "OK".
    * Click to highlight the line starting with "Intel RST VMD Managed Controller 09AB" and click "Install".
    * Click on each partition of the new "Disk1" and click the "Delete Partition" button.  When you are done there should only be one entry in the table for "Disk 1" and it should be labeled "Unallocated Space".
    * Click to highlight "Disk 1 Unallocated Space", and then click the "Create Partition" button.
    * In the entry that appears, divide the number by 2 and place the new number in that field.  For example, the entry should default to 976760, delete that and enter 488380 into the entry field and click "Apply".
    * Ensure the line "Disk 1 Partition 3" that has "Primary" listed in the "Type" column is selected, and click "Next".
    * Click the "Install" button.
    * After copying files, a window will popup titled "Is this the right country or region?". Click "Yes".
    * On the next window titled "Is this the right keyboard layout or input method?", click "Yes".
    * On the next window titled "Want to add a second keyboard layout?" click "Skip".
    * On the screen labeled "Let's connect you to a network", do not select a network to connect to.  Instead, hit Shift + F10, click in the terminal that pops up, type "OOBE\BYPASSNRO" and hit the enter button.  The computer will restart.
    * On the screen labeled "Is this the right country or region?" Click "Yes".
    * On the next window titled "Is this the right keyboard layout or input method?", click "Yes".
    * On the next window titled "Want to add a second keyboard layout?" click "Skip".
    * On the screen labeled "Let's connect you to a network", do not select a network to connect to.  Click the blue hyperlink text that says "I don't have internet".
    * On the screen labeled "Who's going to use this device?", enter "fll" and click "Next".
    * On the screen labeled "Create a super memorable password", enter "maker" and click "Next".
    * On the screen labeled "Confirm your password", enter "maker" and click "Next".
    * On the next three screens, pick any security question, type "maker" in the entry field, and press "Next".
    * On the screen labeled "Choose privacy settings for your device", click "Next" until the button text changes to "Accept" and then click "Accept".

1. Update Windows.

    * Connect to the internet.
    ---
    ***Note: You may need to set the date and time to be able to connect to a network.***

    ---
    * Type `win`+`R`, type `control update` and press enter.
    * Click the "Check for updates" button.
    * If requested, reboot the machine to finish installation of updates.
    * Repeat as necessary to install all updates.

1. Auto-login as FLL user.

    * Type `win`+`R`, type `regedit` and press enter.
    * Elevate to admin.
    * Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\PasswordLess\Device`
    * In the right pane, double click `DevicePasswordLessBuildVersion` and change the value to `0`.
    * Close the registry editor.
    * Type `win`+`R`, type `netplwiz` and un-check the box "Users must enter a username and password to use this computer."
    * Click "OK"
    * Enter the password "maker" twice and press "OK".
    * Type `win`+`I`, select "Accounts" and then select "Sign-in options".
    * In the "Additional settings" group, under "If you've been away, when shoiuld Windows require you to sign in again?" select "Never" from the dropdown menu.
    * Type "maker" into the password field and click "OK".
    * Close the Settings dialog.

1. Configure Recyle Bin

    * Right click on the Recycle Bin on the desktop and select "Properties".
    * Click "Don't move files to the Recycle Bin.  Remove files immediately when deleted."

1. Download/Install Git

    <https://git-scm.com/download/win>

1. Install Conda

    Open a `cmd.exe` terminal and execute the following.

    ```bash
    setx HOME "C:\Users\%USERNAME%"
    exit
    ```

    Open a new `cmd.exe` window and execute.

    ```bash
    cd %HOME%
    curl -k -o miniconda.exe https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
    start "" /wait miniconda.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%HOME%\.conda
    del /f miniconda.exe
    .conda\condabin\conda.bat activate
    conda update -y -n base conda
    conda create -y -n fll python git m2-base m2-bash
    exit
    ```

    Open a git bash window, and execute the following.

    ```bash
    ~/.conda/condabin/conda.bat init bash
    printf "conda activate fll\n" >> ~/.bash_profile
    ```

    Close and re-open git bash, and execute the following.

    ```bash
    pip install pybricks
    ```

1. Download/Install VSCode

    <https://code.visualstidio.com/Download>

    Select the User Installer for x64.

1. Download/Install Lego Education Spike Application.

    <https://education.lego.com/en-us/downloads/spike-app/software/>

1. Download/Install EV3 Classroom Application

    <https://education.lego.com/en-us/downloads/mindstorms-ev3/software>

    Select Windows 10 from the dropdown and click "Download Installer".

1. Download/Install LDraw.

    <https://www.ldraw.org/help/getting-started.html>

    * Click on "Windows Instructions", then scroll down to the "All-In_One_Installer (AIOI)", download and install.
    * Make sure to install LDraw and the full offline catalog.

1. Set display to never shut off on power, and to do nothing when the lid is closed.
1. Install Fedora

    * Use the blue USB stick, and boot to the Fedora installer.
    * Select "Install to Hard Drive"
    * For the "What languange would you like to use during the installation process?" make sure "English (United States)" is selected and click "Continue".
    * Click on "Installation Destination", and then click "Done".  This will make all the default selections.
    * Click "Begin Installation", when finished, click "Finish Installaion".
    * Click the top right corner of the screen, press the power button, and select "Power Off" then click the "Power Off" button to confirm.
    * Once the computer is off, remove the thumb drive and power it back on.
    * Once booted select "Start Setup" on the dialog box that appears.
    * Connect to Wifi, and click "Next".
    * Unclick all options on the "Privacy" dialog, and click "Next".
    * Click "Next" on the "Third-Party Repositories" dialog.
    * Click "Skip" on the "Connect Your Online Accounts" dialog.
    * In the "About You" dialog, enter "FLL" in the "Full Name" entry field, and "fll" in the "Username" field.  Ensure the case is correct and click "Next".
    * In the "Set a Password" dialog, enter "maker" twice, and click "Next".
    * Click "Start Using Fedora Linux".
    * Click "Skip" in the "Welcome to Fedora Linux" dialog.
    * Open a terminal and execute `sudo dnf -y update --refresh` and enter "maker" when it prompts for a password.
    * When the update is complete restart the computer with the following command `sudo shutdown -r now`.
    * Add the `fll` user to the dialout group.  This is needed to make usb connections.  `sudo usermod -aG dialout fll`.

1. Enable auto login for Linux.

    * Click the windows button and type "users" and press enter.
    * Click the "Unlock" button and enter "maker" for the password.
    * Toggle on the "Automatic Login" button.
    * On the left menu, click on "Privacy".  Unclick the "Automatic Screen Lock" toggle button and change the "Blank Screen Delay" to 15 minutes.
    * Close the Settings dialog.

1. Install Google Chrome

    Execute the following commands in a terminal.

    ```bash
    sudo sh -c "dnf config-manager setopt google-chrome.enabled=1 && dnf install -y google-chrome-stable"
    ```

1. Install needed dependencies.

    Execute the following commands to install conda and create an environment for development.

    ```bash
    sudo dnf -y install zsh vim dfu-util
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh -b -p ~/.conda
    rm -fr miniconda.sh
    source ~/.conda/bin/activate
    conda init bash
    conda config --system --set auto_activate_base false
    conda create -y -n fll
    conda activate fll
    conda env update --file requirements.yaml
    ```

1. Install `udev` Rules.

    On Linux, `udev` rules are required to allow access to the hub through USB.  Execute the following to install the needed rules.

    ```bash
    pybricksdev udev | sudo tee /etc/udev/rules.d/99-pybricksdev.rules
    ```

1. Install VSCode.

    Execute the following command in a terminal.

    ```bash
    sudo sh -c 'rpm --import https://packages.microsoft.com/keys/microsoft.asc && echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo && dnf -y install code'
    ```
