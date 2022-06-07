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

class Block:
    def __init__(self):
        self.size = None
        self.block = None
        self.word = None
        self.height = None

    def __str__(self):
        try:
            byte_size = 8
            block_str = ""
            for row in self.block:
                row_chunks = ["".join([str(j) for j in row[i:i+byte_size]]) for i in range(0,len(row),byte_size)]
                block_str += " ".join(row_chunks) + "\n"
            return block_str[:-1]
        except NameError:
            return "You have not generate a block. Use the `_.genBlock()` method"

    # print the height and word size
    def blockShape(self):
        try:
            print(f"number of columns: {self.height}\nsize of each word: {self.word}")
        except NameError:
            print("height and word are not defined. Try creating a block first")

    # return the number
    # of bits in the block
    def blockSize(self, block):
        self.block = block
        return len(block) * len(block[0])

    # Generate the base block
    # (Alt. use numpy array)
    def genBlock(self, size):
        # size is the number of bits in the block
        self.size = size
        if size == 512:
            self.word = 32
            self.height = self.size // 32 
        self.block = [[0 for i in range(self.word)] for j in range(self.height)]

    # turn a string message
    # into binary and merge it 
    # with the block
    def addMessage(self, msg):
        # have fun trying to understand
        # this one...
        # it turns a list of lists
        # into a list
        bin_msg = [j for i in strToBin(msg) for j in i]

        # append the message to the front of the block
        idx = 0
        clm = 0
        while idx < len(bin_msg):
            if idx % self.word == 0 and idx != 0:
                clm += 1
            self.block[clm][idx] = bin_msg[idx]
            idx += 1

        # append a 1 to the end
        self.block[clm][idx] = 1

        # append the length of the
        # message to the end 
        # of the block
        length = [i for i in bin(len(msg) * 8)][2:]
        idx = len(length)
        while idx > 0:
            self.block[-1][-idx] = length[len(length)-idx]
            idx -= 1
