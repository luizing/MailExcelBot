import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import data.Variaveis as var

def send(destinatario, caminho):
    # Cria o cabeçalho do email
    msg = MIMEMultipart()
    msg['From'] = var.email
    msg['To'] = destinatario
    msg['Subject'] = "MailExcelBot"

    # Cria o corpo do email
    msg.attach(MIMEText('Arquivo enviado.', 'plain'))

    # Inserir anexo
    attachment = MIMEBase('application', 'octet-stream')
    with open(caminho, 'rb') as file:
        attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(caminho)}')
    msg.attach(attachment)

    try:
        # Conecta ao servidor smtp e envia o email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(var.email, var.senha)
            server.sendmail(var.email, destinatario, msg.as_string())
            print("Email enviado!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")


