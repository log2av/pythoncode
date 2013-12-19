import os, sys
# First we import the Fabric api
from fabric.api import *
 
# We can then specify host(s) and run the same commands across those systems
env.user = 'c'
env.password = 'xxxxxxxxx'
print "NBR >> on NBR Server ****************************************************************"
def uptime():
	with settings(host_string='192.168.1.1'):
		run("date")
		run("cd /CGFBKUP4/NBRORADATA/ ; ls -lh *DEC2013* | awk '{print $5, $6, $7, $9}'")
	
uptime()

print "*******************************************************************************"

print "EXPORT DETAILS >> on Report Server ****************************************************************"
def uptime():
	with settings(host_string='192,1782,3,3'):
		run("date")
		run("cd /CGFBKUP3/EXPDP_Part_Backup/common ; ls -ltrh *.gz | awk '{print $5, $9}'")
	
uptime()
print "*******************************************************************************"

print "CGF PARTITION >> on DB2 ****************************************************************"
env.user = 'root'
env.password = 'xxxxxxxxxxxx'
def uptime():
	with settings(host_string='IP'):
		run("date")
		run("cd /ORADATA2/CRESTELDATA ; ls -ltrh | awk '{print $5, $9}'")
		print "CGF MASTER >> on DB2 ****************************************************************"
		run("cd /ORATEMP/CGFMASTER_BKUP/ ; ls -lh *.gz | awk '{print $5, $6, $7, $9}'")
uptime()
print "*******************************************************************************"


#raw_input()