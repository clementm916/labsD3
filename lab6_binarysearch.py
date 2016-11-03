class BinarySearch(list):
	"""Class Binary Search extends list """
	def __init__(self,a,b):
		data =[x for x in range(b,a*b+1,b)]
		self.length = len(data)
		super(BinarySearch, self).__init__()
		self.extend(data)


	def search(self, target):
	    """Implements binary search algorithm"""
	    lower = 0
	    upper = len(self)
	    count=0
	    if target == self[upper-1]:
	    	return {"count":count,"index":upper-1}
	    if target ==self[lower]:
	    	return {"count":count,"index":lower}
	    while lower < upper:
	    	
	        x = lower + (upper - lower) // 2
	        val = self[x]
	        if target == val:
	        	count+=1
	        	return {"count":count,"index":x}
	        elif target > val:
	            if lower == x:
	            	count+=1
	                break
	            lower = x
	        elif target < val:
	            upper = x
	            count+=1
	        
	    return {"count":count, "index":-1}
