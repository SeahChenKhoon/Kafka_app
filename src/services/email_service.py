from kafka import KafkaConsumer
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import src.library.util as util

env_variables = util.read_env()

consumer = KafkaConsumer(
    "user_created",
    bootstrap_servers=env_variables["bootstrap_server"],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id="email_service"
)
config_path = env_variables["config_path"]
sender_email = env_variables["sender_email"]
password = env_variables["password"]
config = util.load_config(config_path)

print("[EmailService] Listening for new user registrations...")

for message in consumer:
    event = message.value
    if event["event"] == "user_created":
        username = event["username"]
		
		# Sender and recipient
        receiver_email = event["email"]
        password = password
        # Create message
        message = MIMEMultipart("alternative")
        message["From"] = sender_email
        message["To"] = event["email"]

        message["Subject"] = config["subject"]

        # Email body (plain text + optional HTML)
        text = config["text_body"].replace("{{ username }}", event["username"])
        html = config["html_body"].replace("{{ username }}", event["username"])

        # Attach parts
        message.attach(MIMEText(text, "plain"))
        message.attach(MIMEText(html, "html"))

        # Send the email via Gmail SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
