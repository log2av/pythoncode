import os
db = raw_input ( 'Enter the name of the table ')
cmd1 = 'mysql -u root -pabhishek android -e "select (data_length+index_length)/power(1024,2) MB from information_schema.tables where table_schema=\'android\' and table_name=\'' + db + '\' ;"'


cmd2 = 'mysql -u root -pabhishek android -e "create table ' + db +'_COPY like ' +db + '; " '
print cmd2

cmd3 = 'mysql -u root -pabhishek android -e "alter table ' + db + '_COPY disable keys ; " '
print cmd3

cmd4 = 'mysql -u root -pabhishek android -e "insert into '+db + '_COPY select * from ' + db + ' ; " '
print cmd4

cmd5 = 'mysql -u root -pabhishek android -e "alter table ' +db+ '_COPY enable keys; " '
print cmd5

cmd6 = 'mysql -u root -pabhishek android -e "RENAME TABLE ' +db+ ' TO ' +db+'_delete ; " '
print cmd6

cmd7 = 'mysql -u root -pabhishek android -e "RENAME TABLE ' +db +'_COPY TO ' +db+ ' ; " '
print cmd7

print 'The size before optimization'
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)
os.system(cmd4)
os.system(cmd5)
os.system(cmd6)
os.system(cmd7)

print 'The size after optimization'
os.system(cmd1)
