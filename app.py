import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formataddr
import os

def send_emails(sender_email, sender_password, sender_name, subject, body, to_list, attachment_path=None):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        for recipient in to_list:
            msg = MIMEMultipart()
            msg["From"] = formataddr((sender_name, sender_email))
            msg["To"] = recipient.strip()
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            if attachment_path and os.path.exists(attachment_path):
                with open(attachment_path, "rb") as f:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}")
                    msg.attach(part)

            server.sendmail(sender_email, recipient.strip(), msg.as_string())

        server.quit()
        return True, "✅ Emails sent successfully!"

    except Exception as e:
        return False, f"❌ Error: {str(e)}"


# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="📧 Multi Email Sender", page_icon="📨", layout="centered")
st.title("📧 Bulk Email Sender")
st.write("Send personalized emails with attachments to multiple recipients easily.")

# Form for better state handling
with st.form("email_form", clear_on_submit=True):  
    sender_email = st.text_input("Your Email (Gmail recommended)")
    sender_password = st.text_input("App Password", type="password")
    with st.expander("❓ How to get a Google App Password"):
        st.markdown("""
        - Go to your [Google Account Security Settings](https://myaccount.google.com/security).
        - Enable **2-Step Verification**.
        - Then create an **App Password** under the "App passwords" section.
        - Use this instead of your normal Gmail password.
        """)
    sender_name = st.text_input("Your Name (as it should appear)")
    subject = st.text_input("Email Subject")
    body = st.text_area("Email Body", height=300, placeholder="Type your cover letter or message here...")
    recipients_input = st.text_area("Recipients (one per line or comma separated)", height=100)
    attachment = st.file_uploader("Upload PDF Attachment", type=["pdf"])

    submitted = st.form_submit_button("📨 Send Emails")

if submitted:
    recipients = []
    if recipients_input:
        recipients = [r.strip() for r in recipients_input.replace(",", "\n").split("\n") if r.strip()]

    if not (sender_email and sender_password and sender_name and subject and body and recipients):
        st.error("⚠️ Please fill all required fields and add at least one recipient.")
    else:
        # Save uploaded attachment temporarily
        attachment_path = None
        if attachment:
            attachment_path = os.path.join("temp_" + attachment.name)
            with open(attachment_path, "wb") as f:
                f.write(attachment.read())

        success, message = send_emails(
            sender_email, sender_password, sender_name, subject, body, recipients, attachment_path
        )

        if success:
            st.success(message)
        else:
            st.error(message)

        # Cleanup temp file
        if attachment_path and os.path.exists(attachment_path):
            os.remove(attachment_path)

# ---------------------------
# Footer / Watermark
# ---------------------------
st.markdown(
    """
    <p style='text-align: center; color: gray; font-size: 12px;'>
        Created by Nuwantha Lakshan
    </p>
    """,
    unsafe_allow_html=True
)