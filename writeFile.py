import csv
with open('C:\\Users\\ZL-52S8FFG\\Desktop\\6位手机验证码.txt','a+',encoding='utf8') as f:
    for i in range(1000000):
        if i<10:
            i = '00000'+str(i)
        elif 10<=i and i<100:
            i ='0000'+str(i)
        elif 100<=i and i<1000:
            i ='000'+str(i)
        elif 1000<=i and i<10000:
            i ='00'+str(i)
        elif 10000<=i and i<100000:
            i ='0'+str(i)
        else:
            i=str(i)
        f.write(i + "\n")
