# Blog-Site
my simple markdown blog website

## Setup
1. install dependencies (tested on Debian 12)
```bash
apt install gunicorn
apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade markdown2 pygments flask gunicorn
deactivate
```

2. setup project structure
```bash
mkdir Blog-Site
mkdir Blog-Site/posts
mkdir Blog-Site/static
mkdir Blog-Site/templates
```
```
Blog-Site/
├── app.py
├── posts/
│   ├── first-post.md
│   └── another-post.md
├── templates/
│   ├── base.html
│   ├── index.html
│   └── post.html
└── static/
    └── images.png
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
Environment="PATH=/opt/Blog-Site/venv/bin"
ExecStart=/opt/Blog-Site/venv/bin/gunicorn -b 0.0.0.0:9004 -w 1 app:app
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

4. setup Cloudflare reverse proxy
- buy a domain name
- create a cloudflare tunnel, set cloudflare as DNS provider (TODO how to)
- go to cloudflare > networks > connectors, select your tunnel > edit
- go to Published application routes > add a published application route
`blog.your.domain -> http://localhost:9004`
