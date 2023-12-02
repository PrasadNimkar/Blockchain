from hashlib import sha256
import time

class Block:
    def __init__(self, timestamp, data, previousHash=' '):
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        return sha256((str(self.timestamp) + str(self.data) + str(self.previousHash)).encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesis()]

    def createGenesis(self):
        return Block(time.ctime(), "genesisBlock", "00000")

    def mineBlock(self, date):
        node = Block(time.ctime(), date, self.chain[-1].hash)
        self.chain.append(node)

    def printBlockchain(self):
        for i in range(len(self.chain)):
            print("\n---Block", i, "-------\n timestamp = ", self.chain[i].timestamp, "\n data = ", self.chain[i].data,
                  "\n previousHash =", self.chain[i].previousHash, "\n hash = ", self.chain[i].hash)


CEVcoin = Blockchain()
data = input("Enter data for the new block: ")
print("\n\n------>Mining New Block--->")
CEVcoin.mineBlock(data)
print("\n\n------->New Block mined successfully-->")

CEVcoin.printBlockchain()
