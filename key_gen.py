# SHA-256 key generator
# turn message into binary

from numpy import zeros

# Generate the base block
def genBlock(size):
    # size is the block size
    if size == 512:
        word = 32
        height = size // 32 
    array = [[0 for i in range(word)] for j in range(height)]
    return array

# return the column and row size of the block
def blockShape(size):
    if size == 512:
        column = 32
    rows = size // column
    return (column, rows) 

# convert 
def ltrToBin(ltr):
    num = ord(ltr)
    bin_list = []
    while num > 0:
        bin_list.append(num % 2)
        num = num // 2        
    return [0] * (8 - len(bin_list)) + bin_list[::-1]

def strToBin(msg):
    return [ltrToBin(ltr) for ltr in msg]

print(strToBin("Hello"))

block = zeros(shape=(32,16), dtype=bool)

def create_message(msg, size=512):
    genBlock(512)
    toBinary(msg)
#print(genBlock(512))
#print(block)