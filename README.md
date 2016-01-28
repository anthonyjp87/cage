# cage

This is a stand alone python game that is created based on an interview I saw with the composer John Cage

The game is simple--get a random topic and a number of seconds and speak (intelligently) about the topic for the number of seconds.

So, this game selects a random amount of time based on the cagenum.csv file. This file contains 1000 numbers in a specific distribution. In order to capture an appropriate sample I created a distribution of random int's starting at 1 and tapering off around thrity. 

The file CageWord is a list of many random words. 

The came combines the two. 


A new change: 
Instead of only getting seconds + word, I've added Lines and Words. So randomly, the user will get either seconds, lines, or words and a subject. 

I've also added a timer. 


