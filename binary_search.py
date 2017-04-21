class BinarySearch(list):
	def __init__(self,a,b):
		super(BinarySearch, self).__init__(range(0,(a*b)+1,b)[1:])
		self.length = a

	def search(self,item):
		first = 0
		last = len(self)-1
		found = False
		count = 0 
		result = {}

		if item == self[-1]:
			return {"count":count, "index":last}
		if item == self[0]:
			return {"count":count, "index":first}

		while first<=last and not found:
			center = (first + last)//2
			if self[center] == item:
				found = True
				result['index'] = center
			else:
				if item < self[center]:
					last = center-1
				elif item > self[center]:
					first = center+1
				else:
					found = True
					result['index'] = last
				
			if first == last:
				found = True
				result['index'] = -1

			result['count'] = count
			count += 1

		return result

