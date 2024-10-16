from tkinter import *
import numpy as np  
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
clf=Pipeline([
    ('vectorizer',CountVectorizer()),
    ('nb',MultinomialNB())
])

emails=[
    'Sounds great! Are you home now?',
    'Will u meet ur dream partner soon? Is ur career off 2 a flyng start? 2 find out free, txt HORO followed by ur star sign, e. g. HORO ARIES',
    'will we be ok'
]



data=pd.read_csv('./spam.csv')
data['Spam']=data['Category'].apply(lambda x:1 if x=='spam' else 0)
X_train,X_test,y_train,y_test=train_test_split(data.Message,data.Spam,test_size=0.25)
clf.fit(X_train,y_train)





def check_for_phishing(content):
    arr = [content]
    sc = clf.predict(arr)
    print(sc)
    return sc

def send_email():
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    content = content_text.get("1.0", END)
    phishing_result = check_for_phishing(content)
    res_string  = "Phishing Detected"
    if(phishing_result == 0): res_string = "Phishing Not Detected"
    status_label.config(text=f"Email to {recipient} with subject '{subject}'\nDetection Result: {res_string}", fg="green")

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