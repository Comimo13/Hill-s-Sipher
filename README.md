# 🔐 Hill's Sipher (NumPy-based)

A modular implementation of the Hill Cipher encryption algorithm using Python and NumPy. WARNING ,IT'S LEARNING PROJECT 

---

## 📌 Features

- Multi-language support (Latin, Cyrillic, Arabic, etc.)
- Modular encryption pipeline
- Matrix-based encryption using NumPy
- Automatic padding for uneven input lengths
- Clean separation of encryption components

---

## 🧠 How it works

1. Text is converted into numeric vectors
2. Text is split into fixed-size blocks
3. Blocks are multiplied by a key matrix (K)
4. Results are converted back into characters using modular arithmetic

---

Install dependencies:

```bash
pip install numpy