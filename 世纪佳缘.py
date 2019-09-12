import requests
import json
import time
import pandas as pd
import re
 
def fetchURL(url):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：
        url ：目标网页的 url
    返回：目标网页的 html 内容
    '''
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Cookie':'accessID=2019090915162576633; PHPSESSID=cd6fcded5f04ae07a9a507b74ab4c345; save_jy_login_name=17577286344; myuid=221776759; SESSION_HASH=671c65c29cce6e31eaf80e5161f3ac8462f6c29f; user_access=1; pop_time=1568191503868; stadate1=221776759; myloc=32%7C3201; myage=20; PROFILE=222776759%3Alinger_%3Am%3Ahttps%3A%2F%2Fat1.jyimg.com%2F4c%2F06%2F4daq183236c87780e00860b4f90d%3A1%3A%3A1%3A4dad18323_1_avatar_p.jpg%3A1%3A1%3A50%3A10%3A3.0; mysex=m; myincome=30; RAW_HASH=gAMYvNrqAEvGejjRapUb0r5p1p2Wre4L0RRfNK3BkML8c8A8TFDqMH73lRwoFXiBZvz00SJRQdjB%2AMU23-WuiVPqY7dywhsCbG3UzzQw5Cos-JM.; COMMON_HASH=4c4dad183236c87780e00860b4f90d06; sl_jumper=%26cou%3D17%26omsg%3D0%26dia%3D0%26lst%3D2019-09-10; last_login_time=1568191534; user_attr=000000'
        #'Cookie': 'guider_quick_search=on; SESSION_HASH=f09e081981a0b33c26d705c2f3f82e8f495a7b56; PHPSESSID=e29e59d3eacad9c6d809b9536181b5b4; is_searchv2=1; save_jy_login_name=18511431317; _gscu_1380850711=416803627ubhq917; stadate1=183524746; myloc=11%7C1101; myage=23; mysex=m; myuid=183524746; myincome=30; COMMON_HASH=4eb61151a289c408a92ea8f4c6fabea6; sl_jumper=%26cou%3D17%26omsg%3D0%26dia%3D0%26lst%3D2018-11-07; last_login_time=1541680402; upt=4mGnV9e6yqDoj%2AYFb0HCpSHd%2AYI3QGoganAnz59E44s4XkzQZ%2AWDMsf5rroYqRjaqWTemZZim0CfY82DFak-; user_attr=000000; main_search:184524746=%7C%7C%7C00; user_access=1; PROFILE=184524746%3ASmartHe%3Am%3Aimages1.jyimg.com%2Fw4%2Fglobal%2Fi%3A0%3A%3A1%3Azwzp_m.jpg%3A1%3A1%3A50%3A10; pop_avatar=1; RAW_HASH=n%2AazUTWUS0GYo8ZctR5CKRgVKDnhyNymEBbT2OXyl07tRdZ9PAsEOtWx3s8I5YIF5MWb0z30oe-qBeUo6svsjhlzdf-n8coBNKnSzhxLugttBIs.; pop_time=1541680493356'
    }
 
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        #r.encoding = 'unicode_escape'
        print(r.url)
        return r.text
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")
 
def parserHtml(html):
    '''
    功能：根据参数 html 给定的内存型 HTML 文件，尝试解析其结构，获取所需内容
    参数：
            html：类似文件的内存 HTML 文本对象
    '''
    
    s = json.loads(html)
    
    usrinfo = []
    
    for key in s['userInfo']:
             
        blist = []
 
        uid = key['uid']
        realUid = key['realUid']
        nickname = key['nickname']
        sex = key['sex']
        age = key['age']
        work_location = key['work_location']
        height = key['height']
        education = key['education']
        
        matchCondition = key['matchCondition']
        marriage = key['marriage']
        income = key['income']
        shortnote = key['shortnote']
        image = key['image']
 
        blist.append(uid)
        blist.append(realUid)
        blist.append(nickname)
        blist.append(sex)
        blist.append(age)
        blist.append(work_location)
        blist.append(height)
        blist.append(education)
        blist.append(matchCondition)
        blist.append(marriage)
        blist.append(income)
        blist.append(shortnote)
        blist.append(image)
        
        usrinfo.append(blist)
        print(nickname,age,work_location)
 
    writePage(usrinfo)
    print('---' * 20)
 
 
def writePage(urating):
    '''
        Function : To write the content of html into a local file
        html : The response content
        filename : the local filename to be used stored the response
    '''
 
    import pandas as pd
    dataframe = pd.DataFrame(urating)
    dataframe.to_csv('Jiayuan_UserInfo.csv', mode='a', index=False, sep=',', header=False)
 
def removesame(inputfile,outputfile='outputfile'):
    '''
        function:去除文件中的重复行
        inputfile:需要去除重复行的文件名
        outputfile:输出文件名
    '''
    df = pd.read_csv(inputfile,encoding='utf-8',names=['uid','realUid','nickname','sex','age','work_location','height','education','matchCondition','marriage','income','shortnote','image'])
    datalist = df.drop_duplicates()
    datalist.to_csv(outputfile,encoding='utf-8',index=False, header=False)
    print("Done!")

def savepics(inputfile):
    # 读取csv文件
    userData = pd.read_csv(inputfile,names=['uid','realUid','nickname','sex','age','work_location','height','education','matchCondition','marriage','income','shortnote','image'])
    for line in range(len(userData)):
        url = userData['image'][line]
        img = requests.get(url).content
        nickname = re.sub("[\s+\.\!\/_,$%^*(+\"\'?|]+|[+——！，。？、~@#￥%……&*（）▌]+", "",userData['nickname'][line])
    
        filename = str(line) + '-' + nickname + '-' + str(userData['height'][line]) + '-' + str(userData['age'][line]) + '.jpg'
        try:
            with open("C:\\Users\\hiikjh\\Desktop\\images_output1\\" + filename, 'wb') as f:
                f.write(img)

        except:
            print(filename)
    print("Finished!")

def getuidhash(html):
    restr = r'(.*)uid_hash=(.*?) .*"'
    try:
        searchObj = re.search(restr,html)
        #print("group()",searchObj.group())
        #print("group(1)",searchObj.group(1))
        #print("group(2)",searchObj.group(2))
        uid_hash = searchObj.group(2).split('&',2)[0]
        #print(uid_hash)
        return uid_hash
    except:
        print('getuidhash error!')

    
def savebigpics(inputfile):
    '''
    功能：存取大图片
    '''
    #读取csv文件
    userData = pd.read_csv(inputfile,names=['uid','realUid','nickname','sex','age','work_location','height','education','matchCondition','marriage','income','shortnote','image'])
    maxline = len(userData)
    for line in range(10,maxline):
        if userData['realUid'][line]:
            realUid = str(userData['realUid'][line])
        else:
            print("there is no realUid")
            pass
        
        url = 'http://www.jiayuan.com/%s' % realUid
        html = fetchURL(url)
        uid_hash = getuidhash(html)
        if not uid_hash:
            print("uid_hash is null!")
            pass
        url_bigpic='http://photo.jiayuan.com/showphoto.php?uid_hash=%s&p=1'% str(uid_hash)
        print(url_bigpic)
        html = fetchURL(url_bigpic)
        re_str = r'(.*)<img style="max-width:675px;" src="(.*?.*)" '
        reObj = re.findall(re_str, html)

        nickname = re.sub("[\s+\.\!\/_,$%^*(+\"\'?|]+|[+——！，。？、~@#￥%……&*（）▌]+", "",userData['nickname'][line])  
        
        
        for i in range(len(reObj)):
            print(reObj[i][1])
            img = requests.get(reObj[i][1]).content
            filename = str(line) + '-' + nickname + '-' + str(userData['height'][line]) + '-' + str(userData['age'][line]) + '-' +  str(i) +'.jpg'
            try:
                with open("C:\\Users\\hiikjh\\Desktop\\images_output1\\" + filename, 'wb') as f:
                    f.write(img)
            except:
                print(filename)
        time.sleep(5)
    #print(html)

if __name__ == '__main__':
    maxpage = 5916
    textpage = 1
    for page in range(1, textpage):
        url = 'http://search.jiayuan.com/v2/search_v2.php?key=&sex=f&stc=2:18.24,3:155.170,23:1&sn=default&sv=1&p=%s&f=select' % str(page)
        html = fetchURL(url)
        #print(html)
        parserHtml(html)
 
        # 为了降低被封ip的风险，每爬100页便歇5秒。
        if page%100==99:
            time.sleep(5)
    removesame('Jiayuan_UserInfo.csv','Jiayuan_UserInfo_output.csv')
    #savepics('Jiayuan_UserInfo_output.csv')
    savebigpics('Jiayuan_UserInfo_output.csv')
