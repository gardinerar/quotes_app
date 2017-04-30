from bs4 import BeautifulSoup
import requests

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "c9_django.settings")

import django
django.setup()
from polls.models import Quotes

page = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
soup = BeautifulSoup(page.content, 'html.parser')

quote_class = soup.find_all('div', class_="bqcpx")[0:5]
quote_tag = range(0, len(quote_class))
quote_text = range(0, len(quote_class))

for i in xrange(0,len(quote_class)):
	quote_tag[i] = quote_class[i].find('a')
	quote_text[i] = quote_tag[i].contents[0]
	print(quote_text[i])

for i in xrange(0, len(quote_class)):
    Quotes.objects.get_or_create(quote_text=str(quote_text[i]))

