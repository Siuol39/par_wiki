#!/usr/bin/python3
# -*- coding: utf-8 -*-

########################################################
# Implante un système de file stockées dans des fichiers
########################################################

class FileQueue:
    def __backup_init__(self, name):
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

    def __init__(self, name, backup=False):
        assert type(name) == str
        if backup:
            self.__backup_init__(name)
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

    def __file_is_empty__(self, s):
        with open(s, "r") as f:
            return f.readlines() == []

    def __end_of_ret__(self):
        with open(self.cou, "r") as f:
            c = int(f.readline())
        with open(self.ret, "r") as f:
            n = len(f.readlines())
        return c >= n

    def __clear_ret__(self):
        with open(self.ret, "w") as f:
            f.write("")
        with open(self.cou, "w") as f:
            f.write("0")

    def __clear_file__(self, s):
        with open(s, "w") as f:
            f.write("")

    def __return_queue__(self):
        with open(self.add, "r") as fa:
            with open(self.ret, "w") as fr:
                for l in fa:
                    fr.write(l)
        self.__clear_file__(self.add)

    def is_empty(self):
        return self.__end_of_ret__() and\
            self.__file_is_empty__(self.add)

    def put(self, s):
        with open(self.add, "a") as f:
            f.write(s)
            f.write("\n")

    def rem(self):
        assert not self.is_empty()
        if self.__end_of_ret__():
            self.__clear_ret__()
            self.__return_queue__()
        with open(self.cou, "r") as f:
            n = int(f.readline())
        with open(self.cou, "w") as f:
            f.write(str(n+1))
        with open(self.ret, "r") as f:
            return f.readlines()[n][:-1]
