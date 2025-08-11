# -*- coding: utf-8 -*-
"""
Created on Tue Apr  16 19:48:28 2025

@author: cjohn
"""

#TMYC Spring 2025 Week 4 - Challenge Problem 3

def myhash( passwords ):
    hex = '0123456789abcdef'
    passwords = passwords.encode('utf-8')    
    
    # Create total based on character and position of character
    tot = 0
    for i in range(len(passwords)):
        tot += ( i + 1 ) * passwords[i]
        
    # Adjust total by mod of some prime number    
    tot = tot % 7919        
    
    # create hash based on total
    h = ''
    for i in range(32):        
        m = (i * tot) % 16
        c = hex[m]
        h += c
        
    return h

# Main ################################################

filename1 = "week4_pt1_input.txt"
filename2 = "Week4_pt2_input.txt"

# Get hash of 1st file

with open(filename1) as f:
    password1 = f.read()  
    # password1 = '!TMYC2025!' # for testing
    hash1 = myhash( password1 )
    
# Get hash of second file

with open(filename2) as f:
    password2 = f.read()  
    # password2 = '%TMYC2025!' # for testing
    hash2 = myhash( password2 )
    
# Compare hash1 versus hash2

number = len(hash1)
dif = 0
for i in range(number):
    if hash1[i] != hash2[i]:
        dif += 1 
        
print(hash1)
print(hash2)

ratio = round( 100.0 * dif / number, 1  )    
     
print('\nPercent Difference:', ratio )






    







            







    
    

# keyword1 = '4920414d2054574f20464f4f4c53'
# keyword2 = '444945204e4f542c20504f4f52204445415448'

# def HexToBin(h):
#     return bin(int(h,16))[2:].zfill(4)

# def AsciiToBin(a):
#     return bin(ord(a))[2:].zfill(8)

# def logical_xor(b1,b2):
#     retvalue = '0'
#     sum = int(b1) + int(b2)
#     if sum == 1:
#         retvalue = '1'
#     return retvalue

# # Check s for keywords
# def checkfile(s,keyword1, keyword2):
#     loc1 = s.find(keyword1)
#     loc2 = s.find(keyword2)
    
#     if loc1 < 0 or loc2 < 0 or loc2 < loc1:
#         return ''
#     else:
#         loc1 = loc1 + len(keyword1)
#         # print(loc1, loc2 )
#         return s[loc1:loc2]

# def searchFolder(directory):
#     for filename in os.listdir(directory):
#         # print(filename)
#         file = open(directory + '/' + filename)
#         s = file.read()
#         result = checkfile(s, keyword1, keyword2)
#         if len(result) > 0:
#             return result
        
#     print('')
        
# directory = 'OneDrive_1_4-21-2025'

# payload = searchFolder(directory)

# counta = payload.count('a')

# print( '\nPart 1: Count of "a": ', counta,'\n')

# ###########################################

# # Part 2

# keyfile = 'Problem 2 Keyfile.txt'

# file = open(keyfile)
# b = file.read()
# b = b.replace(' ','')
# index = 0
# key = 0
# while index <= len(b):
#     h = b[index:index+7]
#     index += 7
#     h = h + '1'
#     l = list(h)
#     h = ''
#     for c in l:
#         if c == '1':
#             h += '0'
#         else:
#             h += '1'
#     key = key + int(h,2)
    
# print('\nPart 2: Key:', key, '\n')

# ################################################

# # Part 3

# ######### Convert Payload to binary ##############################

# # For testing based on question
# # payload = '010000110110000101110010'
# # key = 53

# payload = payload   
# l_payload = list(payload)

# b_payload = ''

# for h in l_payload:
#     b = HexToBin(h)    
#     b_payload += b
    
# # print('Payload:', payload )
# # print( b_payload, list(b_payload) )

# b_payload = list(b_payload)

# # ############Convert key to binary #################################

# # treat key as ascii text - not as integer

# s_key = str(key)
# b_key = ''
# for c in s_key:
#     b_key += AsciiToBin(c)
   
# b_key = list(b_key)
    
# ############# xor message and key 

# index = 0 

# xor = ''
# for b in b_payload:
#     if index >= len(b_key):
#         index = 0
#     xor +=  logical_xor( b, b_key[index])
#     index += 1
   
# # convert to ascii
    
# s = ''.join(chr(int(xor[i:i+8], 2)) for i in range(0, len(xor), 8))

# # print results

# pos = s.find('.')

# message = s[:pos+1]

# print('\nPart 3: Mmessage: ', message)
    
