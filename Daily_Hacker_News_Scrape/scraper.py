from bs4 import BeautifulSoup
import requests
from decouple import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl




def get_news():
    #web scrape first article from hacker news .com
    article = ''
    response = requests.get('https://news.ycombinator.com/front')
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    tag = soup.find('a',attrs={"class":"titlelink"})
    tag = str(tag)
    parsed = tag.split('"')
    link = parsed[3]
    parsed = tag.split('>')
    title = parsed[-2].split("<")
    title = title[0]
    # Gener
    news = {
        "Title": title,
        "Link": link
    }
    return(news)


def send_news(news):
    
    msg = MIMEMultipart()

    msg['Subject'] = 'Daily Hacker News'
    body = f"{news['Title']}: {news['Link']}"
    msg.attach(MIMEText(body, 'html')) 

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = str(config('email')) #get sender email from env
    password = str(config('password')) #get password from env
    receiver_email = str(config('receiver'))


    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email,msg.as_string() )
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 



news = get_news()
send_news(news)
