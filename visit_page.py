#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To download source code

import urllib.request as u

def url_of_page(page):
    s = "https://fr.wikipedia.org/wiki/"
    return s + page

def up_to(s, i, c):
    """Il faudrait commenter, je ne sais plus ce que ça fait."""
    t = []
    k = i
    while s[k] != c:
        t.append(s[k])
        k += 1
    return "".join(t)

def list_links(page):
    #page = "Temple_d%27Amon_%28Siwa%29"
    url = url_of_page(page)
    source = u.urlopen(url).read().decode("utf-8")
    i = source.find("<body ")
    t = []
    while i != -1:
        i = source.find("<a href=\"/wiki/", i+1)
        t.append(i)
    pages = []
    for i in t:
        s = up_to(source, i+15, "\"")
        if not ":" in s and not "#" in s\
           and not "<" in s and not ">" in s\
           and not "=" in s:
            pages.append(s)
    pages = list(set(pages))
    return pages
