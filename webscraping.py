from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwizod3NmqbtAhWKQEEAHQPoAeEQPAgI")
soup = bs(r.content)
print(soup)
