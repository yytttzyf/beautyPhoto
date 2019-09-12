import pandas as pd
 
inputfile = "Jiayuan_UserInfo.csv"
outputfile = "Jiayuan_UserInfo_output.csv"
 
df = pd.read_csv(inputfile,encoding='utf-8',names=['uid','nickname','sex','age','work_location','height','education','matchCondition','marriage','income','shortnote','image'])
 
datalist = df.drop_duplicates()
datalist.to_csv(outputfile,encoding='utf-8',index=False, header=False)
print("Done!")
