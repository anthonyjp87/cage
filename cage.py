import numpy as np, random, csv, time, sys

##to do: limit # of seconds to 10 and words <15

##Import Data from CSV Files
f = open('cagenum.csv')
csv_f = csv.reader(f)
a = []
w = []
gameType = ["Words", "Seconds"]

for row in csv_f:
	a.extend(row)

#add list of non-random word in cageword1.csv
word = open('cageword1.csv')
csv_w = csv.reader(word)
for row in csv_w:
	w.append(row)
#number of custom words
#N_cwords = len(w)
#print(random.randrange(0,len(w),1))
#add second list
word = open('cageword.csv')
csv_w = csv.reader(word)

#only add selected random words
for row in csv_w:
	w.append(row)

#print(w)


#Set up trivial Variables 
N_word = len(w)
N_num = len(a)
count = 0


while True:
	try:
		uNumberofPlayers = int(raw_input("Please enter number of players "))
		break
	except ValueError:
		print "Not a Number, Try again"

#Creating Player Array
uPlayerName = []
for i in xrange(0, uNumberofPlayers):
	uPlayerName.append(raw_input("Enter a name:"))

#Game Engine
while (count < N_word):
	print "Player: ", uPlayerName[count%uNumberofPlayers]
	wait_sec = a[random.randrange(1,N_num,1)]
	wait_sec_int= int(wait_sec)
	gameType_itt = random.choice(gameType)
	print "Number of",gameType_itt,":", wait_sec 
	print "Word", w[random.randrange(0,N_word,1)] 
	print raw_input("Hit Enter to GO")	

	if gameType_itt == "Seconds":
		for i in xrange(wait_sec_int, 0, -1):
			print i
			time.sleep(1)
	count = count +1
	print "Next"