# [Setting Up a Development Laptop for FLL](../README.md)

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
    * Click "No Thanks" in the "Welcome to GNOME" dialog.
    * Open a terminal and execute `sudo dnf -y update --refresh` and enter "maker" when it prompts for a password.
    * When the update is complete restart the computer with the following command `sudo shutdown -r now`.

1. Enable auto login for Linux.

    * Click the windows button and type "users" and press enter.
    * Click the "Unlock" button and enter "maker" for the password.
    * Toggle on the "Automatic Login" button.
    * On the left menu, click on "Privacy".  Unclick the "Automatic Screen Lock" toggle button and change the "Blank Screen Delay" to 15 minutes.
    * Close the Settings dialog.

1. Install Google Chrome

    Execute the following commands in a terminal.

    ```bash
    sudo sh -c "dnf install fedora-workstation-repositories && dnf config-manager --set-enabled google-chrome && dnf install -y google-chrome-stable"
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
