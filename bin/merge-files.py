

import os
import filecmp
import time
import datetime
import os
import subprocess

patha = '/var/dump/dir-a'
pathb = '/var/dump/dir-b'
mergeddir = '/var/dump/merged'

mydira = set(os.listdir(patha))
mydirb = set(os.listdir(pathb))


######################
dc = filecmp.dircmp(patha, pathb)
#print 'Common:', dc.common
#print 'Left  :', dc.left_only
#print 'Right :', dc.right_only


for doleft in dc.left_only:
  myfilename = doleft
  cmd = 'cp -p ' +  patha + '/' + myfilename + ' ' +  mergeddir
  proc = subprocess.Popen(cmd,shell=True)
  (out,err) = proc.communicate()
  
  
for doright in dc.right_only:
  myfilename = doright
  cmd = 'cp -p ' +  pathb + '/' + myfilename + ' ' +  mergeddir
  proc = subprocess.Popen(cmd,shell=True)
  (out,err) = proc.communicate()


for docommon in dc.common:
  myfilename = docommon

  myfilea = '/var/dump/dir-a/' + myfilename
  file_mod_timea = round(os.stat(myfilea).st_mtime)
  myfileb = '/var/dump/dir-b/' + myfilename
  file_mod_timeb = round(os.stat(myfileb).st_mtime)

  if file_mod_timea > file_mod_timeb:
    cmd = 'cp -p ' +  patha + '/' + myfilename + ' ' +  mergeddir
    proc = subprocess.Popen(cmd,shell=True)
    (out,err) = proc.communicate()
    
  if file_mod_timea < file_mod_timeb:
    cmd = 'cp -p ' +  pathb + '/' + myfilename + ' ' +  mergeddir
    proc = subprocess.Popen(cmd,shell=True)
    (out,err) = proc.communicate()




#myfilename = 'five.txt'
#cmd = 'cp ' +  patha + '/' + myfilename + ' ' +  mergeddir

#proc = subprocess.Popen(cmd,shell=True)
#(out,err) = proc.communicate()
#print "program output:", out

#myfilea = '/var/dump/dir-a/five.txt'
#file_mod_timea = round(os.stat(myfilea).st_mtime)
#myfileb = '/var/dump/dir-b/five.txt'
#file_mod_timeb = round(os.stat(myfileb).st_mtime)

#print file_mod_timea
#print file_mod_timeb

######################


