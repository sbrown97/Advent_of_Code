import random
import string
import argparse

from week4_solution import entropy

characters = string.ascii_letters + string.digits + string.punctuation
characters = characters.replace(',','')  #remove , so that part 2 can use commas to sparate passwords

def make_password(L):

	password = random.choices(characters, k=L)
	return ''.join(password)


if __name__=="__main__":

	parser = argparse.ArgumentParser(description='')

	parser.add_argument('--p1_file', default='Cyber TMYC/week4/week4_pt1_input.txt', type=str )
	parser.add_argument('--p2_file', default='Cyber TMYC/week4/week4_pt2_input.txt', type=str )
	parser.add_argument('--num_passwords', default=200,type=int )

	args = parser.parse_args()


	# create/open part 1 input file
#	with open(args.p1_file,'w') as file:
#		for i in range(args.num_passwords):
#			# generate password
#			L = random.randint(5,25)
#			password = make_password(L)
#			print(f'L: {L}  entropy: {entropy(password)}')
#
#			# write password to file
#			file.write(password)
#			file.write('\n')

	# create/open part 2 input file
	with open(args.p2_file,'w') as file:
		for i in range(args.num_passwords):
			# generate password
			L1 = random.randint(17,25)
			p1 = make_password(L1)
			while entropy(p1) < 65:
				p1 = make_password(L1)
			print(f'L: {L1} entropy: {entropy(p1)}')
			#L2 = random.randint(5,25)
			#p2 = make_password(L2)

			# write password to file
			#file.write(f'{p1} , {p2}')
			file.write(p1)
			file.write('\n')