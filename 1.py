#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date

if __name__ == '__main__':

    def a(tag, s):
        def b(s):
            return "<"+tag+">"+s+"</"+tag+">";
        return b(s)
    print(a("html", "Test text"))