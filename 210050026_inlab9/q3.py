import os
import sys

# Taking ip address of host server from command line
host_address = sys.argv[1]

# pinging the server
# with packets sent limit as 5 packets using -c flag
# and wait time limit of 8 seconds using -w flag
ping_response = os.system("ping -c 5 -w 8 " + host_address + " > /dev/null")

if ping_response != 0:
    print("NO")
else:
    print("YES")