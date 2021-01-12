#!/usr/bin/env python
# coding: utf-8

# In[3]:


import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)# smtp session
s.starttls() # security
s.login("akhilrmogulla@gmail.com","ohkrhgkhifmhabcx")#sender mail.id
msg=input("enter ur message")
s.sendmail("akhilrmogulla@gmail.com","akashreddymogulla@gmail.com",msg)
s.quit()


# In[ ]:




