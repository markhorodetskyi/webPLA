import csv
import pymysql

dbAbonent = pymysql.connect(host="192.168.0.112", user="root", passwd="02071228", port=3307)
curA = dbAbonent.cursor()

# curA.execute("SELECT * FROM webPLA.user_street;")
# street = curA.fetchall()
# print(street)
#
# with open('street.csv', 'w') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=';',
#                             lineterminator = '\n', quoting=csv.QUOTE_MINIMAL)
#     filewriter.writerow(['ID', 'NAME'])
#     filewriter.writerow([str(street[0][0]), str(street[0][1])])
#     print([str(street[0][0]), str(street[0][1])])
#     filewriter.writerow([str(street[1][0]), str(street[1][1])])
#     print([str(street[1][0]), str(street[1][1])])

curA.execute("SELECT * FROM webPLA.user_private_abonent;")
id_aparato = curA.fetchall()

with open('export.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=';',
                            lineterminator = '\n', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['PAYERIDENT', 'PIB', 'STREETCODE', 'STREET', 'BUILDING', 'FLAT', 'COMPANY', 'OKPO', 'ACCOUNT', 'MFO', 'SERVICE', 'SERVICECOD', 'LS', 'SUM'])

    for abon in id_aparato:
        sql = "SELECT street_id FROM webPLA.user_house where number = %s;"
        curA.execute(sql, str(abon[8]))
        street = curA.fetchall()
        sql = "SELECT id FROM webPLA.user_street where street_name = %s;"
        curA.execute(sql, str(street[0][0]))
        streetId = curA.fetchall()
        sql = "SELECT sum(saldo) FROM webPLA.user_balans where account_id = %s;"
        curA.execute(sql, str(abon[0]))
        saldo = curA.fetchall()
        if(str(abon[1])!='ТзОВ «Стрийбудмонтаж'):
            print([str(abon[0]), str(abon[3]+" "+abon[1]+" "+abon[2]), str(streetId[0][0]), str(street[0][0]), str(abon[8]), str(abon[4]), 'ДП Гірпроменерго', '41239703', '26009053741970', '325321 ', 'Електропостачання', '1', str(abon[0]), round(saldo[0][0]*(-1), 2)])

            filewriter.writerow([str(abon[0]), str(abon[3]+" "+abon[1]+" "+abon[2]), str(streetId[0][0]), str(street[0][0]), str(abon[8]), str(abon[4]), 'ДП Гірпроменерго', '41239703', '26009053741970', '325321 ', 'Електропостачання', '1', str(abon[0]), round(saldo[0][0]*(-1), 2)])
        else:
            print([str(abon[0]), str(abon[1]), str(streetId[0][0]), str(street[0][0]), str(abon[8]), str(abon[4]), 'ДП Гірпроменерго', '41239703', '26009053741970', '325321 ', 'Електропостачання', '1', str(abon[0]), round(saldo[0][0]*(-1), 2)])

            filewriter.writerow([str(abon[0]), str(abon[1]), str(streetId[0][0]), str(street[0][0]), str(abon[8]), str(abon[4]), 'ДП Гірпроменерго', '41239703', '26009053741970', '325321 ', 'Електропостачання', '1', str(abon[0]), round(saldo[0][0]*(-1), 2)])
