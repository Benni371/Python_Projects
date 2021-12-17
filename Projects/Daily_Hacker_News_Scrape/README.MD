# Daily Hacker News #
This python script is used to grab the most recent/popular article from https://news.ycombinator.com/news . The script uses the Beautiful Soup python library to search
throught the site and find the first `<td>` that has specific details about the article. The script will then scrape the conents and return them. The contents are then 
filtered through for the articles title and the hyperlink that leads to the article. These details are then sent as an email using a gmail account to another email account

## Set up ## 
Set up is pretty basic. Clone/Download the `scraper.py` file however you would like. After it is in a folder, you will have to install the following libraries if you
do not already have them:
- `bs4` (Beautiful Soup)
- `requests` (Used for getting the html)
- `python-decouple` (Used for the `env` to hide email credentials)
**Note: if you have the normal `decouple` library you will have to uninstall it. Otherwise the script may not grab the correct library.**. 
Before you setup the `env` file you will need to either create a gmail account or modify a current gmail so that it has developer tools enabled. For a tutorial on how to 
do that refer to this [article](https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development). There is probably another way to do it with 
other email services but I like google so thats what I'll use for the setup.  
  
  
After the libraries are installed and the gmail account is setup, you will have to create a `.env` file to store your email credentials. The `env` file should look like this:  
```python
email = "<put the gmail account that is sending the email>"
password = "<put the password to the sending gmail account>"
receiver = "<put the email account that will receive the email. It could be the same as the sender if you would like>"
```
  
**Important: If you are going to push this to github make sure you include a `.gitignore` file and then add the `.env` file to it. That way your credentials are not
pushed to github**  
  
Once all of this is setup, you should be good to go! Happy Scraping!  
  
## References ##
[Sending Emails with Python](https://realpython.com/python-send-email/)
[Web Scraping Basics](https://www.youtube.com/watch?v=XVv6mJpFOb0)
