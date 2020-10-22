import bs4, requests, smtplib

# ------------------- E-mail list ------------------------
toAddress = ['example@domain.com','example2@domain.com']
# --------------------------------------------------------

#Download page
getPage = requests.get('https://www.example-domain.com')
getPage.raise_for_status() #if error it will stop the program

#Parse text for products
menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
products = menu.select('.model')

the_one = 'phrase' # This is the name of the product you are looking for
flength = len(the_one)
available = False

for product in products:
    for i in range(len(product.text)):
        chunk = product.text[i:i+flength].lower()
        if chunk == the_one:
            available = True

if available == True:
    conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.login('yourmail@gmail.com', 'app_password')
    conn.sendmail('yourmail@gmail.com', toAddress, 'Subject: Product Found!\n\nAttention!\n\nYour product is available today!\n\nHave a nice day!:\nProduct Notifier V1.0')
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
    for i in range(len(toAddress)):
        print(toAddress[i])
    print('')
else:
    print('Your product is not available today.')