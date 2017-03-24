Fuzzer based on Primal Security's FTP Server fuzzer for the tutorial below:
http://www.primalsecurity.net/0x0-exploit-tutorial-buffer-overflow-vanilla-eip-overwrite-2

This fuzzer is made for fuzzing WinAmp .pls playlist files.
Spews out a bunch of fuzz files starting at a buffer size of 100 A's and goes endlessly.
Can be adapted to any type of file, just need to change the design of the template/code. 