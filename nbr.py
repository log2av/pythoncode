for x in range(1, 32):
    print "ALTER TABLE CRESTELMEDIATIONPRD501.TBLMEDIATIONCDR DROP PARTITION PSNBRCDR_" + str(x).zfill(2) + "MAR2014 UPDATE GLOBAL INDEXES;"
    print "DROP TABLESPACE TSNBRCDR_" + str(x).zfill(2) + "MAR2014 INCLUDING CONTENTS AND DATAFILES;"