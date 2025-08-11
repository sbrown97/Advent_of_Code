import requests
import os
import sys
import numpy as np
import hashlib
import pandas as pd

from numpy import log

# local

import hashes as hashes
def submit_answer(question=None, answer = None):
    if not question:
        print('ENTER A QUESTION')
        return 
    if not answer:
        print('ENTER A ANSWER')
        return 
    print(f'Question: {question}\n\tType: {type(question)}')
    print(f'Answer: {answer}\n\tType: {type(answer)}')
    if answer==None:
        print('ANSWER is None; Not submitting')
        return  

    url = r"https://yv9w75zly1.execute-api.us-east-1.amazonaws.com/dev/TMYC_Solution_Checker"  # endpoint of the TMYC API
    # Feel free to use the test below to be sure it's working for you.  But you'll want to customize the fields nested below "Item" for your problem and your submission (see below for the appropriate key to identify a question or part or subpart).
    mysubmission = {
        "operation": "submit",
        "payload": {
            "Item": {
            "id": "bradley.eylander@lmi.org", 
            "question": question,  
            "submission": answer  
            }
        }
    }
    response = requests.post(url, json = mysubmission)  # doing the work
    print(response.text) # because you want to see if your response was correct (or if there was an error!

def get_H(in_chars):
    # seconds in a year 31,557,600
    # N = the number of characters or symbols (for instance, ASCII has 94 total unique symbols)
    # L = the length of the password
    # H = the total information entropy in bits

    L = len(in_chars)
    #get all the non-duplicate character length
    differ_chars = set(in_chars)
    N = len(differ_chars)
    return L * log(N)/log(2)

def part1(filename='week4_pt1_input.txt'):
    # read txt
    with open(filename, 'r') as f:
        pwds = [line.strip() for line in f if line.strip()] 

    cnt_H_65=0
    for c_pwd in pwds:
        H = get_H(c_pwd)
        if H >=65:
            cnt_H_65 += 1
    print(f'Number of H>=65 passwords: {cnt_H_65}')
    return cnt_H_65

# SHA-1, SHA-256, SHA-512, BLAKE2b and MD5
def hash_find_difference(pwd1, pwd2, method='SHA-256'):
    if method == 'SHA-1':
        # hexdigest
        hash1 = hashlib.sha1(pwd1).digest()
        hash2 = hashlib.sha1(pwd2).digest()
    elif method == 'SHA-256':
        hash1 = hashlib.sha256(pwd1).digest()
        hash2 = hashlib.sha256(pwd2).digest()
    elif method == 'SHA-512':
        hash1 = hashlib.sha512(pwd1).digest()
        hash2 = hashlib.sha512(pwd2).digest()
    elif method == 'BLAKE2b':
        hash1 = hashlib.blake2b(pwd1).digest()
        hash2 = hashlib.blake2b(pwd2).digest()
    elif method == 'MD5':
        hash1 = hashlib.md5(pwd1).digest()
        hash2 = hashlib.md5(pwd2).digest()
    else:
        raise ValueError(f"Unsupported hash method: {method}")

    # compare hashes and find percent differnece bewteen the 2:
    cnt_dup=0
    full_cnt = len(hash1)
    for h1, h2 in zip(hash1, hash2):
        # go through each character and tabulate 
        if h1==h2:
            cnt_dup+=1
    per_difference = round(100*(full_cnt-cnt_dup)/full_cnt,1)
    return per_difference, hash1, hash2

def hash_file(filepath, method='SHA-256'):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.read().encode('utf-8')

    if method == 'SHA-1':
        return hashlib.sha1(data).hexdigest()
    elif method == 'SHA-256':
        return hashlib.sha256(data).hexdigest()
    elif method == 'SHA-512':
        return hashlib.sha512(data).hexdigest()
    elif method == 'BLAKE2b':
        return hashlib.blake2b(data).hexdigest()
    elif method == 'MD5':
        return hashlib.md5(data).hexdigest()
    elif method == 'custom':
        return hashes.simple_hash_64bit_custom_salt(data)
    else:
        raise ValueError("Unsupported method")

def part2_individual_passwords(filename1='week4_pt1_input.txt', filename2='week4_pt2_input.txt'):
    # read txt
    # Reach in each file and encode the data with UTF-8 before running the whole file through the hashing algorithm,
    with open(filename1, 'r', encoding='utf-8') as f1:
        utf8_data1 = [line.strip().encode('utf-8') for line in f1 if line.strip()]
    with open(filename2, 'r', encoding='utf-8') as f2:
        utf8_data2 = [line.strip().encode('utf-8') for line in f2 if line.strip()]

    
    # methods: SHA-1, SHA-256, SHA-512, BLAKE2b and MD5
    # tablulate data
    methods = [ "SHA-1","SHA-256", "SHA-512", "BLAKE2b" , "MD5"]
    rows=[]
    for c_method in methods:
        for pwd1, pwd2 in zip(utf8_data1, utf8_data2):
            per_dif,  hash1, hash2 = hash_find_difference(filename1, filename2, method=c_method)
            rows.append({
                'pwd1': pwd1.decode('utf-8'),
                'pwd2': pwd2.decode('utf-8'),
                'method': c_method,
                'hash1': hash1,
                'hash2': hash2,
                'percent_dif %': per_dif
            })

    # convert dictionary to dataframe
    df = pd.DataFrame(rows)
    # save to csv
    df.to_csv('compare_hashing.csv', index=False)
    print(df.head())
    
    return 0

def part2(filename1='week4_pt1_input.txt', filename2='week4_pt2_input.txt'):
    # methods: SHA-1, SHA-256, SHA-512, BLAKE2b and MD5
    # tablulate data
    methods = [ "SHA-1","SHA-256", "SHA-512", "BLAKE2b" , "MD5"]
    rows=[]
    for c_method in methods:
        hash_file1 = hash_file(filename1, method=c_method)
        hash_file2 = hash_file(filename2, method=c_method)
        # compare hashes and find percent differnece bewteen the 2:
        cnt_dup=0
        full_cnt = len(hash_file1)
        for h1, h2 in zip(hash_file1, hash_file2):
            # go through each character and tabulate 
            if h1==h2:
                cnt_dup+=1
        per_difference = round(100*(full_cnt-cnt_dup)/full_cnt,1)
        rows.append({
            'method': c_method,
            'percent_dif %': per_difference
        })

    # convert dictionary to dataframe
    df = pd.DataFrame(rows)
    # save to csv
    df.to_csv('compare_hashing_files.csv', index=False)
    print(df.head())
    # Find the row with the max value
    max_idx = df['percent_dif %'].idxmax()
    max_row = df.loc[max_idx]

    print(f"Method: {max_row['method']}")
    print(f"Avg Diff: {max_row['percent_dif %']}")

    return round(max_row['percent_dif %'], 1)

def part2_df(csv_file='compare_hashing.csv'):
    df = pd.read_csv(csv_file)
    # look at data based on different methods
    methods = (df.method).unique()
    save_method='' 
    save_amount = 0
    save_amount_max=0
    for method in methods:
        temp_data = df[df.method==method]
        diff_data  = temp_data['percent_dif %']
        avg_val = round(np.average(diff_data),1)
        max_val = round(np.max(diff_data),1)
        print(f'Method: {method}')

        print(f'Avg Diff: {avg_val}')
        print(f'Max Diff: {max_val}')
        if avg_val>save_amount:
            save_amount=avg_val
            save_method=method
            save_amount_max=max_val
        
    print(f'Highest avg value: {save_amount} max value: {save_amount_max} using method: {save_method}')
    return save_amount, save_amount_max, save_method

def part3(filename1='week4_pt1_input.txt', filename2='week4_pt2_input.txt'):
    # methods: SHA-1, SHA-256, SHA-512, BLAKE2b and MD5
    # tablulate data
    methods = [ "SHA-1","SHA-256", "SHA-512", "BLAKE2b" , "MD5", 'custom']
    rows=[]
    for c_method in methods:
        hash_file1 = hash_file(filename1, method=c_method)
        hash_file2 = hash_file(filename2, method=c_method)
        # compare hashes and find percent differnece bewteen the 2:
        cnt_dup=0
        full_cnt = len(hash_file1)
        for h1, h2 in zip(hash_file1, hash_file2):
            # go through each character and tabulate 
            if h1==h2:
                cnt_dup+=1
        per_difference = round(100*(full_cnt-cnt_dup)/full_cnt,1)
        rows.append({
            'method': c_method,
            'percent_dif %': per_difference
        })

    # convert dictionary to dataframe
    df = pd.DataFrame(rows)
    # save to csv
    df.to_csv('compare_hashing_files.csv', index=False)
    print(df.head(10))
    # Find the row with the max value
    max_idx = df['percent_dif %'].idxmax()
    max_row = df.loc[max_idx]

    print(f"Method: {max_row['method']}")
    print(f"Avg Diff: {max_row['percent_dif %']}")

    return round(max_row['percent_dif %'], 1)

if __name__ == "__main__":
    # H_cnt = part1()
    # submit_answer(question='w4_1', answer = H_cnt)
    # output = part2()
    # submit_answer(question='w4_2', answer = output)
    output = part3()