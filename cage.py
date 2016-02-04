import numpy as np, random, csv, time, sys

##Import Data from CSV Files
f = open('cagenum.csv')
csv_f = csv.reader(f)
a = []
w = []
gameType = ["Words", "Seconds", "Lines"]

for row in csv_f:
	a.extend(row)

word = open('cageword.csv')
csv_w = csv.reader(word)

for row in csv_w:
	w.append(row)


#Set up trivial Variables 
N_word = len(w)
N_num = len(a)
count = 0


#Creating Player Array
uNumberofPlayers = int(raw_input("Please enter number of players "))
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
	print "DONE"