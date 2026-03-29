# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

##################### Extra Hard Starting Project Functions ######################

def send_email(email, letter):
    my_email = 'wdavern@gmail.com'
    # This is for gmail
    app_password = "iysj adhq xton czjf" #input('Enter your password: ')
    # Put the subject in the first part of the message with 2 line breaks
    messy = letter.encode('ascii', errors='ignore')
    mess = messy.decode('utf-8')
    message = f"Subject:Hello from Bills Python\n\n{mess}"
    print(f"the message is {message.strip()}")
    to_email = email
    # When using with you don't need to do a connection.close()
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=my_email,to_addrs=to_email, msg=message)

def get_letter(row):
    name = row[0]
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    letter = f"letter_templates/{choice(letters)}"
    message = ""
    try:
        with open(letter, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if line.endswith('[NAME],\n'):
                    print("Inside line.endwith")
                    message += line.replace('[NAME]', name)
                else:
                    message += line
        return message

    except FileNotFoundError:
        print("Couldn't find {letter} file")
        return False


def main():
    now = dt.datetime.now()
    day = now.day
    month = now.month

    with open('birthdays.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            # If today is someones birthday, send them an email!
            if int(row[3])  == int(month) and int(row[4]) == int(day):
                message = get_letter(row)
                send_email(row[1], message)

if __name__ == '__main__':
    main()
