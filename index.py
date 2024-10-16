from tkinter import *
import numpy as np  



def check_for_phishing(content):
    pass

def send_email():
    pass

root = Tk()
root.title("Simulated Phishing Email Detector")

# Recipient email details
Label(root, text="Recipient Email (Placeholder):").grid(row=0, column=0)
recipient_entry = Entry(root, width=40)
recipient_entry.grid(row=0, column=1)
recipient_entry.insert(0, "test@placeholder.com")  # Using a placeholder email

# Email subject
Label(root, text="Subject:").grid(row=1, column=0)
subject_entry = Entry(root, width=40)
subject_entry.grid(row=1, column=1)

# Email content
Label(root, text="Content:").grid(row=2, column=0)
content_text = Text(root, height=10, width=40)
content_text.grid(row=2, column=1)

# Send button
send_button = Button(root, text="Send Email", command=send_email)
send_button.grid(row=3, column=1)

# Status label to show the phishing detection result
status_label = Label(root, text="")
status_label.grid(row=4, column=1)

root.mainloop()