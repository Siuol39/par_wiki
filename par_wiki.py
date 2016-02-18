#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ram_queue import RAMQueue
from visit_page import list_links
from manage_visited import HashFile

import urllib.error

INIT = "Marie_Dorin-Habert"
FILE = "visited"

def save_hsh(page):
    V = HashFile("visited")
    V.put(page)
    return

def save_file(page):
    with open(FILE, "a") as f:
        f.write(page + "\n")
    return

def color(page, colored):
    """colored : dict of pages
    {hash(a) : [a], hash(b) : [b, b']}

    """
    h = hash(page)
    if h in colored:
        colored[h].append(page)
    else:
        colored[h] = [page]
    return

def is_colored(page, colored):
    """  O(1) !!  """
    h = hash(page)
    return (h in colored) and (page in colored[h])

def main(f = save_file, init = INIT):
    q = RAMQueue() # queuing pages
    c = {} # colored pages
    q.put(init)
    color(init, c)

    stopped = False

    while not q.is_empty() and not stopped:
        try:
            page = q.get()
            f(page)
            print(page)
            t = list_links(page)
            for p in t:
                if not is_colored(p, c):
                    print("    " + p)
                    color(p, c)
                    q.put(p)
        except KeyboardInterrupt:
            stopped = True
        except urllib.error.HTTPError:
            stopped = True
            print(page)
