from tkinter import *
from tkinter import filedialog
import smtplib
from email.message import EmailMessage

#Global variable
attachments = []

#Screen Init
master       = Tk()
master.title = 'Custom Email App'

#Functions
def attachFile():
    filename = filedialog.askopenfilename(initialdir='c:/',title='Please select a file')
    attachments.append(filename)
    notif.config(fg='green', text = 'Attached ' + str(len(attachments)) + ' files')
    
def send():
    try:
        msg      = EmailMessage()
        username = temp_username.get()
        password = temp_password.get()
        to       = temp_receiver.get()
        subject  = temp_subject.get()
        body     = temp_body.get()
        msg['subject'] = subject
        msg['from'] = username
        msg['to'] = to
        msg.set_content(body)

        filename = attachments[0]
        filetype = filename.split('.')
        filetype = filetype[1]
        if filetype == "jpg" or filetype == "JPG" or filetype == "png" or filetype == "PNG":
            import imghdr
            with open(filename, 'rb') as f:
                file_data = f.read()
                image_type = imghdr.what(filename)
            msg.add_attachment(file_data, maintype='image', subtype=image_type, filename=f.name)

        else:
            with open(filename, 'rb') as f:
                file_data = f.read()
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=f.name)
        
        if username=="" or password=="" or to=="" or subject=="" or body=="":
            notif.config(text="All fields required", fg="red")
            return
        else:
            server   = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            notif.config(text="Email has been sent successfully", fg="green")
    except:
        notif.config(text="Error sending email", fg="red")


def reset():
  usernameEntry.delete(0,'end')
  passwordEntry.delete(0,'end')
  receiverEntry.delete(0,'end')
  subjectEntry.delete(0,'end')
  bodyEntry.delete(0,'end')

#Label
Label(master, text="Custom Email App", font=('Calibri',15)).grid(row=0, sticky=N)
Label(master, text="Please use the form below to send an email", font=('Calibri',11)).grid(row=1, sticky=W, padx=5 ,pady=10)

Label(master, text="Email", font=('Calibri', 11)).grid(row=2,sticky=W, padx=5)
Label(master, text="Password", font=('Calibri', 11)).grid(row=3,sticky=W, padx=5)
Label(master, text="To", font=('Calibri', 11)).grid(row=4,sticky=W, padx=5)
Label(master, text="Subject", font=('Calibri', 11)).grid(row=5,sticky=W, padx=5)
Label(master, text="Body", font=('Calibri', 11)).grid(row=6,sticky=W, padx=5)
notif = Label(master, text="", font=('Calibri', 11),fg="red")
notif.grid(row=7,sticky=S)

#Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject  = StringVar()
temp_body     = StringVar()

#Entry
usernameEntry = Entry(master, textvariable = temp_username)
usernameEntry.grid(row=2,column=0)
passwordEntry = Entry(master, show="*", textvariable = temp_password)
passwordEntry.grid(row=3,column=0)
receiverEntry  = Entry(master, textvariable = temp_receiver)
receiverEntry.grid(row=4,column=0)
subjectEntry  = Entry(master, textvariable = temp_subject)
subjectEntry.grid(row=5,column=0)
bodyEntry     = Entry(master, textvariable = temp_body)
bodyEntry.grid(row=6,column=0)

#Tombol
Button(master, text = "Send", command = send).grid(row=7,   sticky=W,  pady=15, padx=5)
Button(master, text = "Reset", command = reset).grid(row=7,  sticky=W,  padx=45, pady=40)
Button(master, text = "Attachments", command = attachFile).grid(row=7,  sticky=W,  padx=90, pady=40)

#Main loop
master.mainloop()