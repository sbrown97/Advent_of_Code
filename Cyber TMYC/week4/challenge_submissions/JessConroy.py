def probably_a_hash_function(file, prime_multiplier=23, bits = 32):
    hash_value = 0
    for char in file:
        hash_value = (hash_value * prime_multiplier + ord(char)) % 2**bits
    return hash_value

