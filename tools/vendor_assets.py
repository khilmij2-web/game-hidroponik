#!/usr/bin/env python3
"""Unduh Tailwind, Font Awesome & Google Font lalu tanam ke assets agar game jalan OFFLINE.
Jalankan sekali (butuh internet):  python3 tools/vendor_assets.py"""
import re, pathlib, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent / "app/src/main/assets/www"
HTML = ROOT / "index.html"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36"}

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()

def save(rel, data):
    p = ROOT / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(data)

html = HTML.read_text(encoding="utf-8")

# 1. Tailwind
save("vendor/tailwind.js", get("https://cdn.tailwindcss.com"))
html = html.replace("https://cdn.tailwindcss.com", "vendor/tailwind.js")

# 2. Font Awesome (css + webfonts)
fa = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/"
css = get(fa + "css/all.min.css").decode()
for f in set(re.findall(r"\.\./webfonts/([\w.\-]+)", css)):
    save("vendor/webfonts/" + f, get(fa + "webfonts/" + f))
save("vendor/fa.css", css.replace("../webfonts/", "webfonts/").encode())
html = html.replace(fa + "css/all.min.css", "vendor/fa.css")

# 3. Google Font Plus Jakarta Sans
gurl = re.search(r'https://fonts\.googleapis\.com/css2[^"\']+', html).group(0).replace("&amp;", "&")
gcss = get(gurl).decode()
for i, u in enumerate(sorted(set(re.findall(r"url\((https://[^)]+)\)", gcss)))):
    name = f"font{i}.woff2"
    save("vendor/fonts/" + name, get(u))
    gcss = gcss.replace(u, "fonts/" + name)
save("vendor/gfont.css", gcss.encode())
html = re.sub(r'https://fonts\.googleapis\.com/css2[^"\']+', "vendor/gfont.css", html)

HTML.write_text(html, encoding="utf-8")
print("Selesai: semua aset sudah lokal (offline-ready).")
