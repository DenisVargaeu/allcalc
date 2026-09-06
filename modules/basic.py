import os
import sys

def test(number):
    print(number)
def restart_app():
    os.execl(sys.executable, sys.executable, *sys.argv)