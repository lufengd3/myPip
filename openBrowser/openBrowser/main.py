#!/usr/bin/python
'''
CLI helper
Open url or files with browser in command line
Homepage: https://github.com/keith3/myPip/openBrowser
Author: http://lufeng.me
'''

import sys
import webbrowser
from time import sleep

def main():
    if '-v' in sys.argv:
        print 'openBrowser 0.0.4'
    elif '-h' in sys.argv:
        print "-v show version"
        print "-h helper"
    else:
        target = sys.argv[1]
        webbrowser.open(target)

        sleep(3)
        exit()

if __name__ == '__main__':
    main()
