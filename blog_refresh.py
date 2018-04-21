# blog-refresh.py

import requests
from bs4 import BeautifulSoup

url_netflix = "https://medium.com/netflix-techblog"
url_spotify = "https://labs.spotify.com"
url_paypal = "https://www.paypal-engineering.com"
url_github = "https://githubengineering.com"
url_square = "https://medium.com/square-corner-blog"
url_linkedin = "https://engineering.linkedin.com/blog"

def get_today_content():
    req_netflix = requests.get(url_netflix)
    soup = BeautifulSoup(r_netflix.text, "html.parser")
    posts = {}
