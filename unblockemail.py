import pandas as pd
import os

def unblock_email(email_to_unblock, csvdata_path, blocked_csv_path):
    # Load the CSV files
    data = pd.read_csv(csvdata_path)
    blocked_emails = pd.read_csv(blocked_csv_path)

    # Check if the email to unblock is in the blocked CSV
    if email_to_unblock in blocked_emails['Email'].values:
        # Get the details of the email to unblock
        email_details = blocked_emails[blocked_emails['Email'] == email_to_unblock]
        
        # Remove the email from the blocked emails DataFrame
        blocked_emails = blocked_emails[blocked_emails['Email'] != email_to_unblock]
        
        # Append the email details back to the main data DataFrame
        data = pd.concat([data, email_details], ignore_index=True)
        
        # Save the updated data to csvdata.csv
        data.to_csv(csvdata_path, index=False)
        
        # Save the updated blocked emails CSV
        blocked_emails.to_csv(blocked_csv_path, index=False)

        print(f"Email {email_to_unblock} has been unblocked and restored.")
    else:
        print(f"Email {email_to_unblock} not found in the blocked emails list.")

# Paths to the CSV files
csvdata_path = r"C:\Users\Siddhartha\Downloads\csvdata.csv"
blocked_csv_path = r"C:\Users\Siddhartha\Downloads\BlockedEmail.csv"

# Email to unblock (from user input or another source)
email_to_unblock = input("Enter the email to unblock: ")

# Call the function to unblock the email
unblock_email(email_to_unblock, csvdata_path, blocked_csv_path)
