# -*- coding: utf-8 -*-

"""test"""

from lxml import etree
from bs4 import BeautifulSoup
import requests
import json
# from selenium import webdriver
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from time import ctime, sleep
import datetime
import threading
import re
from atexit import register
from urllib.request import urlopen as uopen
from urllib.parse import quote
import smtplib
import sys
import os
from fontTools.ttLib import TTFont


# fromaddr=input('from:')
# toaddr=input('to:').split(',')
# print('enter message,end with ^D')
#
# msg=''
# while 1:
#     line=sys.stdin.readlines()
#     if not line:
#         break
#     msg=msg+line
#
# server=smtplib.SMTP('localhost')
# server.sendmail(from_addr=fromaddr,to_addrs=toaddr,msg=msg)
# server.quit()

# def mean(sorted_list):
#     if not sorted_list:
#         return ([],[])
#     big=sorted_list[-1]
#     small=sorted_list[-2]
#
#     big_list,small_list=mean(sorted_list[:-2])
#
#     big_list.append(small)
#     small_list.append(big)
#
#     big_list_sum=sum(big_list)
#     small_list_sum=sum(small_list)
#
#     if big_list_sum>small_list_sum:
#         return ((big_list,small_list))
#     else:
#         return((small_list,big_list))
# test=[1,2,3,4,5,6,7,8]
# print(mean(test))

# def loop0():
#     print('start loop0 at ',ctime())
#     sleep(4)
#     print('loop0 done at ',ctime())
# def loop1():
#     print('start loop1 at ',ctime())
#     sleep(2)
#     print('loop0 done at ',ctime())
# def main():
#     print('starting at ',ctime())
#     # _thread.start_new_thread(loop0(),())
#     # _thread.start_new_thread(loop1(),())
#     # loop0()
#     # loop1()
#     sleep(6)
#     print('all done at ',ctime())
# if __name__=='__main__':
#     main()

font = TTFont("autohome/autohome_1.ttf")
uniList = font['cmap']
# uniList = font['cmap'].tables[0].ttFont.getGlyphOrder()
print(uniList)
