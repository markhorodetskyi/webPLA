#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import pymysql
import datetime
import time
pymysql.install_as_MySQLdb()


now = datetime.date.today()
first = now.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
today = now.strftime("%Y-%m-01")
monthAgo = lastMonth.strftime("%Y-%m")
monthAgo2 = lastMonth.strftime("%m.%Y")

dbAbonent = pymysql.connect(host="192.168.0.112", user="root", passwd="02071228", port=3307)
curA = dbAbonent.cursor()
id_met=''
count=0
curA.execute("SELECT * FROM webPLA.user_spozhistory ORDER BY date ASC;")
abon = curA.fetchall()
for i in abon:
    # if(str(i[6])!='120143058' and str(i[6])!='120143027' and str(i[6])!='120143079' and str(i[6])!='120143078' and str(i[6])!='120143083' and str(i[6])!='120143046' and str(i[6])!='120142020' and str(i[6])!='120142023' and str(i[6])!='120142077'):
    sql = "INSERT INTO webPLA.user_meterdataprivate(pokazT1, pokazT2, pokazT3, pokazT0, date, account_id) VALUES (0.0, 0.0, 0.0, %s, %s, %s);"
    curA.execute(sql, (i[2], i[1], i[6]))
    dbAbonent.commit()
    if(str(i[1])=='2018-12-01'):
        sql = "INSERT INTO webPLA.user_meterdataprivate(pokazT1, pokazT2, pokazT3, pokazT0, date, account_id) VALUES (0.0, 0.0, 0.0, %s, '2019-01-01', %s);"
        curA.execute(sql, (i[3], i[6]))
        dbAbonent.commit()
