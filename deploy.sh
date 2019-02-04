#!/bin/sh
scp -r . pi:~/hardware-software-codesign/
ssh pi -t 'python ~/hardware-software-codesign/src/main.py'
