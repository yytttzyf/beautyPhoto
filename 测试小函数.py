#import pandas as pd
import requests
import json
import time
import re
  
def test1():
    return 
    strs = '''<td align="center">
                  <img style="max-width:675px;" src="http://t4.jyimg.com/31/96/c30ab6ded0ae521a478f09f6abff/167563403d.jpg" alt=""/>
                  <input type="hidden" value="167563403" class="pid" />
                </td>'''
    re_str = r'(.*)<img style="max-width:675px;" src="(.*?.*)" '
    reObj = re.findall(re_str, strs)
    url = reObj[0][1]
    #print(reObj[0])
    print (url)

def test2():
    st = test1()
    if not st:
        print("null")
    else:
        print("not null")


if __name__ == '__main__':
    test2()
