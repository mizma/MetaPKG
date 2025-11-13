import os
from pathlib import Path
from invoke import task

TASKS_DIR = Path(__file__).resolve().parent

@task()
def install(c):
    c.run("makepkg -s")
    pattern = "*.pkg.tar.zst"
    files = [p for p in TASKS_DIR.rglob(pattern) if p.is_file()]

    if not files:
        print(f"no *.pkg.tar.gz found in {TASKS_DIR}")
        return

    for f in files:
        command = f"sudo pacman -U {f}"
        c.run(command)

    print("""
`sudo systemctl edit ollama` and add the following

~~~ini
[Service]
Environment="OLLAMA_CUDA=1"
Environment="OLLAMA_MAX_LOADED_MODELS=2"
Environment="OLLAMA_HOST=0.0.0.0"
~~~

Then `sudo systemctl restart ollama` to restart the service
    """)
    pass

@task()
def start(c):
    target_dir = TASKS_DIR / "open-webui"
    os.chdir(target_dir)
    c.run("docker compose up -d")
    pass

@task()
def stop(c):
    target_dir = TASKS_DIR / "open-webui"
    os.chdir(target_dir)
    c.run("docker compose stop")
    pass
