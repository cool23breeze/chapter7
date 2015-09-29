__author__ = 'dmitrijdenisenko'


import os

def run(**args):
    print "[*] In enviroment module."
    return str(os.environ)
