import os
for x in range(1,31):
    print 'ALTER TABLE CRESTELMEDIATIONPRD501.TBLMEDIATIONCDR DROP PARTITION PSNBRCDR_' + str(x).zfill(2) + 'DEC2012 UPDATE GLOBAL INDEXES;'
    print 'DROP TABLESPACE TSNBRCDR_' + str(x).zfill(2) + 'DEC2012 INCLUDING CONTENTS AND DATAFILES;'
s=raw_input()