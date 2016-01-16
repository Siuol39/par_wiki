#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import mkdir, remove, path

class HashFile:
    def __init__(self, name):
        self.name = name
        self.count = self.name + "/count"
        if not path.isdir(name):
            mkdir(name)
            with open(self.count, "w") as f:
                f.write("0")
        else:
            assert path.isfile(self.count)
        return

    def inc_file(self, s, p = 1):
        with open(s, "r") as f:
            n = int(f.readline())
        with open(s, "w") as f:
            f.write(str(n+p))

    def number_elements(self):
        with open(self.count, "r") as f:
            n = int(f.readline())
        return n

    def is_empty(self):
        return self.number_elements == 0

    def contains(self, s):
        assert type(s) == str
        h = hash(s)
        p = self.name + "/" + str(h)
        if not path.exists(p):
            return False
        with open(p, "r") as f:
            t = f.readlines()
            return s + "\n" in t

    def put(self, s):
        assert type(s) == str
        assert not self.contains(s)
        h = hash(s)
        p = self.name + "/" + str(h)
        with open(p, "a") as f:
            f.write(s + "\n")
        self.inc_file(self.count)

    def rem(self, s):
        assert type(s) == str
        assert self.contains(s)
        h = hash(s)
        p = self.name + "/" + str(h)
        with open(p, "r") as f:
            t = f.readlines()
        with open(p, "w") as f:
            for e in t:
                if e != s + "\n":
                    f.write(e)
        self.inc_file(self.count, -1)
