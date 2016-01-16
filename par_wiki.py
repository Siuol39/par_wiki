#!/usr/bin/python3
# -*- coding: utf-8 -*-

from file_queue import FileQueue
from visit_page import list_links
from manage_visited import HashFile

import urllib.error

INIT = "Marie_Dorin-Habert"

def save(page):
    V = HashFile("visited")
    V.put(page)

def main(f = save, init = None):
    q = FileQueue("to_visit")
    c = HashFile("colored")

    if init != None:
        q.put(init)
        c.put(init)

    stopped = False

    while not q.is_empty() and not stopped:
        try:
            page = q.rem()
            f(page)
            print(page)
            t = list_links(page)
            for p in t:
                if not c.contains(p):
                    print("    " + p)
                    c.put(p)
                    q.put(p)
        except KeyboardInterrupt:
            stopped = True
        except urllib.error.HTTPError:
            stopped = True
            print(page)
