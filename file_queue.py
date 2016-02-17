#!/usr/bin/python3
# -*- coding: utf-8 -*-

########################################################
# Implante un système de file stockées dans des fichiers
########################################################

from os import mkdir, remove, path

class FileQueue:
    def _backup_init(self, name):
        with open(name + "_name", "r") as f:
            self.name = f.readline()
        self.add = self.name + "_add"
        self.ret = self.name + "_ret"
        self.cou = self.name + "_cou"
        f = open(self.add, "r")
        f.close()
        f = open(self.ret, "r")
        f.close()
        f = open(self.cou, "r")
        f.close()

    def __init__(self, name):
        assert type(name) == str
        if path.isfile(name + "_name"):
            self._backup_init(name)
            return
        self.name = name
        with open(name + "_name", "w") as f:
            f.write(name)
        for t in [("_add", ""), ("_ret", ""), ("_cou", "0")]:
            f = open(name + t[0], "w")
            f.write(t[1])
            f.close()
        self.add = self.name + "_add"
        self.ret = self.name + "_ret"
        self.cou = self.name + "_cou"

    def _file_is_empty(self, s):
        with open(s, "r") as f:
            return f.readlines() == []

    def _end_of_ret(self):
        with open(self.cou, "r") as f:
            c = int(f.readline())
        with open(self.ret, "r") as f:
            n = len(f.readlines())
        return c >= n

    def _clear_ret(self):
        with open(self.ret, "w") as f:
            f.write("")
        with open(self.cou, "w") as f:
            f.write("0")

    def _clear_file(self, s):
        with open(s, "w") as f:
            f.write("")

    def _return_queue(self):
        with open(self.add, "r") as fa:
            with open(self.ret, "w") as fr:
                for l in fa:
                    fr.write(l)
        self._clear_file(self.add)

    def is_empty(self):
        return self._end_of_ret() and\
            self._file_is_empty(self.add)

    def put(self, s):
        with open(self.add, "a") as f:
            f.write(s)
            f.write("\n")

    def rem(self):
        assert not self.is_empty()
        if self._end_of_ret():
            self._clear_ret()
            self._return_queue()
        with open(self.cou, "r") as f:
            n = int(f.readline())
        with open(self.cou, "w") as f:
            f.write(str(n+1))
        with open(self.ret, "r") as f:
            return f.readlines()[n][:-1]
