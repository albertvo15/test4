

import os,sys
import subprocess
import re
import time
import datetime

grepstr = 'BCX98321'
path = '/var/data/bdi/'
dirs = os.listdir(path)


for file in dirs:
  filepath = path + file
#  print filepath
  f = open (filepath)
  for line in f:
#    print line
    if 'BCX98321' in line:
#      print 'FOUND str in ' + file
      cmd = 'ls -al ' + filepath + '| cut -d " " -f 5,6,7,9'
      proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True)
      (out,err) = proc.communicate()

      out = out.strip('\n')
      (filesize,m1,m2,m3) = re.split(' ',out)
#      last_mod = str(os.path.getmtime(filepath))

      cmd2 = 'date -r ' + filepath + '| cut -d " " -f 2-7'
      proc = subprocess.Popen(cmd2, stdout=subprocess.PIPE,shell=True)
      (moddate,err) = proc.communicate()
      moddate2 = moddate.strip()
      moddate3 = moddate2.replace('UTC','')
      moddate3 = moddate3.strip()
      (month, day, time, year,other) = re.split(' ',moddate3)
      (hour,min,sec) = re.split(':',time)

#      print 'output ' + out
#      print file + ' - ' +  out
#      print file + ' - ' + filesize + ' - ' + m1 + m2 + m3 
#      print file + ' - ' + filesize + ' - ' + last_mod
#      print file + ' - ' + filesize + ' - ' + moddate3
#      print file + ' - ' + filesize + ' - ' + month + ' ' + day +' '  + other + ' ' + time
      print file + ' - ' + filesize + ' - ' + month + ' ' + day +' '  + other + ' ' + hour + ':' + min



