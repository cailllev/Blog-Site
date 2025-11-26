# Mandatory First Post
Finally, I took 1h to create a simple markdown blog website.<br>
*Now there should be no excuses left to not document something.*<br>
Anyhow, this is how you can replicate this if you want:

## Setup
### install dependencies
```bash
apt install gunicorn python3-markdown python3-markdown2
```

### setup project structure
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

### setup service
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

### setup Cloudflare reverse proxy
- buy a domain name
- create a cloudflare tunnel, set cloudflare as DNS provider (TODO how to)
- go to cloudflare > networks > connectors, select your tunnel > edit
- go to Published application routes > add a published application route
```
blog.your.domain -> http://localhost:9004
```

## Disclaimer
The initial structure was <s>surely not</s> built by AI. Ain't noone got time to write HTML and CSS nomore.
