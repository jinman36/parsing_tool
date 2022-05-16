import re

regex = r's[_]port:"[0-9]{5}"|port [0-9]{5}|Port: [0-9]{5}|cat'

with open ('failed_passwd.txt') as infile:
   ports = infile.read()
   results = print(re.findall(regex, ports))