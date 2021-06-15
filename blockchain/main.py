class Block():
    def __init__(self, index, timestamp, data, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.__hash__()

    def __eq__(self, other):
        return self.data == other.data and self.index == other.index

    def __hash__(self):
        return hash(self.data)

    def __str__(self):
        return self.index + self.timestamp + self.data + self.previousHash + "%d" %self.hash

    def __repr__(self):
        return "%d" %self.hash


class blockChain():
    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block(0, "01/01/2021", "Genesis Block", "0")

    def getLatestBlock(self):
        return self.chain[-1]


 #  def addNewBlock(self, newBlock):
   #    newBlock.previoushash = self.getLatestBlock().hash
    #   newBlock.hash = hash()

x = Block("0", "01/01/2021", "Genesis Block", "0")
print([x])