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
id_met=''
count=0
curA.execute("SELECT * FROM webPLA.auth_user;")
abon = curA.fetchall()
for i in abon:
    if(i[4]>="120143001" and i[4]<="120143088"):
        account = str(i[0])

        # print(account+' '+name+' '+l_name+' '+s_name+' '+apartaments+' '+meter+' '+house)
        sql = "INSERT INTO webPLA.auth_user_groups(user_id, group_id) VALUES (%s, '1');"
        curA.execute(sql, (account))
        dbAbonent.commit()
        count+=1
print(str(count))
# print(count)
	# if indexIn >=0:
	# 	sql = 'UPDATE abonent.abonent_oplata SET dateOpl=\''+str(indexRep)+'\' WHERE idoplata ='+str(i[0])+';'
	# 	curA.execute(sql)
	# 	dbAbonent.commit()

# UPDATE `abonent`.`abonent_oplata` SET `dateOpl`='20.11.2018' WHERE `idoplata`='14817';
