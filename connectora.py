import cx_Oracle

conn_str = u'abhishek/abhishek@10.172.171.66/CGFLUC'
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