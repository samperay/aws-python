#!/usr/bin/python

import boto3
import os
import paramiko
import sys
import urllib2
import re
import subprocess
from pprint import pprint
from time import sleep
from glob import glob
from os.path import basename, dirname

block_device = urllib2.urlopen("http://169.254.169.254/latest/meta-data/block-device-mapping/ami").read()
root_partition = block_device + '1'

disk_threshold = 80

# Get Current Disk Details 

df = subprocess.Popen(["df", "-hT", root_partition], stdout=subprocess.PIPE)
output = df.communicate()[0]
device, Type, size, used, available, percent, mountpoint = output.split("\n")[1].split()

percent_int = int(percent.split('%')[0]) # 14
size_int = int(re.search(r'\d+', size).group())

if percent_int <= disk_threshold:
    print('disk size is below threshold.. No action.. exiting')
    sys.exit(1)
else:
    print('Disk has to be increased..')
    sys.exit(0)