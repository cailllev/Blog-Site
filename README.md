# Blog-Site
my simple markdown blog website

## Setup
1. install dependencies
```bash
apt install gunicorn python3-markdown python3-markdown2
```

2. setup project structure
```bash
mkdir wwwroot
mkdir wwwroot/posts
mkdir wwwroot/templates
```
```
wwwroot/
├── app.py
├── posts/
│   ├── first-post.md
│   └── another-post.md
└── templates/
    ├── base.html
    ├── index.html
    └── post.html
```

3. setup service
```bash
nano /etc/systemd/system/blog-site.service
```
```bash
[Unit]
Description=My Blog-Site

[Service]
Type=simple
User=web
ExecStart=/bin/bash /opt/Blog-Site/start_server.sh
WorkingDirectory=/opt/Blog-Site
Restart=on-failure


[Install]
WantedBy=multi-user.target
```
```bash
systemctl daemon-reload
systemctl enable blog-site.service
systemctl start blog-site.service
systemctl status blog-site.service
```
