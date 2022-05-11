#!/bin/env python 

import os
import time

# fork a sub process
pid = os.fork()

if pid == 0 :
    print("This is child pid=%d, getpid=%d, getppid=%d" % (pid,os.getpid(),os.getppid()))
else:
    time.sleep(10)
    print("This is parent pid=%d, getpid=%d, getppid=%d" % (pid,os.getpid(),os.getppid()))
    
