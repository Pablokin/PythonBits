#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import androidhelper
import os

def showWebView(content) :
    f = open("webkit.html", "w")
    f.write(content) 
    f.close() 
    droid=androidhelper.Android() 
    droid.webViewShow(str(os.path.abspath(os.getcwd())) +"/webkit.html")