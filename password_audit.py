# password_audit.py
# Simple educational password strength and entropy checker.
# Use this to test passwords you own. Do NOT test other people's passwords.

import math
import argparse
import getpass
import re

def estimate_charset_size(pw: str) -> int:
    size = 0
    if re.search(r'[a-z]', pw): size += 26
    if re.search(r'[A-Z]', pw): size += 26
    if re.search(r'[0-9]', pw): size += 10
    if re.search(r'[^A-Za-z0-9]', pw): size += 32  # rough for symbols
    return size if size > 0 else 1

def entropy_bits(pw: str) -> float:
    charset = estimate_charset_size(pw)
    return len(pw) * math.log2(charset)

def strength_label(bits: float) -> str:
    if bits < 28:
        return "Very weak"
    if bits < 36:
        return "Weak"
    if bits < 60:
        return "Reasonable"
    if bits < 80:
        return "Strong"
    return "Very strong"

def common_patterns(password: str):
    patterns = []
    if password.lower() in ("password", "123456", "qwerty"): patterns.append("Very common password")
    if re.search(r'(.)\1\1', password): patterns.append("Repeating characters")
    if re.search(r'^\d+$', password): patterns.append("All digits")
    if re.search(r'^[a-z]+$', password): patterns.append("All lowercase letters")
    if re.search(r'^[A-Z]+$', password): patterns.append("All uppercase letters")
    return patterns

def audit(password: str):
    bits = entropy_bits(password)
    label = strength_label(bits)
    patterns = common_patterns(password)
    advice = []
    if len(password) < 8: advice.append("Make it at least 12 characters.")
    if not re.search(r'[A-Z]', password): advice.append("Add uppercase letters.")
    if not re.search(r'[a-z]', password): advice.append("Add lowercase letters.")
    if not re.search(r'[0-9]', password): advice.append("Add digits.")
    if not re.search(r'[^A-Za-z0-9]', password): advice.append("Add symbols (e.g. !@#$%).")
    if re.search(r'\s', password): advice.append("Avoid spaces.")
    if bits < 60: advice.append("Consider using a long passphrase (3–5 uncommon words).")
    return {
        "length": len(password),
        "entropy_bits": round(bits, 2),
        "label": label,
        "patterns": patterns,
        "advice": advice
    }

def run_interactive():
    print("Password Audit Tool (press Ctrl+C to exit)\n")
    try:
        while True:
            pw = getpass.getpass("Enter password to audit: ")
            result = audit(pw)
            print(f"\nLength: {result['length']}  Entropy: {result['entropy_bits']} bits  => {result['label']}")
            if result['patterns']:
                print("Patterns detected:", ", ".join(result['patterns']))
            if result['advice']:
                print("\nAdvice:")
                for a in result['advice']:
                    print(" -", a)
            else:
                print("\nLooks good! Use a password manager to store complex passwords.\n")
            print("-" * 50 + "\n")
    except KeyboardInterrupt:
        print("\nExiting... Goodbye!")

def main():
    parser = argparse.ArgumentParser(description="Password audit tool (educational).")
    parser.add_argument("-p", "--password", help="Password to audit (not recommended on CLI).")
    args = parser.parse_args()

    if args.password:
        pw = args.password
        result = audit(pw)
        print(f"\nLength: {result['length']}  Entropy: {result['entropy_bits']} bits  => {result['label']}")
        if result['patterns']:
            print("Patterns detected:", ", ".join(result['patterns']))
        if result['advice']:
            print("\nAdvice:")
            for a in result['advice']:
                print(" -", a)
        else:
            print("\nLooks good! Use a password manager to store complex passwords.\n")
    else:
        run_interactive()

if __name__ == "__main__":
    main()
