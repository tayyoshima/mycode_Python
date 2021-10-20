import requests
from datetime import datetime

#Request API
response = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-all')
res = response.json()
data = res[0]
print(data)

date_string = data['txn_date']
date_object = datetime.strptime(date_string, "%Y-%m-%d")
x = datetime.date(date_object)
print(x.strftime("%B"))

#print("ข้อมูล ณ วันที่",data['update_date'][8:10],"เดือน",data['update_date'][5:7],"ปี",data['update_date'][0:4],"เวลา",data['update_date'][11:13]+"."+data['update_date'][14:16],"น.")
print("ข้อมูล ณ วันที่",data['update_date'][8:10],x.strftime("%B"),data['update_date'][0:4],"เวลา",data['update_date'][11:13]+"."+data['update_date'][14:16],"น.")
print("ผู้ติดเชื้อใหม่",data['new_case'],"ราย")
print("ผู้ติดเชื้อสะสม",data['total_case'],"ราย")
print("ผู้เสียชีวิตเพิ่ม",data['new_death'],"ราย")
print("ผู้เสียชีวิตสะสม",data['total_death'],"ราย")
print("ผู้หายป่วยเพิ่ม",data['new_recovered'],"ราย")
print("ผู้หายป่วยสะสม",data['total_recovered'],"ราย")


