# MetaPKG

Meta PKGBUILDs for different use-cases to manage multi-package use-cases on Arch.

## Installing

Run `./install-pkgs.sh <DIRNAME>` where DIRNAME is the sub-directory.
This will install the dependencies listed in `<DIRNAME>/PKGBUILD` file.

Some packages also has a separate .install script to install from
other repositories like flatpak and pypi.  These scripts will
need to be ran separately.

