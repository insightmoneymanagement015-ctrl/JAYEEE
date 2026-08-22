import hashlib
import json
import time

from config import (
    COIN_NAME,
    COIN_SYMBOL,
    MAX_SUPPLY,
    BLOCK_REWARD,
    DIFFICULTY,
    NETWORK_NAME,
    GENESIS_MESSAGE,
)


class Blockchain:
    def __init__(self):
        self.chain = []
        self.total_supply = 0
        self.create_genesis_block()

    def calculate_hash(self, block):
        data = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(data).hexdigest()

    def create_genesis_block(self):
        block = {
            "index": 0,
            "timestamp": int(time.time()),
            "previous_hash": "0" * 64,
            "transactions": [
                {
                    "type": "genesis",
                    "message": GENESIS_MESSAGE,
                    "coin": COIN_SYMBOL,
                }
            ],
            "nonce": 0,
        }

        block["hash"] = self.calculate_hash(block)
        self.chain.append(block)

    def mine_block(self, miner_address):
        if self.total_supply >= MAX_SUPPLY:
            print("Maximum supply sudah tercapai.")
            return

        reward = min(BLOCK_REWARD, MAX_SUPPLY - self.total_supply)

        block = {
            "index": len(self.chain),
            "timestamp": int(time.time()),
            "previous_hash": self.chain[-1]["hash"],
            "transactions": [
                {
                    "type": "mining_reward",
                    "to": miner_address,
                    "amount": reward,
                    "coin": COIN_SYMBOL,
                }
            ],
            "nonce": 0,
        }

        target = "0" * DIFFICULTY

        print(f"Mining Block #{block['index']}...")

        while True:
            block["hash"] = self.calculate_hash(block)

            if block["hash"].startswith(target):
                break

            block["nonce"] += 1

        self.chain.append(block)
        self.total_supply += reward

        print("\nBlock berhasil ditemukan!")
        print("Block      :", block["index"])
        print("Hash       :", block["hash"])
        print("Nonce      :", block["nonce"])
        print("Reward     :", reward, COIN_SYMBOL)
        print(
            "Total supply:",
            self.total_supply,
            "/",
            MAX_SUPPLY,
            COIN_SYMBOL,
        )

    def show_chain(self):
        print("\n==========", NETWORK_NAME, "==========")

        for block in self.chain:
            print("\nBlock #", block["index"])
            print("Hash:", block["hash"])
            print("Previous:", block["previous_hash"])
            print("Nonce:", block["nonce"])
            print("Transactions:", block["transactions"])

        print(
            "\nSupply:",
            self.total_supply,
            "/",
            MAX_SUPPLY,
            COIN_SYMBOL,
        )


if __name__ == "__main__":
    blockchain = Blockchain()

    print("================================")
    print(COIN_NAME, "Blockchain")
    print("================================")
    print("Symbol:", COIN_SYMBOL)
    print("Max Supply:", MAX_SUPPLY)
    print("Consensus: Proof-of-Work")
    print("Algorithm:", "SHA-256")

    blockchain.mine_block("JAYEEEE-MINER-001")
    blockchain.show_chain()
