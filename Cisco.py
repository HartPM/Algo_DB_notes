def isPrimeNumber(elements):
	# Write your code here
	def is_prime(n):
		for i in range(2,n):
			if (n%i == 0):
				return False
			return True

	result = []
	list = []
	for x in elements:
		list.append(x)
	for n in list:
		if is_prime(n) == True:
			result.append('Prime')
		else:
			result.append('Composite')
	return result
