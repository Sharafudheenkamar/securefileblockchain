import hashlib
import json
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.create_block(previous_hash="1", proof=100)  # Genesis block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'data': self.current_data,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.current_data = []  # Reset the current data
        self.chain.append(block)
        return block

    def add_data(self, data):
        """Add staff or department data to the current transaction list."""
        self.current_data.append(data)

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while True:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":  # Simple mining condition
                return new_proof
            new_proof += 1

    def mine_block(self):
        previous_block = self.chain[-1]
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        return self.create_block(proof, previous_hash)

blockchain = Blockchain()
