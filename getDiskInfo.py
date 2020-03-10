from glob import glob
import subprocess
import os
import sys
from os.path import basename, dirname

def physical_drives():
    drive_glob = '/sys/block/*/device'
    return [basename(dirname(d)) for d in glob(drive_glob)]

def partitions(disk):
    if disk.startswith('.') or '/' in disk:
        raise ValueError('Invalid disk name {0}'.format(disk))
    partition_glob = '/sys/block/{0}/*/start'.format(disk)
    return [basename(dirname(p)) for p in glob(partition_glob)]

disk = physical_drives()
disk_part = partitions(disk[0])

conv_str = ' '.join(map(str, disk_part))
main_device = "/dev/" + conv_str

# Fetching mount point from main_device

df = subprocess.Popen(["df", "-hT", main_device], stdout=subprocess.PIPE)
output = df.communicate()[0]
device, Type, size, used, available, percent, mountpoint = output.split("\n")[1].split()

if Type == 'xfs':
  os.system('sudo xfs_growfs -d'+mountpoint)
  print('file system has been extended')
elif Type == 'ext3' or 'ext4':
  print('Need to work on ext file systems')

sys.exit(0)