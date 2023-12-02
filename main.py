import smtplib
import datetime as dt
import pandas as pd
from random import randint

file = pd.read_csv("birthdays.csv")
df = pd.DataFrame(file)

name = df.name.iloc[0]
email = df.email.iloc[0]
year = df.year.iloc[0]
month = df.month.iloc[0]
day = df.day.iloc[0]
birthday = (year, month, day)
now = dt.datetime.now()

if birthday == (now.year, now.month, now.day):
    letter_no = randint(1, 3)
    with open(f"letter_templates/letter_{letter_no}.txt", "r") as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", name)

    my_email = "[*YOUR EMAIL]"
    password = "[*YOUR PASSWORD]"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
        