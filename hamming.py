from secrets import randbits
def gen_hamming(x):
    x = [x>>3,x>>2&1,x>>1&1,x&1]
    p1 = x[0] ^ x[1] ^ x[3]
    p2 = x[0] ^ x[2] ^ x[3]
    p4 = x[1] ^ x[2] ^ x[3]
    p8 = x[0] ^ x[1] ^ x[2]
    bits = [p1,p2,x[0],p4,x[1],x[2],x[3],p8]
    if randbits(2) != 0:
        bits[randbits(3)] ^= 1
    return ''.join(map(str,bits))
    
def transmit(m,fout):
    for c in m:
        fout.write(gen_hamming(ord(c)>>4)+'\n')
        fout.write(gen_hamming(ord(c)&0xf)+'\n')
        
def decode_hamming(bits):
    p1 = bits[0] ^ bits[2] ^ bits[4] ^ bits[6]
    p2 = bits[1] ^ bits[2] ^ bits[5] ^ bits[6]
    p4 = bits[3] ^ bits[4] ^ bits[5] ^ bits[6]
    p8 = bits[7] ^ bits[0] ^ bits[1] ^ bits[2]
    
    error_position = p1 + p2 * 2 + p4 * 4 + p8 * 8
    if error_position == 0:
        return bits[2], bits[4], bits[5], bits[6]
    
    # Correct the error if possible
    if error_position <= 7:
        bits[error_position - 1] ^= 1
    
    return bits[2], bits[4], bits[5], bits[6]

def reverse_transmit(file_path):
    encoded_data = open(file_path, "r").readlines()
    flag = ""
    
    for i in range(0, len(encoded_data), 2):
        bits1 = list(map(int, encoded_data[i].strip()))
        bits2 = list(map(int, encoded_data[i + 1].strip()))
        
        chunk1 = decode_hamming(bits1)
        chunk2 = decode_hamming(bits2)
        
        flag += chr(((chunk1[0] << 3) + (chunk1[1] << 2) + (chunk1[2] << 1) + chunk1[3])*10+((chunk2[0] << 3) + (chunk2[1] << 2) + (chunk2[2] << 1) + chunk2[3])+36)
    
    return flag

recovered_flag = reverse_transmit("output.txt")
print("Recovered Flag:", recovered_flag)

