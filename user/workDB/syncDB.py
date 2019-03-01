#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import pymysql
import datetime
import time
from django.contrib.auth.hashers import make_password
pymysql.install_as_MySQLdb()
from collections import deque



 # Создает хэш
dbAbonent = pymysql.connect(host="213.174.22.133", user="root", passwd="02071228", port=3307, charset='utf8')
curA = dbAbonent.cursor()
curA.execute("SELECT * FROM webPLA.user_private_abonent;")
abon = curA.fetchall()
curA.execute("SELECT * FROM abonent.abonent_oplata;")
sal1 = curA.fetchall()
curA.execute("SELECT * FROM webPLA.user_balans;")
sal2 = curA.fetchall()
count3=0
count4=0

for i in abon:
    count=0
    count2=0
    for a in sal1:
        if (str(i[0])==str(a[1])):
            count=count+1
    for b in sal2:
        date = str(b[3])
        if (i[0]==b[4] and date[0:7]!='2019-01'):
            count2=count2+1
    if(count!=count2):
        count3=count3+1
        print(i[0], count, count2, 'false', count3)
    else:
        print(i[0], count, count2, 'ok')


for c in sal1:
    if (str(c[2])=='2018-06-01' and c[4]=='Оплата' and str(c[1]) != '110091088'):
        print(c[1])
        count4=count4+1

print(count3, count4)
    # sql="SELECT * FROM webPLA.user_privelege WHERE id = %s;"
    # curA.execute(sql, (i[9]))
    # limit = curA.fetchall()
    # print(limit)

    # sql="SELECT number, street_id FROM webPLA.user_house WHERE number = %s;"
    # curA.execute(sql, (i[8]))
    # house = curA.fetchall()
    # for a in house:
    #     h_number = a[0]
    #     street = a[1]
    #     sql="SELECT town_id FROM webPLA.user_street WHERE street_name = %s;"
    #     curA.execute(sql, (a[1]))
    #     town = curA.fetchall()
    #     for b in town:
    #         town_name = b[0]
    #         adress = 'м.'+town_name+' вул.'+street+' '+h_number+' кв '+str(i[4])

    # sql = 'UPDATE webPLA.user_private_abonent SET house_number_id = %s WHERE account_id = %s;'
    # if(int(i[0])>=110091001 and int(i[0])<=110091098):
    #     curA.execute(sql,('9а', i[0]))
    #     dbAbonent.commit()
    # if(int(i[0])>=120142001 and int(i[0])<=120142080):
    #     curA.execute(sql,('14б', i[0]))
    #     dbAbonent.commit()
    # if(int(i[0])>=120143001 and int(i[0])<=120143088):
    #     curA.execute(sql,('14в', i[0]))
    #     dbAbonent.commit()

# print(count)
	# if indexIn >=0:
	# 	sql = 'UPDATE abonent.abonent_oplata SET dateOpl=\''+str(indexRep)+'\' WHERE idoplata ='+str(i[0])+';'
	# 	curA.execute(sql)
	# 	dbAbonent.commit()

# UPDATE `abonent`.`abonent_oplata` SET `dateOpl`='20.11.2018' WHERE `idoplata`='14817';
