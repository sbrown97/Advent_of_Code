from JessConroy import probably_a_hash_function



if __name__=="__main__":

	p1_file = 'week4/week4_pt1_input.txt'
	p2_file = 'week4/week4_pt2_input_v2.txt'

	with open(p1_file,'r') as file:
		p1 = file.read()
		#p1 = p1.encode('utf-8')

	with open(p2_file,'r') as file:
		p2 = file.read()
		#p2 = p2.encode('utf-8')

	
	h1 = probably_a_hash_function(p1)
	print(f'Hash of file 1: {h1}')
	h2 = probably_a_hash_function(p2)
	print(f'Hash of file 2: {h2}')

	diff = sum(1 for char1, char2 in zip(h1,h2) if char1 != char2)
	print(f'character change percent: {diff/len(h1)}')