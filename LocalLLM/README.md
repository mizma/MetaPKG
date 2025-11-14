# LocalLLM Meta Package

## Install

1. `yay -Bi .` to generate the Package and install

### Set environments

`sudo systemctl edit ollama` and add the following

~~~ini
[Service]
Environment="OLLAMA_CUDA=1"
Environment="OLLAMA_MAX_LOADED_MODELS=2"
Environment="OLLAMA_HOST=0.0.0.0"
~~~

Then `sudo systemctl restart ollama` to restart the service

### Install Models

Install models using `ollama pull <model-name>`.  Models can be searched in [Ollama](https://ollama.com/search)

## Deploy Open WebUI

1. `cd open-webui`
2. `docker compose up -d`
3. open [local IP at 8080](http://127.0.0.1:8080)

