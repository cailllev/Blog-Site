from datetime import datetime
from flask import Flask, render_template, abort
from markdown2 import markdown
from os import listdir, path
from pygments.formatters import HtmlFormatter

from zoneinfo import ZoneInfo


app = Flask(__name__)
POST_DIR = "posts"
PYGMENTS_CSS = HtmlFormatter(style="monokai").get_style_defs('.codehilite')
# more styles here: https://dt.iki.fi/pygments-gallery


@app.context_processor
def inject_now():
    now = datetime.now(ZoneInfo("Europe/Zurich")).strftime("%Y-%m-%d %H:%M %Z")
    return {"now": now}

def get_posts():
    files = [f[:-3] for f in listdir(POST_DIR) if f.endswith(".md")]
    files = sorted(files, reverse=True)
    posts_dict = {}
    for p in files:
        if "-" not in p:
            continue # invalid name
        link = p
        year = p.split("-")[0]
        title = " ".join([p.capitalize() for p in (p.split("-")[3:])]) # uppercase everything after 20xx-xx-xx
        if year in posts_dict:
            posts_dict[year].append((title, link))
        else:
            posts_dict[year] = [(title, link)]
    return posts_dict

def load_post(slug):
    filepath = path.join(POST_DIR, f"{slug}.md")
    if not path.isfile(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        md_content = f.read()
    html = markdown(md_content, extras=["fenced-code-blocks", "pygments"])
    return html

@app.route("/")
def index():
    posts = get_posts()
    return render_template("index.html", posts=posts)

@app.route("/post/<slug>")
def post(slug):
    posts = get_posts()  # so sidebar works on all pages
    content = load_post(slug)
    if content is None:
        abort(404)
    return render_template("post.html", content=content, posts=posts, title=slug, pygments_css=PYGMENTS_CSS)

@app.route("/about")
def about():
    posts = get_posts()
    return render_template("about.html", posts=posts, title="About me")

if __name__ == "__main__":
    print("running without wsgi!")
    app.run("0.0.0.0", 9004)
