#!/usr/bin/python3
# -*- coding: utf-8 -*-

#############################################
# Implante un système de file stockées en RAM
#############################################

class RAMQueue:
    def __init__(self):
        self.add = [] # where data is added
        self.ret = [] # where reversed data is got

    def _reverse(self):
        n = len(self.add)
        for k in range(n-1, -1, -1):
            self.ret.append(self.add[k])
        self.add = []

    def __len__(self):
        return len(self.add) + len(self.ret)

    def _add_empty(self):
        return self.add == []

    def _ret_empty(self):
        return self.ret == []

    def is_empty(self):
        return self.__len__() == 0

    def put(self, e):
        self.add.append(e)

    def get(self):
        if self.is_empty():
            raise IndexError
        elif self._ret_empty():
            self._reverse()
        return self.ret.pop()
