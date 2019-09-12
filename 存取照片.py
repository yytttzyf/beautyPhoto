import requests
import pandas as pd
import re
 
# 读取csv文件
userData = pd.read_csv("Jiayuan_UserInfo_output.csv",names=['uid','nickname','sex','age','work_location','height','education','matchCondition','marriage','income','shortnote','image'])
 
for line in range(len(userData)):
    if line > 3:
        break
    url = userData['image'][line]
    url = 'http://t1.jyimg.com/01/1c/685184a6bfc0d6fb642d57832a1e/152993609d.jpg'

    img = requests.get(url).content
    nickname = re.sub("[\s+\.\!\/_,$%^*(+\"\'?|]+|[+——！，。？、~@#￥%……&*（）▌]+", "",userData['nickname'][line])
    
    filename = str(line) + '-' + nickname + '-' + str(userData['height'][line]) + '-' + str(userData['age'][line]) + '.jpg'
    try:
        with open("C:\\Users\\hiikjh\\Desktop\\images_output1\\" + filename, 'wb') as f:
            f.write(img)
    except:
        print(filename)
 
print("Finished!")

