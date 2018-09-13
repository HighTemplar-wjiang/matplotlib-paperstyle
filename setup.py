# Credit: https://stackoverflow.com/a/35854177

# -*- coding: utf-8 -*-
import matplotlib as mpl
import glob
import os.path
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-install', action='store_true', default=True)
parser.add_argument('-upgrade', action='store_true')
options = parser.parse_args()

#~ # ref  ->  matplotlib/style/core
BASE_LIBRARY_PATH = os.path.join(mpl.get_data_path(), 'stylelib')
STYLE_PATH = os.path.join(os.getcwd(),'mplstyles')
STYLE_EXTENSION = 'mplstyle'
style_files = glob.glob(os.path.join(STYLE_PATH,"*.%s"%(STYLE_EXTENSION)))

for _path_file in style_files:
    _, fname = os.path.split(_path_file)
    dest = os.path.join(BASE_LIBRARY_PATH, fname)
    if not os.path.isfile(dest) and options.install:
        shutil.copy(_path_file, dest)
        print("%s style installed"%(fname))
    elif options.upgrade:
        shutil.copy(_path_file, dest)
        print("%s style upgraded"%(fname))
    elif os.path.isfile(dest):
        print("%s style already exists (use -upgrade to upgrade)"%(fname))
    else:
        pass