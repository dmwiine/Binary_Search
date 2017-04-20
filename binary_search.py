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

one_to_twenty = BinarySearch(20, 1)
ten_to_thousand = BinarySearch(100, 10)
two_to_forty = BinarySearch(20, 2)

print(one_to_twenty.search(16))
print(ten_to_thousand.search(10000))
print(two_to_forty.search(33))