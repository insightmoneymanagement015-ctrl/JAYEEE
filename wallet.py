import hashlib
import secrets


def create_wallet():
    private_key = secrets.token_hex(32)

    public_key = hashlib.sha256(
        private_key.encode()
    ).hexdigest()

    address = "JAYE" + hashlib.sha256(
        public_key.encode()
    ).hexdigest()[:40]

    return private_key, public_key, address


if __name__ == "__main__":
    private_key, public_key, address = create_wallet()

    print("========== JAYEEEE WALLET ==========")
    print("Address:")
    print(address)

    print("\nPublic Key:")
    print(public_key)

    print("\nPrivate Key:")
    print(private_key)

    print("\nPERINGATAN:")
    print("Jangan bagikan Private Key kepada siapa pun.")
