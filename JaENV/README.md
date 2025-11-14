# Ja-JP Environment setup Meta Package

Installs IME and JP fonts.

## Install

1. `makepkg -s` to generate the Package
2. `sudo pacman -U ja-jp-essentials-<ver>-any.pkg.tar.zst` to install the listed dependencies.

### Set environments

1. Add `exec-once = fcitx5` to `hyprland.conf`
2. set environment variables in `.profile` or `.zprofile`
  * `export QT_IM_MODULE=fcitx`
  * `export XMODIFIERS=@im=fcitx`
3. Open `fcitx5-configtool` and add Mozc
4. Add `--enable-features=UseOzonePlatform --ozone-platform=wayland --enable-wayland-ime --enable-features=WebRTCPipeWireCapturer`
   to following
  * `~/.config/chrome-flags.conf`, `~/.config/electron-flags.conf` etc.
  * Add this to the `.desktop` files for applications using Electron (Chromium based browsers, Discord, VSCodium etc.)

