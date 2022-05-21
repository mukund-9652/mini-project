import smtplib 
try: 
    #Create your SMTP session 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 

   #Use TLS to add security 
    smtp.starttls() 

    #User Authentication 
    smtp.login("sit19cs040@sairamtap.edu.in","Mukundrs2905!")

    #Defining The Message 
    message = "Message_you_need_to_send" 

    #Sending the Email
    smtp.sendmail("sender_email_id", "receiyer_email_id",message) 

    #Terminating the session 
    smtp.quit() 
    print ("Email sent successfully!") 

except Exception as ex: 
    print("Something went wrong....",ex)
