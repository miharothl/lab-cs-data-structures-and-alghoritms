import datetime
import hashlib
from time import sleep


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash()
        self.next = None

    def _calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (self.data + self.timestamp.strftime("%m/%d/%Y, %H:%M:%S")).encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):

        if data is None:
            return

        if self.head is None:
            block = Block(datetime.datetime.now(), data, previous_hash=None)
            self.head = block
            self.tail = block
        else:
            block = Block(datetime.datetime.now(), data, previous_hash=self.tail.hash)
            self.tail.next = block
            self.tail = self.tail.next


def test_block_chain_integrity_block_should_contain_hash_from_previous_block():

    chain = BlockChain()

    chain.append('1st block')
    chain.append('2st block')
    chain.append('3st block')

    chain.head.hash == chain.head.next.previous_hash

    print("Pass: Block contains hash of previous block."
          if chain.head.hash == chain.head.next.previous_hash else "Fail")


def test_appending_block_with_same_message_should_have_different_hash():

    chain = BlockChain()

    chain.append('3st block')
    sleep(1)
    chain.append('3st block')  # Same data added, block should have different hash as its time dependent

    print("Pass: Same data."
          if chain.head.data == chain.head.next.data else "Fail")
    print("Pass: Different hash as hash is timestamp dependent."
          if chain.head.hash != chain.head.next.hash else "Fail")


def test_can_append_block_with_empty_message():

    chain = BlockChain()

    chain.append('3st block')
    chain.append('')

    print("Pass: Chain can contain empty data."
          if chain.head.next.data == '' else "Fail")


if __name__ == "__main__":
    test_block_chain_integrity_block_should_contain_hash_from_previous_block()
    test_appending_block_with_same_message_should_have_different_hash()
    test_can_append_block_with_empty_message()
