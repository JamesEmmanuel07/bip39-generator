# bip39-generator
BIP39 mnemonic phrase generator

Here’s the updated **README.md** with your repository link incorporated:

```markdown
# BIP39 Mnemonic Phrase Generator

A Python script to generate **BIP39-compliant 12 or 24-word mnemonic phrases** for cryptocurrency wallets. Uses cryptographically secure entropy and validates checksums.

## ⚠️ Security Warning
- **Never share generated phrases** – treat them like passwords!
- **Do not use for real wallets** without thorough security auditing.
- Run **offline** for maximum safety.

---

## 📥 Installation

### **On VS Code (PC)**
1. **Install Python**:  
   Download from [python.org](https://www.python.org/downloads/). Ensure `python --version` works in the terminal.

2. **Clone the Repository**:  
   ```bash
   git clone https://github.com/JamesEmmanuel07/bip39-generator.git
   cd bip39-generator
   ```

3. **Verify Files**:  
   Ensure the folder contains:
   - `bip39_generator.py`
   - `english.txt`

### **On Termux (Android)**
1. **Install Termux**:  
   Download from [F-Droid](https://f-droid.org/en/packages/com.termux/).

2. **Update Packages**:  
   ```bash
   pkg update && pkg upgrade
   ```

3. **Install Dependencies**:  
   ```bash
   pkg install python git
   ```

4. **Clone the Repository**:  
   ```bash
   git clone https://github.com/JamesEmmanuel07/bip39-generator.git
   cd bip39-generator
   ```

---

## 🚀 Usage

### **On VS Code**
1. Open the project folder in VS Code.
2. Launch the terminal (`Ctrl + `` or `Terminal → New Terminal`).
3. Run:
   ```bash
   python bip39_generator.py
   ```
   - If `python` doesn’t work, try `python3`.

### **On Termux**
1. Navigate to the project folder:
   ```bash
   cd bip39-generator
   ```
2. Run the script:
   ```bash
   python bip39_generator.py
   ```

### **Optional: Make the Script Executable**
1. Add execute permissions:
   ```bash
   chmod +x bip39_generator.py
   ```
2. Run directly:
   ```bash
   ./bip39_generator.py
   ```

---

## 📝 Notes
- **Wordlist**: Uses the official BIP39 English wordlist from `english.txt`.
- **Checksum Validation**: Phrase includes a SHA-256 checksum for BIP39 compliance.
- **Testing**: Always test with dummy phrases before real use.

---

## 📜 License
MIT License. See [LICENSE](LICENSE) for details.

---

## 🔗 Repository
[https://github.com/JamesEmmanuel07/bip39-generator](https://github.com/JamesEmmanuel07/bip39-generator)
```

---

### How to Use:
1. Copy the above text.
2. Replace the existing `README.md` in your repository with this updated version.
3. Commit and push the changes:
   ```bash
   git add README.md
   git commit -m "Updated README with installation and usage instructions"
   git push origin main
   ```

Now your repository will have a clear, professional guide for users to install and run the script on both VS Code and Termux! 🚀 Let me know if you need further tweaks. 😊
