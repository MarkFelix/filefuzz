#############################################################################################
# Fuzzer based on Primal Security's FTP Server fuzzer.										#
# http://www.primalsecurity.net/0x0-exploit-tutorial-buffer-overflow-vanilla-eip-overwrite-2#
# This fuzzer is made for fuzzing WinAmp .pls playlist files.                               #
# Original winamp 5.12 exploit: https://www.exploit-db.com/exploits/3422/					#
# Spews out a bunch of fuzz files starting at a buffer size of 100 A's and goes endlessly.  #
# Can be adapted to any type of file, just need to change the design of the template.       #
#############################################################################################

import sys
import time
from time import sleep

# File header
start= "[playlist]\r\nFile1=\\\\"

# create string of 100 A's '\x41'
buff = '\x41'*100

# End of file
end="\r\nTitle1=pwnd\r\nLength1=512\r\nNumberOfEntries=1\r\nVersion=2\r\n"
 
# loop through building the buffer with an increasing length by 50 A's
while True:

  try:

    # Get length of Buff to append size to end of each fuzz file
    count = str(len(buff))

    # Open the file to write to
    f = open('file'+count+'.pls', 'w')

    # Write the file
    f.write(start)
    f.write(buff)
    f.write(end)
    f.close

    # Increase the buff string by 50 A's and then the loop continues
    buff = buff + '\x41'*50

    # Sleep is good. Remove and see what happens. I dare you!
    sleep(5)
 
  except: # Crash on error and exit
    print "[+] Crash occured"
    sys.exit()
