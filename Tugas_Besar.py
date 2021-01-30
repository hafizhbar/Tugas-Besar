#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# In[2]:


fromaddr = "hfz216@gmail.com"
toaddr = 'ridwanluthfiyah@gmail.com'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ini hanya sebuah percobaan"


# In[3]:


body = "Semoga Bisa\n""Semoga Bisa\n""Semoga Bisa"
msg.attach(MIMEText(body, 'plain'))


# In[4]:


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "PASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


# In[ ]:




