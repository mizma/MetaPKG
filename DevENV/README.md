# Ja-JP Environment setup Meta Package

Installs IME and JP fonts.

## Install

1. `makepkg -s` to generate the Package
2. `sudo pacman -U ja-jp-essentials-<ver>-any.pkg.tar.zst` to install the listed dependencies.

### Set environments

#### Diff viewer

Global Configuration

~~~
git config --global core.pager delta
git config --global interactive.diffFilter 'delta --color-only'
git config --global delta.navigate true
git config --global merge.conflictStyle zdiff3
~~~

#### tmux

* Color issues
  * certain terminal colors does not adhere to the terminal settings.
  * seems to be able to set to default instead in .tmux.conf

~~~config
set-option -ga terminal-overrides ",xterm-256color:Tc"
set -g default-terminal "screen-256color"
set -g status-bg default
set -g status-fg default
~~~

* mouse wheel doesn't scroll
  * `set -g mouse on`
* fix the indexing maddness.

~~~config
# Start windows and panes at 1 instead of 0
set -g base-index 1
setw -g pane-base-index 1
~~~

* See `./home/.tmux.conf` and `./home/.local/bin/tmux-sessionizer` in
  `mizma/LinuxSetupMemo` for more customizations

#### nvim related

* `git clone git@github.com:mizma/nvimrc.git ~/.config/nvim && nvim`
* `touch ~/.config/nvim/PROTECTED`
  * make sure ML4W doesn't overwrite my nvim configs
* For editing with root privaleges
  * use sudoedit for system files that are not symlinked
  * use `sudo -E nvim` for keeping current ENV and run nvim as root

#### Docker

* `sudo systemctl enable --now docker.service` to start and enable
  the service
* Add the user to the docker group
  * `sudo usermod -aG docker $USER`
  * `newgrp docker` or restart the terminal to take effect

#### fzf related

* Start with [official examples](https://github.com/junegunn/fzf/wiki/Examples#git)
