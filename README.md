Windows / Linux (same commands):



Python virtual environment setup (recommended)

python -m venv venv


# Optional: dependencies install requirements.txt 
pip install -r requirements.txt




Linux / Mac:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt



# PassCheck

**PassCheck** is a simple educational Python tool to audit password strength and entropy.  
It checks whether a password is **Very Weak, Weak, Reasonable, Strong, or Very Strong**, detects common patterns, and provides advice to improve security.

> ⚠️ **Warning:** Only use this tool on passwords you own. Do **not** test other people's passwords.

---

## Features

- Entropy-based password strength measurement
- Detects common patterns (repeating chars, all digits, common passwords)
- Gives actionable advice to strengthen your password
- Continuous interactive mode (runs until you press Ctrl+C)
- One-time CLI mode with `-p` argument


---

## 🚀 Setup & Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SUBHO883/PassCheck.git
cd PassCheck

