def find_missing(l,l2):
	"""Finds the missing number in the smaller list give two """
	l_l= len(l)
	l_l2 =len(l2)


	if l_l ==0 or l_l2==0:
		return 0           #returns 0 if both lists are empty
	elif l_l == l_l2:
		return 0           #retunns zero if the lists are equal
	elif l_l>l_l2:         #if list one is bigger than lis two
		for i in range(l_l):
			if l[i] not in l2: #checks for the missing item
				return l[i]   #returns the missing item 

	elif l_l<l_l2:            #if list 2 is bigger than list 1
		for i in range(l_l2):
			if l2[i] not in l: #checks for the missing item
				return l2[i]   #checks for the missing item

