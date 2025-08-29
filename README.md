# cyfertool
Cyfertool

### `README.md`

````markdown
# Sequential GUID Generator

This tool generates **sequentially incremented/decremented GUIDs** (UUIDs) based on a provided base GUID.  
It is useful for **testing IDOR vulnerabilities, fuzzing APIs, and exploring predictable UUID sequences**.

---

## 🚀 Features
- Generate a list of sequential GUIDs around a **base GUID**.
- Customizable **count** (default = 50).
- Save results to a file for use in fuzzers.
- `--only-guids` mode for clean wordlist generation (perfect for ffuf, Burp, wfuzz, etc.).
- Lightweight, no dependencies.

---

## 📦 Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/sequential-guid-generator.git
cd sequential-guid-generator
````

No external dependencies are required — it runs on pure Python 3.

---

## ⚡ Usage

### Generate and Print

```bash
python3 sequential_guid_generator.py --guid 00000000-0000-0000-033f-9cb227550081 --count 20
```

### Generate and Save to File

```bash
python3 sequential_guid_generator.py --guid 00000000-0000-0000-0342-ab857e74c03a --count 100 --out guids.txt
```

### Generate Wordlist for Fuzzing

```bash
python3 sequential_guid_generator.py --guid 00000000-0000-0000-033f-9cb227550081 --count 200 --only-guids > wordlist.txt
```

Result (`wordlist.txt`):

```
00000000-0000-0000-033f-9cb227550051
00000000-0000-0000-033f-9cb227550052
00000000-0000-0000-033f-9cb227550053
...
```

This file can now be used directly with:

```bash
ffuf -w wordlist.txt -u https://target/api/resource/FUZZ
```

---

### Options

* `--guid` / `-g`: Base GUID (required)
* `--count` / `-c`: Number of sequential GUIDs to generate (default: 50)
* `--title` / `-t`: Custom title for output section
* `--out` / `-o`: Save results to a file
* `--only-guids`: Print **only GUIDs** (no index/title) for use in fuzzers

---

## 🔐 Security Note

This script is intended for:

* **Educational purposes**
* **Testing predictable UUID implementations**
* **Penetration testing with proper authorization**

⚠️ Do **not** use this tool on systems you don’t have explicit permission to test.

---

## 📜 License

MIT License © 2025 Fcyfer


```

