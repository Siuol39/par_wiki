#!/usr/bin/python3
# -*- coding: utf-8 -*-

from file_queue import FileQueue
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

def color_ram(page, colored):
    """colored : list of pages"""
    colored.append(page)
    return

def visit(page):
    color(page)
    return list_links(page)

def main(f = save_file, init = None):
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
