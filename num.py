#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-  
import time
import os
import commands
import json
import requests
import csv
import ctypes  
import pprint
import ConfigParser
import subprocess 
import shlex
import signal
import simplejson as sjson
import pandas as pd
import numpy as np
import getopt
import datetime
from numpy import NaN
import codecs 
import random

import sys  

ops = ['+', '-', 'x', '/']

if __name__ == '__main__':

    total_num = int(sys.argv[1])

    i = 0
    while i < total_num:
        Anum = random.randint(10,90)
        Bnum = random.randint(4,9)
        op = ops[random.randint(0,99) % 2]
        '''
        if op == '-':
            if (Anum % 10) < Bnum:  # avoid sub in 10-set
                continue
        '''
        if op == '+':
            if (Anum % 10) + Bnum < 10: # get step in 10-set
                continue

        i = i + 1
        print("%d %s %d =      "%(Anum, op, Bnum))

    sys.exit(0)
