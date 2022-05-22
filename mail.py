import smtplib
department_lib={"water":"sit19cs040@sairamtap.edu.in","EB":"sit19cs030@sairamtap.edu.in"}
#department_name="current"
#message="No current in my area."
#number="+917845159519"

def mail_to_department(department,number,message):
    try: 
        #Create your SMTP session 
        smtp = smtplib.SMTP('smtp.gmail.com', 587) 

    #Use TLS to add security 
        smtp.starttls() 

        #User Authentication m
        smtp.login("meckendor@gmail.com","") #ask mukund r s for password

        #Defining The Message 
        message = "Respect Sir,\nThere has been a complaint \nMobile:"+number+"\nComplaint: "+message+".\nKindly do the needfull within 3 days.\n\nRegards,\nAutomated-Mail"

        #Sending the Email
        smtp.sendmail("meckendor@gmail.com", department_lib[department], message)

        #Terminating the session 
        smtp.quit() 
        print ("Email sent successfully!") 

    except Exception as ex: 
        print("Something went wrong....",ex)
