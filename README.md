# BPlus-Trees-Implementation

This is a simulation of BPlus Trees using files, done as a part of the course assignment for CS315A at IIT Kanpur. I have implemented a B-Plus Tree which supports the following 

1. Search
2. Range Search
3. Insertion

Deletion of keys is not yet handeled. 
The data is stores in a contiguos record format in data file in tree folder. 
The exact problem statement may be seen from BTreeAssignment.pdf

##Some of the statistics are given below:
###Basic Inserions
48.398025 --seconds taken to do Basic Insertions

Number of Disc Accesses: 8895432

###Sample Query file
####QUERY1		
Minimum Time= 0.000112000000001

Maximim Time= 0.017766

Average Time= 0.00025188

Standard Deviation in Time from Average= 0.000561177664915

Minimum Disc Accesses= 19.0

Maximim Disc Accesses= 210.0

Average Disc Accesses= 111.614

Standard Deviation in Disc Accesses from Average= 39.8847465079


####QUERY2	
Minimum Time= 0.000111000000004

Maximim Time= 0.001989

Average Time= 0.000611343

Standard Deviation in Time from Average= 0.000306842701316


Minimum Disc Accesses= 20.0

Maximim Disc Accesses= 217.0

Average Disc Accesses= 114.289

Standard Deviation in Disc Accesses from Average= 40.6417209158


####QUERY3		
Minimum Time= 0.000220000000006

Maximim Time= 0.002155

Average Time= 0.000425452

Standard Deviation in Time from Average= 0.000174742873091

Minimum Disc Accesses= 21.0

Maximim Disc Accesses= 216.0

Average Disc Accesses= 112.26

Standard Deviation in Disc Accesses from Average= 38.7302775616

From the above statistics we can conclude that the average number of Disc Accesses is same for all the three operations. But single search takes less time that Insertion. This is expected as reading is faster than writing. 
