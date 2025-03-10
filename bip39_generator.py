import secrets
import hashlib
import sys

def load_wordlist():
    with open("english.txt", "r") as f:
        return [word.strip() for word in f.readlines()]

BIP39_WORDLIST = load_wordlist()

def get_word_count():
    while True:
        count = input("Enter 12 or 24 for word phrase: ").strip()
        if count in ("12", "24"):
            return int(count)
        print("Invalid input. Choose 12 or 24.")

def generate_mnemonic():
    word_count = get_word_count()
    entropy_bytes = 16 if word_count == 12 else 32
    
    entropy = secrets.token_bytes(entropy_bytes)
    hash_bytes = hashlib.sha256(entropy).digest()
    checksum_bits = bin(hash_bytes[0])[2:].zfill(8)[: word_count // 3]
    
    entropy_bits = ''.join([bin(byte)[2:].zfill(8) for byte in entropy])
    combined_bits = entropy_bits + checksum_bits
    
    chunks = [combined_bits[i*11 : (i+1)*11] for i in range(len(combined_bits)//11)]
    mnemonic = [BIP39_WORDLIST[int(chunk, 2)] for chunk in chunks]
    
    return ' '.join(mnemonic)

if __name__ == "__main__":
    try:
        phrase = generate_mnemonic()
        print("\n ☠ Crypto Wallet Secret Phrase Hacked Successfully ☠ :")
        print(phrase)
        print("\n⚠️ Keep this phrase SECRET! ⚠️")
    except KeyboardInterrupt:
        sys.exit("\nOperation cancelled.")
