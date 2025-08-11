import hashlib

class WilsonHash:
    def __init__(self, data: bytes):
        self.data = data
        self._digest = self._compute_digest()

    def _invert_binary(self, bin_num):
        # Invert each bit in a binary string: '0' becomes '1', and '1' becomes '0'
        return "".join("0" if val == "1" else "1" for val in bin_num)

    def _compute_digest(self):
        # Convert each byte to an 8-bit binary string and join them
        binary_str = "".join(format(byte, "08b") for byte in self.data)
        
        # Pad the binary string until its length is a multiple of 128 bytes
        block_size_bytes = 128
        padding_length_bytes = block_size_bytes - len(self.data) % block_size_bytes
        
        # Pad by repeatedly inverting 8-bit segments determined from the binary string value
        for i in range(padding_length_bytes):
            start_idx = int(binary_str, 2) % (len(binary_str) - 8)
            segment = binary_str[start_idx:start_idx + 8]
            inverted = self._invert_binary(segment)
            binary_str += inverted

        # Generate digest by deterministically selecting a 128-bit slice from the padded binary string
        digest_size_bits = 128
        start_idx = int(binary_str, 2) % (len(binary_str) - digest_size_bits)
        digest_binary = binary_str[start_idx:start_idx + digest_size_bits]

        # Return the digest split into 8-bit chunks and converted to bytes
        return bytes(int(digest_binary[i:i+8], 2) for i in range(0, digest_size_bits, 8))
    
    def digest(self):
        return self._digest
    
    def hexdigest(self):
        return self._digest.hex()
    
    
def main():
    hash_algos = ["sha1", "sha256", "sha512", "blake2b", "md5", "WilsonHash"]

    with open("week4/challenge_submissions/Wilson/data/week4_pt1_input.txt", "r") as f1, open("week4/challenge_submissions/Wilson/data/week4_pt2_input.txt", "r") as f2:
        data1 = f1.read().encode(encoding="utf-8")
        data2 = f2.read().encode(encoding="utf-8")

    results = []
    for hash_algo in hash_algos:
        if hash_algo == "WilsonHash":
            h1 = WilsonHash(data1).hexdigest()
            h2 = WilsonHash(data2).hexdigest()
        else:
            hash_fn = getattr(hashlib, hash_algo)
            h1 = hash_fn(data1).hexdigest()
            h2 = hash_fn(data2).hexdigest()
        
        percent_diff = sum(c1 != c2 for c1, c2 in zip(h1, h2)) / len(h1)

        results.append((hash_algo, percent_diff))
        
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    for algo, pct in sorted_results:
        print(f"{algo}: {pct:.1%} difference in hex chars")
        
if __name__ == "__main__":
    main()
