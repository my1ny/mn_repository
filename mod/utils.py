import math
import random
from datetime import datetime as dt
import os

def mt_sqrt(x):
    return math.sqrt(x)

def mt_sinpi():
    return math.sin(math.pi / 2)

def mt_elog():
    return math.log(math.e)

def mt_exp(x):
    return math.exp(x)

def mt_pi():
    return math.pi


def rd_int(x, y):
    return random.randint(x, y)

def rd_list(this):
    return random.choice(this)

def rd_rd():
    return random.random()

def rd_nmvar():
    return random.normalvariate(0, 1)


def get_dtnow():
    return dt.now()

def cvt_time2str(objtime):
    return dt.strptime(objtime, "%Y-%m-%d")

def cvt_str2time(strtime):
    obj = dt.now()
    return obj.strftime("%Y-%m-%d")


def get_curdir():
    return os.getcwd()

def os_mkdir(pname):
    return os.mkdir(pname)