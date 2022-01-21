from django.shortcuts import render
from email.mime.text import MIMEText
import smtplib
import pandas as pd
from django.http import HttpResponse
def data(request):
    return render(request,'mail_portal.html')
def sendmail(request):
    print("Called function")
    a=request.POST['msg']
    print(a)
    msg=MIMEText(a)
    fromaddr=request.POST['uname']
    pw=request.POST['psw']
    data=pd.read_csv('emails.csv').values.tolist()
    toaddr=['']
    for i in range(0,len(data)):
        toaddr.append(str(data[i][1]))
    toaddr.remove('')
    msg['From']=fromaddr
    msg['subject']=request.POST['sub']
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromaddr,pw)
    server.sendmail(fromaddr,toaddr,msg.as_string())
    server.quit()
    return HttpResponse('Mail sent')


# from django.shortcuts import render
# import smtplib
# from email.mime.text import MIMEText
# from django.http import HttpResponse

# def sendmail(request):
#     try: 
#         #Create your SMTP session 
#         smtp = smtplib.SMTP('smtp.gmail.com', 587) 

#         #Use TLS to add security 
#         smtp.starttls() 

#         #User Authentication 
#         smtp.login("abhishekpatra0709@gmail.com","abhisha177")

#         #Defining The Message 
#         message = "Message_you_need_to_send" 

#         #Sending the Email
#         smtp.sendmail("abhishekpatra0709@gmail.com", "isha.panchal17@gmail.com",message) 

#         #Terminating the session 
#         smtp.quit() 
#         return HttpResponse('Mail sent')

#     except Exception as ex: 
#         return HttpResponse('Mail not sent')
    

# # Create your views here.
