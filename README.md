# 🔐 Password Strength Checker (Streamlit + Python)

A Streamlit-based web application that evaluates the strength of a password using multiple security rules. The application provides real-time feedback and classifies passwords as Weak, Moderate, or Strong based on a scoring system.

---

## 🚀 Features

- Real-time password strength evaluation
- Regex-based validation logic
- Strength scoring system (0–5 scale)
- Dynamic UI feedback (Weak / Moderate / Strong)
- Clean and interactive Streamlit interface
- Secure password input field (hidden characters)

---

## 🛠 Tech Stack

- Python 3.x
- Streamlit
- Regular Expressions (`re` module)

---

## 🧠 How It Works

The application evaluates the password based on five security rules:

1. Minimum length of 8 characters  
2. Contains lowercase letters (a-z)  
3. Contains uppercase letters (A-Z)  
4. Contains numeric digits (0-9)  
5. Contains special characters (@, #, $, %, etc.)

Each satisfied condition increases the strength score by 1.

### Strength Classification:

- **0–2 → Weak ❌**
- **3 → Moderate ⚠️**
- **4–5 → Strong ✅**

The final score is displayed along with a visual status indicator.

---

## 📂 Project Structure

Password-Strength-Checker/  
│── project.py  
│── requirements.txt  
│── README.md  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/Fernandes-Samuel01/password-strength-checker.git

### 2️⃣ Navigate to Project Folder

cd password-strength-checker

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Run the Application

python -m streamlit run project.py

The application will open automatically in your browser.

---

## 🎯 Project Objective

The objective of this project is to demonstrate:

- Understanding of Python fundamentals  
- Implementation of conditional logic  
- Usage of regular expressions for pattern matching  
- Development of a web-based application using Streamlit  
- Clean UI/UX without writing HTML/CSS manually  

---

## 🔮 Future Improvements

- Add password generator feature  
- Add strength progress bar visualization  
- Provide password improvement suggestions  
- Add password history tracking (locally)  
- Deploy on Streamlit Cloud for public access  

---

## 👨‍💻 Author

Samuel Fernandes  
Software Development Intern  
