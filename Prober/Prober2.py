import subprocess
import sys
from influxdb import InfluxDBClient
import time

client= InfluxDBClient('localhost',8086,'admin','somethingnew','ANM3')
inp=sys.argv
ip=inp[1]
samp=inp[2]
x=len(inp)
oid=" ".join(inp[3:x])


z=subprocess.Popen(['python','-u','123.py',ip,samp,oid],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
while True:
	out=z.stdout.readline()
	if len(out)==0:
		break
	gg=out.split(" ")
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
