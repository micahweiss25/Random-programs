# SHA-256 key generator
# turn message into binary

from numpy import zeros

# Generate the base block
# (depricated)
def genBlock(size):
    # size is the block size
    if size == 512:
        word = 32
        height = size // 32 
    return [[0 for i in range(word)] for j in range(height)]

# alternate method to 
# generate a block
'''def genBlock(size):
    column, row = blockShape(size)
    return zeros(shape=(row,column), dtype=bool)'''

# return the tuple
# of column and row 
# size of the block
def blockShape(size):
    if size == 512:
        column = 32
    row = size // column
    return (column, row) 

# return the size 
# of the block
def blockSize(block):
    return len(block) * len(block[0])

# convert letters/utf-8 
# characters to binary
def ltrToBin(ltr):
    num = ord(ltr)
    bin_list = []
    while num > 0:
        bin_list.append(num % 2)
        num = num // 2        
    return [0] * (8 - len(bin_list)) + bin_list[::-1]

# covert string messages
# in to binary
def strToBin(msg):
    return [ltrToBin(ltr) for ltr in msg]

def create_message(msg, size=512):
    genBlock(blockShape(512))
    strToBin(msg)

# print the block 
# in a pretty way
def printBlock(block):
    size = blockSize(block)
    column, rows = blockShape(size)
    byte_size = 8
    block_str = ""
    for row in block:
        row_chunks = ["".join([str(j) for j in row[i:i+byte_size]]) for i in range(0,len(row),byte_size)]
        block_str += " ".join(row_chunks) + "\n"
    print(block_str[:-1])

block = genBlock(512)
printBlock(block)