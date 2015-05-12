import cx_Oracle

conn_str = u'crestelmediationprd501/crestelmediationprd501@10.171.17.87/CGFLUC'
con = cx_Oracle.connect(conn_str)
#print con.version
c = con.cursor()
c.execute(u'SELECT * FROM tblcircle')
with open('ans.csv', 'w') as text_file:
    text_file.write('CircleName CircleID \n')
    for row in c:
        text_file.write(row[0] + ' ' + row[1] + '\n')
con.close()
#       text_file.write(row[0], "-", row[1])