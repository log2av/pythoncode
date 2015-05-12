with open('delquery.txt', 'w') as f:
    for x in range(83497,83521):
        f.write("DELETE FROM CRESTELSMPRD501.tblmrulelookupdata WHERE LOOKUPDATAID='" + str(x).zfill(12) + "';\n")
		