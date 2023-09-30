import smtplib

my_email = "alintxxipython@gmail.com" # *xKFQF3iJE:u)2W1k.j,,N10apQhaV
password = "jnwxzrbemsckbxxu"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="appbrewerytesting@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )