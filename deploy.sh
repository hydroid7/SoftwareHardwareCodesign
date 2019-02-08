#!/bin/sh
scp -r . pi:~/hardware-software-codesign/
ssh pi -t 'python3 ~/hardware-software-codesign/src/main.py'
