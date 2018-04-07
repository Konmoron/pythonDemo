#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# FILE NAME: test_time.py
# CREATED AT: 2018/4/6 11:25
# VERSION: v1

__author__ = 'ChaoQiang'

# import time
import datetime
import time

# get now timestamp
now_timestamp = time.time()

# get localtime
now_localtime = time.localtime()

# get format time
format_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# get now datetime
now_datetime = datetime.datetime.now()

# get format time
format_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
format_datetime_timestamp = int(time.mktime(datetime.datetime.now().timetuple()))

# get 1 days ago's date
datetime_1_days_ago = datetime.datetime.now() - datetime.timedelta(days=1)
datetime_1_days_ago_timestamp = int(time.mktime((datetime.datetime.now() - datetime.timedelta(days=1)).timetuple()))

# format 1 days ago's date
format_datetime_1_days_ago = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")

# print time
def print_time(time_need_print):
    print 'Time is ', time_need_print

if __name__ == '__main__':
    print_time(now_timestamp)
    print_time(now_localtime)
    print_time(format_time)
    print_time(now_datetime)
    print_time(format_datetime)
    print_time(format_datetime_timestamp)
    print_time(datetime_1_days_ago)
    print_time(datetime_1_days_ago_timestamp)
    print_time(format_datetime_1_days_ago)