#! /usr/bin/env python
# coding: utf-8

import pymysql
from collections import deque
import time
import datetime
import csv

dbAbonent = pymysql.connect(host="192.168.0.112", user="root", passwd="02071228", port=3307)
dbMeter = pymysql.connect(host="192.168.0.105", user="root", passwd="root", db="meters", port=3306)
curA = dbAbonent.cursor()
curM = dbMeter.cursor()

id_met=''

now = datetime.date.today()
first = now.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
today = now.strftime("%Y-%m-01")
monthAgo = lastMonth.strftime("%Y-%m")
monthAgo2 = lastMonth.strftime("%m.%Y")

curA.execute("SELECT meter_sn, account_id FROM webPLA.user_private_abonent;")
id_aparato = curA.fetchall()
for i in id_aparato:
	tabToIns = i[0]
	curM.execute("SELECT id, device_type FROM meters.aparatos WHERE id_device like \'"+str(i[0])+"\';")
	id_met=curM.fetchall()
	print(id_met)
	for a in id_met:
		curM.execute("SELECT Wh_t0, Wh_t1, Wh_t2, Wh_t3, fecha, id_aparato FROM meters.indicaciones_mtx1 WHERE id_aparato like \'"+str(a[0])+"\' ORDER BY fecha;")
		kWh=curM.fetchall()
		kWh_int = (kWh[-1][0]+kWh[-1][1]+kWh[-1][2]+kWh[-1][3])/1000
		print('Abonent = '+str(i[1])+', Meter: '+str(i[0])+', id = '+str(a[0])+', date: '+str(kWh[-1][4])+', kWh = '+str(kWh_int))
# 		sql = "INSERT INTO webPLA.user_meterdataprivate(pokazT1, pokazT2, pokazT3, pokazT0, date, account_id) VALUES (0.0, 0.0, 0.0, %s, %s, %s);"
# 		curA.execute(sql, (str(kWh_int), today, str(i[1])))
# dbAbonent.commit()
					# print(b)
	# curM.execute("SELECT Wh_t0 FROM meters.indicaciones_mtx1 where id_aparato like '%s' ORDER BY id DESC" %(id_aparato))
	# meterData = curM.fetchone()
	# return meterData

# while True :
# 	meterData=inputId()
# 	print(meterData)
