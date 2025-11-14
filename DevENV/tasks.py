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
#   pattern = "*.pkg.tar.zst"
#   files = [p for p in TASKS_DIR.rglob(pattern) if p.is_file()]
#
#   if not files:
#       print(f"no *.pkg.tar.gz found in {TASKS_DIR}")
#       return
#
#   for f in files:
#       command = f"sudo pacman -U {f}"
#       c.run(command)

    print("""
Refer to README.md for setting up environments for eash installed packages
    """)
    pass

@task()
def clean(c):
    """remove package artifacts"""
    run_rm(c, ["src", "pkg", "*.pkg.tar.zst", ".SRCINFO"])
    pass
