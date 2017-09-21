import threading
import subprocess
import time

class IntervalRunner(threading.Thread):
    def __init__(self, seconds):
        self.seconds = seconds
        self.oid=raw_input("enter the oid:")
	self.k=self.oid.split(" ")
	self.ki=[[] for u in range(len(self.k))]
	self.g=[]
	self.i=0
	self.cm="snmpget -v2c -c public localhost"+" "+self.oid
	threading.Thread.__init__(self)

    def run(self):
        while True:
	    #print self.cm
            p = subprocess.Popen(self.cm, shell=True,
                                 stdout=subprocess.PIPE)

            std=p.stdout.readlines()
            x=len(std)
	    g=[]
	    for i in range(x):
	        k= std[i].rsplit(None,1)[-1]
		g.append(k)
		#print g
            l=len(g)
	    #self.ki=[[] for u in range(l)]
	    for u in range(l):
			self.ki[u].append(g[u])
			#print self.ki
	    lo=len(self.ki[0])
	    for u in range(l):
			if(lo>1):
				rate=int(self.ki[u][lo-1])-int(self.ki[u][lo-2])
				print rate
	    time.sleep(self.seconds)
	    
sample=raw_input("enter the sampling interval:")
s=float(sample)
runner = IntervalRunner(s)
runner.start()
runner.join()

