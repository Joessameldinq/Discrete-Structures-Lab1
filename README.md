# 🧩 Lab 1 – Logic, Quantifiers, and Number Operations

### **Course:** CSE214 – Discrete Mathematics

### **University:** Alexandria University

### **Faculty:** Engineering

### **Department:** Computer & Systems Engineering

### **Language:** Python


---

## 🎯 Learning Objectives

By the end of this lab, you will:
- Translate **logical quantifiers** into Python code.  
- Implement **basic number theory operations** (divisibility, gcd, modular arithmetic).  
- Understand **nested quantifiers** using nested loops in Python.  
- Learn to **comment and explain your logic** clearly in code.  
- Write small tests and analyze outputs.

---

## 🗂 Folder Contents

| File | Description |
|------|--------------|
| `lab1_(student_id).py` | Your main file. You must implement all functions and comment your logic. |
| `tests/` | Contains basic Pytest test cases. You can extend these if you wish. |
| `grader.py` | Optional: runs all tests automatically for you. |
| `README.md` | This instruction file (lab handout). |

---

## 🧠 Part 1 – Logic & Quantifiers

Implement:

| Function | Description |
|-----------|--------------|
| `check_universal(predicate, domain)` | Simulates ∀x in domain. Returns True only if all values satisfy the predicate. |
| `check_existential(predicate, domain)` | Simulates ∃x in domain. Returns True if at least one value satisfies the predicate. |
| `nested_quantifiers(predicate, domain_x, domain_y)` | Tests all four combinations: ∀x∀y, ∀x∃y, ∃x∀y, ∃x∃y. Returns a dictionary of results. |

💡 **Hint for Nested Quantifiers:**  
Think of it as **nested loops** in Python:
```python
for x in domain_x:
    for y in domain_y:
        # evaluate predicate(x, y)
```

---

## 🔢 Part 2 – Number Operations

Implement:

| Function | Description |
|-----------|--------------|
| `is_divisible(a, b)` | Returns True if b divides a. |
| `gcd(a, b)` | Computes the greatest common divisor (Euclidean algorithm). |
| `mod_equiv(a, b, m)` | Checks if a ≡ b (mod m). |
| `mod_exp(base, exp, mod)` | Computes base^exp % mod efficiently. |
| `is_prime(n)` | Returns True if n is a prime number. |

---

## 💬 Documentation Requirement (for both parts)

Each function **must contain comments** explaining:
1. **The logic or algorithm** you used.  
2. Any **special conditions or decisions** you made.  

---

## 🧪 Part 3 – Testing Your Code

Run your file directly to see its demo output:
```bash
python lab1_(student_id).py
```
Run tests (if you installed pytest):
> To install it you just need to run this in your terminal
> ```bash
> pip install pytest
> ```
```bash
pytest -q
```
or:
```bash
python grader.py
```

---

## 📌 Submission Rules

- Submit **only one file**: `lab1_(student_id).py` remove the brackets for example `lab1_12345678.py`
- Include your name and ID at the top of the file.
- Your file must run without syntax errors.
