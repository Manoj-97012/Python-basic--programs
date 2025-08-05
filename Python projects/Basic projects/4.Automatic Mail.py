import smtplib

def automatic_email():
    user = input("Enter your Name >>: ")
    recipient_email = input("Enter your Email >>: ")

    subject = "Welcome!"
    body = f"Dear {user},\n\nYou are a good programmer!\nWelcome to TheCleverProgrammer!\n\nRegards,\nManoj"
    message = f"Subject: {subject}\n\n{body}"

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls() 
        sender_email = "akulama4@gmail.com"
        app_password = "xchp rncx uzxj mhi"
        s.login(sender_email, app_password)
        s.sendmail(sender_email, recipient_email, message)
        print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ Failed to send email. Error:", e)

    finally:
        s.quit()

automatic_email()
