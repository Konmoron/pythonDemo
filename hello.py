#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# FILE NAME: hello.py
# CREATED AT: 2018/4/7 14:45
# VERSION: v1

__author__ = 'ChaoQiang'

from datetime import datetime
import os

# get timestamp
now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# get curr dir
# curr_dir = os.getcwd()

# open file and write hello world
def write_mess():
    # defile result file name
    result_file_name = os.path.splitext(__file__)[0] + '_result.txt'
    #print result_file_name

    # write message
    with open(result_file_name, 'a') as result_file:
        result_file.write('hello world!\n \texec time is %s! curr file is %s!\n' % (now_time, __file__))

# print os.path.split(__file__)
# print os.path.splitext(__file__)[0]

if __name__ == '__main__':
    print 'hello world! exec time is %s! curr file is %s' % (now_time, __file__)
    write_mess()