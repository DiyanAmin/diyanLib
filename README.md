# diyanLib 📦

A lightweight Python utility library by **Diyan Amin**, designed to simplify everyday coding tasks with reusable modules.  
Currently includes modules for **data handling**, with room to expand into math utilities, file operations, and more.

---

## ✨ Features
- Modular design — import only what you need.
- Easy to extend with new utilities.
- Clear, beginner‑friendly code structure.

---

## 📂 Project Structure
```text
diyanLib/
│
├── __init__.py        # Exposes modules
├── data.py            # Data storage & retrieval utilities
├── imports.py  # Data Science modules.
└── utils.py #Utility functions

And much more!
```

## Clone or copy into your Python Environment
```bash
git clone https://github.com/DiyanAmin/Tools---Utils
```

Path: `Python\Libs\site-packages`, copy this repositary as a folder and paste inside `site-packages` and import normally!

## Usage Examples

1. Store and retrieve data:
```python
import diyanLib

diyanLib.data.store('test.txt','Hello, world!') #Store data

print(diyanLib.data.retrieve('test.txt')) #Retrieve and print data
```

2. Working with data science and/or machine & deep learning
```python
from diyanLib.imports import * #Imports data science libraries with aliases except for keras and sklearn, from whom specific things are imported.
```

#

## 📖 Contributing
1. Fork the repository  
2. Add your module inside `diyanLib/`  
3. Update `__init__.py` to expose it  
4. Submit a pull request 🚀

---

## 🧑‍💻 Author
**Diyan Amin**  
GitHub: [DiyanAmin](https://github.com/DiyanAmin)

---

## 📜 License
MIT License — free to use, modify, and distribute.
