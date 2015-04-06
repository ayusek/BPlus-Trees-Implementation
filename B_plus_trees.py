#Assume that no duplicates are allowed , else check for duplicates while inserting

#My B-tree is such that a node that the smallest pointer in its left list

import time
import numpy
'''
file structure
isroot : 
isleaf :
Parent :
left brother :
right brother :
'''   

import linecache
#linecache.getline('/etc/passwd', 4), 0 based count

Disc_Accesses = 0

query0_list_disc = []
query1_list_disc = []
query2_list_disc = []

query0_list_time = []
query1_list_time = []
query2_list_time = []

output_file = open('queryOutput.txt','w')
Disc_Accesses += 1

#This would always remain open
with open ("bplustree.config", "r") as myfile:
	Disc_Accesses += 1
	parameter=myfile.read().replace('\n', '')

#number of entries is between n and 2*n now. 
n = int(parameter)

with open ("tree/data"  , 'w') as myfile:
	myfile.write('')

Disc_Accesses += 1

#You call add_entry, next_line_no corresponds to its line number in the file

file_name_count = 0 
def get_new_name():
	global file_name_count 
	file_name_count += 1 
	return str(file_name_count)



#returns the file name in which the key may be present (Last Occourence Reported)
def get_node(key , node_file):
	
	node_file = str(node_file)
	if(node_file == None):
		return None	

	count = 0 
	switch = False 

	global Disc_Accesses

	for line in open('tree/' + node_file , 'r'):
		Disc_Accesses += 1
		line = line.replace('\n' , '')
		#return its name if its a leaf node
		if(count == 1 and int(line) == 1):
			return node_file

		if (count <=  4):
			count = count + 1
		else :
			#Not - a leaf node
			if (switch ==  False):
				switch = True
				old_path = line
			else:
				switch = False
				if (float(key) < float(line)):
					
					
					return get_node(key , old_path)

	return get_node(key , old_path)


#Returns the line number in the data file for the last occourence
def get_lineno_in_data(key):
	global root
	contatining_file = get_node(key , root)

	if(contatining_file == None):
		return None

	count = 0 
	switch = False 
	flag = False
	actual_line = None

	global Disc_Accesses

	for line in open('tree/' + contatining_file , 'r'):
		Disc_Accesses += 1
		line = line.replace('\n' , '')

		#return its name if its a leaf node
		if(count == 1):
			assert(int(line) == 1)

		if (count <=  4):
			count = count + 1

		else :
			#Not - a leaf node
			if (switch ==  False):
				switch = True
				line_no = int(line)

			else:
				switch = False
				if not flag:
					if (float(key)  == float(line)):
						flag = True
						actual_line = line_no
				else:
					if (float(key)  == float(line)):
						actual_line = line_no			

	return actual_line



next_line_no = 0
def Insert_into_store(data):
	global next_line_no
	next_line_no += 1
	data = data.replace('\n','')
	global Disc_Accesses
	with open ('tree/data','a') as data_file:
		Disc_Accesses += 1
		data_file.write(data + "\n")
	return next_line_no


def adjust_right(file , value):
	global Disc_Accesses
	lines = []
	if(file == 'None'):
		return True

	with open ('tree/' + file , 'r') as myfile:
		Disc_Accesses += 1
		for line in myfile:
			lines.append(line)

	lines[4] = value
	with open ('tree/' + file , 'w') as myfile:
		Disc_Accesses += 1
		for item in lines:
			myfile.write(item)

	return True


def change_parent(file , parent):
	lines = []
	global Disc_Accesses
	with open ('tree/' + file , 'r') as myfile:
		Disc_Accesses += 1
		for line in myfile:
			lines.append(line)

	lines[2] = parent 
	with open ('tree/' + file , 'w') as myfile:
		Disc_Accesses += 1
		for line in lines:
			myfile.write(line)


def notify_children(list , parent):
	switch = True
	for item in list:
		if switch:
			change_parent(item.replace('\n','') , parent + '\n')
			switch = False
		else:
			switch = True

def Insert_into_node(node_name , pointer , key_value):
	node_name = str(node_name)
	pointer = str(pointer)
	key_value = str(key_value)
	lines = []
	global Disc_Accesses

	with open ('tree/' + node_name , 'r') as myfile:
		Disc_Accesses += 1
		for line in myfile:
			lines.append(line)

		#lines has the data for this file
	num_entries = int((len(lines) - 5)/2)


	if(num_entries < n ):
		#Insertable 

		if(len(lines) - 5 == 1):
			i = len(lines)
			lines = lines[0:i-1] + [pointer + '\n' , key_value + '\n' ] + [lines[i-1]]
			
		else:
			Switch = False
					#Insertable
			for i in range(5, len(lines)):

				if(Switch == False):
					Switch = True

				else:
					Switch = False

					if(float(key_value) < float(lines[i])):
						#To be Inserted
						
						lines = lines[0:i-1] + [pointer + '\n' , key_value + '\n' ]+ lines[i-1:]
						break
			else:
				i = len(lines)
				if(lines[i-1] == 'None\n'):
					lines = lines[0:i] + [pointer + '\n' , key_value + '\n' ]
				else:
					
					if(lines[1] == "1\n" ):

						lines = lines + [pointer + '\n' , key_value + '\n' ]
					else:
							lines = lines[0:i-1]   + [pointer + '\n' , key_value + '\n' ]+ lines[i-1 : ]
				

		with open ('tree/' + node_name , 'w') as myfile :
			Disc_Accesses += 1
			for item in lines:				
				myfile.write(item)
		return True

	else:
		
		#Non-Insertable
		#Form two out of them here and then carry them forward
		Switch = False
		for i in range(5, len(lines)):
			if(Switch == False):
				Switch = True

			else:
				Switch = False

				if(float(key_value) < float(lines[i])):
					#To be Inserted
					
					lines = lines[0:i-1] + [pointer + '\n' , key_value + '\n' ]+ lines[i-1:]
					break
		else:
			if(Switch == True):
				#last one was a pointer
				i = len(lines)
				lines = lines[0:i-1] + [pointer + '\n' , key_value + '\n' ]+ [lines[i-1]]
			else:
				#last one was a key
				lines = lines + [pointer + '\n' , key_value + '\n' ]

		#Now, I need to split the lines
		if(int(lines[1].replace('\n' ,'')) == 1):
			#Leaf Node
			#Split lines accordingly and then link those files
			old_headers = lines[0:5]
			
			entries = len(lines) - 5
			assert(entries%2 == 0 )
			data = lines[5:]
			size = len(data)
			assert(size % 2 == 0 )
			end = int(size/4)*2
			first_half = data[0:end]
			second_half = data[end:]

			second_part = old_headers + second_half
			first_part = ['0\n' , '1\n' , lines[2] , second_part[3] , node_name + '\n'] + first_half

			new_file = get_new_name()

			second_part[3] = new_file + '\n'

			with open ('tree/' + node_name , 'w') as myfile :
				Disc_Accesses += 1
				for item in second_part:				
					myfile.write(item)


			with open ('tree/' + new_file , 'w') as myfile :
				Disc_Accesses += 1
				for item in first_part:				
					myfile.write(item)

			adjust_right(first_part[3].replace('\n' , '') , new_file + '\n')

			return Insert_into_node(lines[2].replace('\n','') , new_file , second_part[6].replace('\n','') )
				
		else:
			old_headers = lines[0:5]
			
			entries = len(lines) - 5
			data = lines[5:]
			size = len(data)
			end = int(size/4)*2
			
			first_half = data[0:end-1]
			second_half = data[end:]

			Parent = old_headers[2].replace('\n','')
			carry = data[end-1].replace('\n','')

			if(Parent == 'None' and old_headers[0] == '1\n'):
				#Root Node
				new_file1 = get_new_name()
				new_file2 = get_new_name()
				old_headers[2] = new_file2 + '\n'
				old_headers[0] = "0\n"
				second_part = old_headers + second_half
				first_part = old_headers + first_half

				with open ('tree/' + new_file1 , 'w') as myfile :
					Disc_Accesses += 1
					for item in first_part:				
						myfile.write(item)

				#No need to maintain siblings
				with open ('tree/' + node_name , 'w') as myfile :
					Disc_Accesses += 1
					for item in second_part:				
						myfile.write(item)
				

				root_data = ['1\n' , '0\n' , 'None\n' , 'None\n' , 'None\n' , new_file1 + '\n' , carry + '\n' , node_name + '\n' ]

				with open ('tree/' + new_file2 , 'w') as myfile :
					Disc_Accesses += 1
					for item in root_data:				
						myfile.write(item)

				global root 
				root = new_file2

				notify_children(first_half , new_file1) #Tell children about their new parent

				return True
			else:
			#old_headers have information of the parent as well here
				second_part = old_headers + second_half
				first_part = old_headers + first_half

				new_file = get_new_name()

				with open ('tree/' + new_file , 'w') as myfile :
					Disc_Accesses += 1
					for item in first_part:				
						myfile.write(item)

				#No need to maintain siblings
				with open ('tree/' + node_name , 'w') as myfile :
					Disc_Accesses += 1
					for item in second_part:				
						myfile.write(item)

				notify_children(first_half , new_file)
				return Insert_into_node(Parent , new_file , carry)

		assert(False)
		return False
			



#Insertion Mastermind
def Insert_into_tree(key  , lineno):
	key = str(key)
	lineno = str(lineno)
	leaf_node_to_insert = get_node(key , root)
	return Insert_into_node(leaf_node_to_insert , lineno , key)


#The Data format needs to be very strict
def Insert(data):
	key = data.split('\t')[0]
	return Insert_into_tree(key , Insert_into_store(data))


#Insert Basic Data First
def Insert_Basic():
	global Disc_Accesses
	for line in open('assgn2_bplus_data.txt','r'):
		Disc_Accesses += 1
		Insert(line)

def Initialize():
	global root 
	global Disc_Accesses
	root = get_new_name()
	single_leaf = get_new_name()
	#Initializing Root
	with open ('tree/' + root , 'w') as myfile:
		Disc_Accesses += 1
		myfile.write('1\n')
		myfile.write('0\n')
		myfile.write('None\n')
		myfile.write('None\n')
		myfile.write('None\n')
		myfile.write(single_leaf + '\n')

	with  open ('tree/' + single_leaf , 'w') as myfile:
		Disc_Accesses += 1
		myfile.write('0\n')
		myfile.write('1\n')
		myfile.write(root + '\n')
		myfile.write('None\n')
		
		myfile.write('None\n')

def search_all_in_file_left(end_node , key):
	if(end_node == 'None' or end_node == None):
		return []

	data_list = []
	lines = []

	global Disc_Accesses
	with open ('tree/' + end_node , 'r') as myfile:
		Disc_Accesses += 1
		for line in myfile:
			lines.append(line.replace('\n',''))

	#lines is the list of lines in this file
	left_brother = lines[3].replace('\n' ,'')
	switch = True
	put = True

	for i in reversed(range(5,len(lines))):
		if switch:
			switch = False
			if(float(key) == float(lines[i])):
				put = True
			else:
				put = False
		else:
			switch = True
			if put :
				data_list.append(linecache.getline('tree/data' , int(lines[i])))
		
	if put : return data_list + search_all_in_file_left(left_brother , key)
	else : return data_list

def search_all_in_file_right(end_node , lower_limit ,upper_limit):
	data_list = []
	lines = []

	if(end_node == 'None' or end_node == None):
		return data_list

	global Disc_Accesses
	with open ('tree/' + end_node , 'r') as myfile:
		Disc_Accesses += 1
		for line in myfile:
			lines.append(line.replace('\n',''))

	switch = False
	old_line = 0
	for i in range(5, len(lines)):
		if switch : 
			print (float(lines[i]),upper_limit,lower_limit)
			if (float(lines[i]) <= upper_limit and float(lines[i]) >= lower_limit):
				data_list.append(linecache.getline('tree/data' , int(old_line)))
			switch = False

		else:
			switch = True
			old_line = lines[i]

		
	#lines is the list of lines in this file
	right_brother = lines[4].replace('\n' ,'')

	if(right_brother == 'None'):
		return data_list
	else:
		if (float(lines[len(lines) - 1]) <= float(upper_limit) and float(lines[len(lines) - 1]) >= float(lower_limit)):
			return data_list + search_all_in_file_right(right_brother , lower_limit , upper_limit) 
		else:
			return data_list
	
def query0(key , value):
	key = key.replace('\n','').replace(' ','')
	value = value.replace('\n' , '').replace(' ','')

	global Disc_Accesses
	global output_file
	Disc_Accesses = 0 
	start_time = time.clock()

	if (Insert(key + '\t' + value + '\n')):
		time_taken = str(time.clock() - start_time)
		
		output_file.write("Insertion Done in "+ time_taken  +" seconds with "+str(Disc_Accesses) + " Disc Accesses")
	else:
		output_file.write("Insertion Unsuccessful")

	global query0_list_time
	global query0_list_disc

	query0_list_disc.append(Disc_Accesses)
	query0_list_time.append(time_taken)

	return True

def query1(key):
	key = str(key).replace('\n','').replace(' ','')
	#Searching this key
	global root

	global Disc_Accesses
	global output_file
	Disc_Accesses = 0 
	start_time = time.clock()
	data_list = search_all_in_file_left(get_node(key,root) , key) #Returns the node with the last occourence of the key
	#Write data list in file and then record stats
	time_taken = str(time.clock() - start_time)
		
	output_file.write(str(data_list) + " found in "+ time_taken  +" seconds with "+str(Disc_Accesses) + " Disc Accesses")

	global query1_list_time
	global query1_list_disc

	query1_list_disc.append(Disc_Accesses)
	query1_list_time.append(time_taken)

	return True

def query2(center , range):
	center = float(str(center).replace('\n',''))
	range = float(str(range).replace('\n',''))
	lower_limit = center - range
	upper_limit = center + range
	infremum = lower_limit - 0.000001

	global root
	global Disc_Accesses
	global output_file


	Disc_Accesses = 0 
	start_time = time.clock()
	data_list = search_all_in_file_right(get_node(infremum , root), lower_limit, upper_limit)
	#Write data list in file and then record stats
	time_taken = str(time.clock() - start_time)
		
	output_file.write(str(data_list) + " found in the given range in "+ time_taken  + " seconds with "+str(Disc_Accesses) + " Disc Accesses")

	global query2_list_time
	global query2_list_disc

	query2_list_disc.append(Disc_Accesses)
	query2_list_time.append(time_taken)

	return True


def query(file):
	global Disc_Accesses
	with open (file , 'r') as myfile:
		Disc_Accesses += 1
		for line in myfile :
			words = line.split('\t')
			if(words[0] == '0' ):
				query0(words[1] , words[2])
			elif(words[0] == '1'):
				query1(words[1])
			elif(words[0] == '2'):
				query2(words[1], words[2])
			else:
				print line
		return True


start_time = time.clock()
Initialize()  #Initializes the B-Tree Structure..
Insert_Basic()

print time.clock() - start_time,"--seconds taken to do Basic Insertions"
print "Number of Disc Accesses:",Disc_Accesses 
print "Root node is:" , root

print "Running Queries --- "
query('querysample.txt')

print "--------------------------QUERY STATS----------------------------------------"
print "\t\t-----QUERY0-----\t\t"
print "Minimum Time=",min(query0_list_time)
print "Maximim Time=",max(query0_list_time)
print "Average Time=",numpy.mean(query0_list_time)
print "Standard Deviation in Time from Average=",numpy.std(query0_list_time)
print "----"
print "Minimum Disc Accesses=",min(query0_list_disc)
print "Maximim Disc Accesses=",max(query0_list_disc)
print "Average Disc Accesses=",numpy.mean(query0_list_disc)
print "Standard Deviation in Disc Accesses from Average=",numpy.std(query0_list_disc)
print ""
print "\t\t-----QUERY0-----\t\t"
print "Minimum Time=",min(query1_list_time)
print "Maximim Time=",max(query1_list_time)
print "Average Time=",numpy.mean(query1_list_time)
print "Standard Deviation in Time from Average=",numpy.std(query1_list_time)
print "----"
print "Minimum Disc Accesses=",min(query1_list_disc)
print "Maximim Disc Accesses=",max(query1_list_disc)
print "Average Disc Accesses=",numpy.mean(query1_list_disc)
print "Standard Deviation in Disc Accesses from Average=",numpy.std(query1_list_disc)
print ""
print "\t\t-----QUERY0-----\t\t"
print "Minimum Time=",min(query2_list_time)
print "Maximim Time=",max(query2_list_time)
print "Average Time=",numpy.mean(query2_list_time)
print "Standard Deviation in Time from Average=",numpy.std(query2_list_time)
print "----"
print "Minimum Disc Accesses=",min(query2_list_disc)
print "Maximim Disc Accesses=",max(query2_list_disc)
print "Average Disc Accesses=",numpy.mean(query2_list_disc)
print "Standard Deviation in Disc Accesses from Average=",numpy.std(query2_list_disc)
output_file.close()


