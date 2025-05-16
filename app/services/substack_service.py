import requests
from flask import current_app

def get_latest_posts():
    rss_url = current_app.config.get('SUBSTACK_URL')
    if not rss_url:
        return []
    api_url = f"https://api.rss2json.com/v1/api.json?rss_url={rss_url}"
    resp = requests.get(api_url)
    data = resp.json()
    posts = []
    for item in data.get("items", [])[:5]:
        posts.append({
            "title": item["title"],
            "published": item["pubDate"],
            "link": item["link"],
            "thumbnail": item.get("thumbnail"),
            "subtitle": item.get("description", "No Subtitle Provided")
        })
    return posts 