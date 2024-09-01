#Email Validator : This project validates the email addresses.

#correct formats
#deepika9782@gmail.com
#w@gmail.com
#wn@gmail.com
#deepikaprolifics@gmail.in
#w@w.in

#wrong formats
#123deepika@gmail.com
#deepika 123@gmail.com
#Anana@gmail.com
#vennela@34@gmail.com




email = input("Enter your Email: ") # to take email as an input
s,u,sc = 0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1 ):
           if (email[-4] == ".") or (email[-3] == "."):
               for i in email:
                   if i == i.isspace():
                       s=1
                   elif i.isalpha():
                       if i==i.upper():
                           u=1
                   elif i.isdigit():
                       continue
                   elif i == "_" or i=="." or i=="@":
                       continue
                   else:
                       sc=1
               if s==1 or u==1 or sc==1:
                    print("Wrong Email 5")
               else:
                   print("Correct Email ")
           else:
                print("Wrong Email 4")
            
        else:
            print("Wrong Email 3")
        
    else:
       print("Wrong Email 2") 
else:
    print("Wrong Email 1")
    
