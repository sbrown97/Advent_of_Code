import os

def simple_hash_32bit(text):
    # Initialize hash value (just a constant)
    hash_val = 0xDEADBEEF

    for i, ch in enumerate(text):
        # Convert char to integer
        val = ord(ch)
        # Combine using basic math
        # this line of code takes the current hash value, incorporates the value and position of the current character, 
        # and then mixes these together using addition and a position-dependent bitwise XOR with a left-shifted version of the character's value. 
        hash_val = (hash_val + val * (i + 1)) ^ (val << (i % 4))
        hash_val = hash_val & 0xFFFFFFFF  # Keep it 32-bit

    # Convert to fixed-length hex string
    # convert it to its lowercase hexadecimal representation,
    # and ensure the resulting string is at least 8 characters long by padding it with leading zeros if necessary.
    return f"{hash_val:08x}"

def simple_hash_64bit(text):
    # Initialize hash value (just a constant)
    hash_val = 0xDEADBEEFDEADBEEF

    for i, ch in enumerate(text):
        # Convert char to integer
        val = ord(ch)
        shift_ = (i % 8) * 8
        # SHIFT LEFT and OR
        mixed = (val << shift_) | (val * (i + 1))
        # XOR
        hash_val ^= mixed
        # XOR + SHIFT RIGHT
        hash_val = (hash_val + (val ^ (hash_val >> 3))) & 0xFFFFFFFFFFFFFFFF  # Keep 64-bit

    return f"{hash_val:016x}"

# idea: 
# 1. whether or not the characters represent an even or odd number and 
# 2. sum or the first 10 letters.
def custom_deterministic_salt(text):
    text_bytes=False
    if isinstance(text, bytes):
        text = text.decode('utf-8', errors='ignore')
        text_bytes=True
    partial = text[:10]
    binary_pattern = ""
    sum_ascii = 0
    for ch in partial:
        num = ord(ch)
        sum_ascii += num
        # determine if odd or even
        # binary 1 if odd
        # binary 0 if even
        binary_pattern += '1' if num % 2 else '0'

    # padd 0's to the right
    padded_binary = binary_pattern.ljust(10, '0')[:10]
    binary_int= int(padded_binary, 2)

    # Convert both pieces to integers and combine
    # XOR (1) and (2)
    salt_val = (binary_int ^ sum_ascii) & 0xFFFFFFFFFFFFFFFF

    # Return as byte string (8 bytes = 64 bits)
    if text_bytes:
        return salt_val.to_bytes(8, 'big')
    else:
        return salt_val.to_bytes(8, 'big')

def simple_hash_64bit_custom_salt(text):
    if isinstance(text, bytes):
        text = text.decode('utf-8', errors='ignore')
    salt = custom_deterministic_salt(text)
    salted_input = salt.hex() + text
    # Initialize hash value (just a constant)
    
    hash_val = 0xDEADBEEFDEADBEEF

    for i, ch in enumerate(salted_input):
        # Convert char to integer
        val = ord(ch)
        shift_ = (i % 8) * 8
        # SHIFT LEFT and OR
        mixed = (val << shift_) | (val * (i + 1))
        # XOR
        hash_val ^= mixed
        # XOR + SHIFT RIGHT
        hash_val = (hash_val + (val ^ (hash_val >> 3))) & 0xFFFFFFFFFFFFFFFF  # Keep 64-bit

    return f"{hash_val:016x}"


if __name__ == "__main__":
    msg = "hello world"
    print('before: ', msg)
    print("simple hash 32bit:", simple_hash_32bit(msg))
    print("simple hash 64bit:", simple_hash_64bit(msg))
    print("simple hash 64bit random salt:", simple_hash_64bit_custom_salt(msg))
    print("simple hash 64bit random salt:", simple_hash_64bit_custom_salt(msg))