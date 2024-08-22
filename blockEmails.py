import pandas as pd
import os

def block_email(data,blockEmail,blockedCsvPath):
    blocked_emails=[]
    if blockEmail in data['Email'].values:
        data=data[data['Email'] != blockEmail ]
        blocked_emails.append(blockEmail)

        data.to_csv("csvdata.csv",index=False)

           # Check if blocked emails CSV exists; if not, create it
        file_exists = os.path.isfile(blockedCsvPath)
        
        # Save the blocked email to a new or existing CSV file
        with open(blockedCsvPath, 'a') as f:
            if not file_exists:
                f.write("Blocked Email\n")
            for email in blocked_emails:
                f.write(f"{email}\n")
        print(f"Email {block_email} has benn blocked")

    else:
        print(f"Email {block_email} not found in the csv")





data=pd.read_csv(r"C:\Users\hp\Desktop\csvdata.csv")
print(data)
blockEmail=input()
blockedCsvPath=r"C:\Users\hp\Desktop\BlockedEmail.csv"

block_email(data,blockEmail,blockedCsvPath)

