import math
import hashlib
from collections import Counter

def entropy(password):
	# H = L (logN / log2)
	L = len(password)
	N = len(set(password))
#	N = 94

	H = L * (math.log(N)/math.log(2))

	return H


def part1(password_file):

	strong_passwords = 0
	weak_passwords = 0
	delta = 0
	total_H = 0
	num_passwords = 0
	weak_H = 0

	# part 1
	with open(password_file,'r') as file:
		for password in file.readlines():
			password = password.replace('\n','')
			H = entropy(password)
			total_H += H
			num_passwords += 1

			if H >= 65:
				strong_passwords += 1
			else:
				weak_passwords += 1
				weak_H += H
				delta += (65 - H)


	print(f'Week 5 part 1: {strong_passwords} strong passwords, {weak_passwords} weak passwords, {total_H/num_passwords} average entropy')

	return

def avalanche_function(p1, p2):


	# SHA-256
	h1 = hashlib.sha256(p1).hexdigest()
	h2 = hashlib.sha256(p2).hexdigest()

	diff = sum(1 for char1, char2 in zip(h1, h2) if char1 != char2)
	print(f'SHA-256 	bit change % : {diff/len(h1)}')
	
	# SHA-512
	h1 = hashlib.sha512(p1).hexdigest()
	h2 = hashlib.sha512(p2).hexdigest()

	diff = sum(1 for char1, char2 in zip(h1, h2) if char1 != char2)
	print(f'SHA-512 	bit change % : {diff/len(h1)}')

	# SHA-1
	h1 = hashlib.sha1(p1).hexdigest()
	h2 = hashlib.sha1(p2).hexdigest()

	diff = sum(1 for char1, char2 in zip(h1, h2) if char1 != char2)
	print(f'SHA-1 	bit change % : {diff/len(h1)}')

	h1 = hashlib.blake2b(p1).hexdigest()
	h2 = hashlib.blake2b(p2).hexdigest()

	diff = sum(1 for char1, char2 in zip(h1, h2) if char1 != char2)
	print(f'Blake2b 	bit change % : {diff/len(h1)}')
	
	h1 = hashlib.md5(p1).hexdigest()
	h2 = hashlib.md5(p2).hexdigest()

	diff = sum(1 for char1, char2 in zip(h1, h2) if char1 != char2)
	print(f'MD-5	bit change % : {diff/len(h1)}')

	return
	


def part2(p1_file, p2_file):

	with open(p1_file,'r') as file:
		p1 = file.read()
		p1 = p1.encode('utf-8')

	with open(p2_file,'r') as file:
		p2 = file.read()
		p2 = p2.encode('utf-8')

	avalanche_function(p1,p2)
	return 


if __name__=="__main__":

	p1_file = 'week4/week4_pt1_input.txt'
	
	part1(p1_file)

	p2_file = 'week4/week4_pt2_input_v2.txt'

	part2(p1_file, p2_file)
