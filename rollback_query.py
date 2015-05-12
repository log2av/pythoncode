a = []
for x in range(764, 789):
    a.append('000000083' + str(x))
print 'delete from CRESTELSMPRD501.TBLMRULELOOKUPDATA where LOOKUPDATAID in'
print a