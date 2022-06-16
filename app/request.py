
import urllib.request
import requests
import json
from .models import Blogg

#  stations = json.loads(response.text)
#   stations_by_name = []
#   for station in stations:
#     name = station.get('name')
#     url = station.get('url')
#     favicon = station.get('favicon')
#     votes = station.get('votes')
#     if station:
#       obj = Radio(name=name, url=url, favicon=favicon, votes=votes)
#       stations_by_name.append(obj)
#   return stations_by_name
def get_blog():

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com",
        "X-RapidAPI-Key": "31e9cbe3d8msh574eaee9cfc96afp14b0aejsn2dbf23758e92"
    }

    response = requests.request("GET", url, headers=headers)
    results = json.loads(response.text)
    blogs = results['originator']

    bloglist=[]
    for blog in blogs:
        id = blog.get('id')
        category = blog.get('category')
        text = blog.get('text')
        author = blog.get('author')
        if blog:
            obj = Blogg(id=id,category=category,text=text,author=author)
        bloglist.append(obj)
    # print(blog)
    return bloglist