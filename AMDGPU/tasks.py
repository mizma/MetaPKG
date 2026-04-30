import glob
from pathlib import Path
from invoke import task

TASKS_DIR = Path(__file__).resolve().parent

##############################################
### Helper Functions
##############################################

def run_rm(c, paths):
    """run rm -rf command equivalent for each pf against paths

    Args:
        c (Obj): invoke context object
        paths (List): List of paths to remove
    """
    files = []
    for f in paths:
        files.extend(glob.glob(f))

    for f in files:
        c.run(f"rm -rf {f}")
    pass

##############################################
### Invoke Task Definitions
##############################################

@task()
def install(c):
    c.run("yay -Bi --noconfirm .")

    print("""
1. Add `exec-once = fcitx5` to `hyprland.conf`
2. set environment variables in `.profile` or `.zprofile`
  * `export QT_IM_MODULE=fcitx`
  * `export XMODIFIERS=@im=fcitx`
3. Open `fcitx5-configtool` and add Mozc
4. Add `--enable-features=UseOzonePlatform --ozone-platform=wayland --enable-wayland-ime --enable-features=WebRTCPipeWireCapturer`
   to following
  * `~/.config/chrome-flags.conf`, `~/.config/electron-flags.conf` etc.
  * Add this to the `.desktop` files for applications using Electron (Chromium based browsers, Discord, VSCodium etc.)
    """)
    pass

@task()
def clean(c):
    """remove package artifacts"""
    run_rm(c, ["src", "pkg", "*.pkg.tar.zst", ".SRCINFO"])
    pass

