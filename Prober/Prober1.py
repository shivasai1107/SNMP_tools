import subprocess
import sys
from influxdb import InfluxDBClient
import time

client= InfluxDBClient('localhost',8086,'admin','somethingnew','ANM3')
samp=raw_input("enter the sampling interval:")
com=raw_input("enter the community string:")
ip=raw_input("enter the ip:")
id=raw_input("enter the oid:")
z=subprocess.Popen(['python','-u','123.py'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
z.stdin.write(samp+"\n")
z.stdin.write(com+"\n")
z.stdin.write(ip+"\n")
z.stdin.write(id+"\n")
z.stdin.flush()
z.stdin.close()
while True:
	out=z.stdout.readline()
	if len(out)==0:
		break
	gg=out.split(" ")
	if(gg[0]!="enter"):
		rate=gg[0]
		oid=(gg[1]).rstrip()

		print rate
		print oid
		json_body = [
        		{
            		"measurement": "Rates",
            		"tags": {
                		"oid":oid,
               			},
				
            			"fields": {
                			"Counter_Rate":rate
            			}
        		}
    			]
		client.write_points(json_body)	
	#x=sys.stdout(out)
	#if x != None:
	#	gg=str(x.split(" "))
		#print gg[0]
	#gg=x.split(" ")
	#print gg[0]
#	(out is None) or 

