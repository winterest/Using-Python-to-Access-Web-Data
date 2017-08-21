# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 22:21:44 2017

@author: lxyxi
"""

import urllib

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
