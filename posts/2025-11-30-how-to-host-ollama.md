# Self Host Ollama + Open-WebUI

## System
* Debian 12
* 16 GB Ram
* 4 GB GPU Ram (GTX 1050)

## Setup
### New User
We do not want to run this with root, create an unpriv user:
```bash
mkdir /opt/llm
useradd -m -d /opt/llm -s /bin/bash llm
echo "export OLLAMA_HOST=http://172.18.0.1:11434" > /opt/llm/.bashrc
su - llm
```

### Firewalls
Allow our WebUI docker container to talk to the ollama (systemd) service.<br>
The following firewall works with a cloudflare ssh tunnel, webservers hosted on 9001-9009, and the above route.<br>
USE AT YOUR OWN RISK, DO NOT ISOLATE YOURSELF FROM YOUR SERVER!
```
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     0    --  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
ACCEPT     6    --  0.0.0.0/0            0.0.0.0/0            tcp dpts:9001:9009
ACCEPT     6    --  0.0.0.0/0            0.0.0.0/0            tcp dpt:22
ACCEPT     6    --  172.16.0.0/12        0.0.0.0/0            tcp dpt:11434
DROP       0    --  0.0.0.0/0            0.0.0.0/0
```

### Open-WebUI
This is the frontend-server for the LLMs. It looks like the ChatGPT website, and will redirect your queries to the backend ollama server. 

```bash
nano /opt/llm/docker-compose.yml
```
```
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    ports:
      - "9003:8080"
    restart: unless-stopped
    environment:
      - OLLAMA_BASE_URL=http://172.18.0.1:11434
    volumes:
      - /opt/llm/open-webui:/app/backend/data
```
```bash
docker compose up -d
```

#### Bonus Content
If you want to automatically shut down the Open-WebUI container when noone is visiting your website (i.e. your not active), see [Open-WebUI Auto Idle](https://github.com/cailllev/OpenWebUI-auto-idle).

### Ollama
This is where the <s>magic</s> linear algebra happens. It takes your funny texts and predicts the next tokens.<br>
The returned tokens will be visible in the Open-WebUI gui.

```bash
apt install nvidia-driver-full # may depend on your GPU and kernel, please consult an LLM what works for you
nano /etc/systemd/system/ollama.service
```
```
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
Environment="OLLAMA_HOST=172.18.0.1:11434"
ExecStart=/usr/local/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

[Install]
WantedBy=default.target
```
```bash
systemctl daemon-reload
systemctl enable blog-site.service
systemctl start blog-site.service
systemctl status blog-site.service
```

## Install a new Model
```bash
su - llm
ollama list
ollama pull deepseek-r1:7b
...
```
![Deepseek-R1](/static/ollama/deepseek-r1.png)
