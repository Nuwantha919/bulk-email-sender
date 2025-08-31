# 📧 Bulk Email Sender (Streamlit + Python)

A simple and user-friendly **Streamlit web app** to send emails (with optional PDF attachments) to multiple recipients at once.  
This project uses **Python, Streamlit, and Gmail App Passwords** for secure authentication.

---

## 🚀 Features
- Send emails to **multiple recipients** (comma or line-separated).
- Attach a **PDF file** (e.g., CV, cover letter, or reports).
- Secure authentication using **Google App Passwords**.
- Easy-to-use web interface with **Streamlit**.
- Inline help on **how to generate a Google App Password**.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Streamlit** – for the UI
- **smtplib** – for sending emails
- **email.mime** – for attachments and formatting

---

## 📂 Project Structure

bulk-email-sender

│── app.py              # Main Streamlit application

│── requirements.txt    # Python dependencies

│── README.md           # Project documentation

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/multi-email-sender.git
   cd multi-email-sender
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt

streamlit run app.py

## 🔑 Getting Your Google App Password

Gmail does not allow direct login with your account password when using SMTP.
Instead, you must generate a 16-digit App Password.

Follow these steps:

Go to Google Account Security
.

Enable 2-Step Verification (if not already enabled).

Under App Passwords, create a new password.

Select Mail as the app and Windows Computer (or "Other") as the device.

Copy the 16-character password shown and use it in this app.

<img width="936" height="926" alt="image" src="https://github.com/user-attachments/assets/b9ec8ed1-8e1e-428d-b6e2-f1a1441b6861" />



## ⚠️ Disclaimer

This project is for educational and personal use only.

Do not use it for spamming or sending unsolicited emails.

Sending bulk unsolicited emails may violate Google’s policies and local laws.

The authors are not responsible for misuse of this tool.

## ❤️ Contributing

Feel free to fork this repo, submit issues, or create pull requests.
Suggestions and improvements are always welcome!
