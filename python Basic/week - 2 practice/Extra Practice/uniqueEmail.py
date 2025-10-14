with open("emails.txt",'r+') as file:
    content = file.read().strip().split("\n")
    emails = [email.lower() for email in content]
    uniqueEmails = sorted(list(set(emails)))

with open("unique_emails.txt",'w') as file:
    for email in uniqueEmails:
        file.write(f"{email}\n")