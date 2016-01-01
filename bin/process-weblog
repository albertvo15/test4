
import re

path = '/var/log/web.log'

regex = '([(\w\-\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d*)'
#regex = '([(\w\-\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
#regex = '([(\w\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'

f = open(path)

for line in f:
#  print line
  match =  re.match(regex, line)
  hostname = match.group(1)
  g2 = match.group(2)
  g3 = match.group(3)
  g4 = match.group(4)
  g5 = match.group(5)
  (shortdate,tz) = re.split(' ',g2)
  print hostname + ' - ' + g5 + ' - ' + shortdate

