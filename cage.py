import numpy as np
import random
import csv
import time

f = open('cagenum.csv')
csv_f = csv.reader(f)
a = []
w = []


for row in csv_f:
	a.extend(row)

word = open('cageword.csv')
csv_w = csv.reader(word)

for row in csv_w:
	w.append(row)


N_word = len(w)
N_num = len(a)
count = 0


while (count < N_word):
	wait_sec = a[random.randrange(1,N_num,1)]
	print type(wait_sec)	
	print type(float(wait_sec))	

	print "Number of Seconds:", wait_sec 
	print "Random Word", w[random.randrange(0,N_word,1)] 
	print raw_input("stuffs")	

	# for i in xrange(wait_sec,0,-1):
	# 	time.sleep(1)
	# 	print i
	# count = count +1