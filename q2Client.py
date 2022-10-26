import xmlrpc.client
import sys

s = xmlrpc.client.ServerProxy('http://localhost:8080')
num = sys.argv[1]
magic_num = s.getMagicNumber(int(num))
print(magic_num)
s.kill()