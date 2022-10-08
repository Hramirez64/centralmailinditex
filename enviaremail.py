from email.message import EmailMessage
import smtplib

def enviar_email(email_destino,codigo):
    remitente = "uninorte2132gr7@outlook.es"
    destinatario = email_destino
    mensaje = "Codigo de Activacion: "+ codigo
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Codigo de Activacion"
    email.set_content(mensaje, subtype="html")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "Inditex_g7")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()


def recuperar_email(email_destino):
    remitente = "uninorte2132gr7@outlook.es"
    destinatario = email_destino
    mensaje = "<h2>Correo de Restablecimiento de Contraseñas</h2>"
    mensaje=mensaje+ "<a href='https://centralmensajesinditec.herokuapp.com/restablecer/"+email_destino+"'>Click para Restablecer la contraseña</a>"
    mensaje=mensaje+"<hr>"
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Recuperar Contraseña"
    email.set_content(mensaje, subtype="html")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "Inditex_g7")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()
    