import re

regex1 = r'port [0-9]{5}'
regex2 = r'Port: [0-9]{5}'
regex3 = r's[_]port:"[0-9]{5}"'

from multiprocessing import Process
import sys

def port1():
  with open ('failed_passwd.txt', 'r') as infile:
    ports = infile.read()
    results = print(re.findall(regex1,ports))
def port2():
  with open ('failed_passwd.txt', 'r') as infile:
    ports = infile.read()
    results = print(re.findall(regex2,ports))
def port3():
  with open ('failed_passwd.txt', 'r') as infile:
    ports = infile.read()
    results = print(re.findall(regex3,ports))

if __name__=='__main__':
  p1 = Process(target = port1)
  p1.start()
  p2 = Process(target = port2)
  p2.start()
  p3 = Process(target = port3)
  p3.start()
