## Setup
* check for Windows machines, install Python, check for pip

* Install Homebrew: 
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
* check with command `brew doctor`. If broken use [this page](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos)

* Install python3: `brew install python3`

* Install Beautiful Soup: `pip3 install beautifulsoup4`

## Basic Start, feat. Gilmore Girls
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

baseURL = "http://www.reddit.com/r/GilmoreGirls"
html = urlopen(baseURL)
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify());
```

## Navigating the Tree - REPL
* Review basic HTML structure
	* parents, children, siblings, descendents
* Show Inspector tools in Chrome
* how do I get a tag 
	* review BS documentation
  * soup.head
  * soup.head['title']
  * soup.head.title
  * soup.head.title.string
  * soup.div
  * soup.find('div')
  * soup.find_all('div')
  * soup.find('div', 'thing')
  * posts = soup.find_all('div', attrs={'data-author': True})
  	* len(posts)
* going down the tree
	* contents
	* children
	* descendents
* navigating in other directions

* ASSIGNMENT: print the number of posts on the page

## Scrape the Dead!
* [Deadlists](http://deadlists.com/deadlists/yearresults.asp?KEY=1972)
* [data specifications](http://www.deadlists.com/dlsite/dataspec.html)
* [abbreviations table](http://deadlists.com/deadlists/symbols.htm)

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

baseURL = "http://deadlists.com/deadlists/yearresults.asp?KEY=1972"
html = urlopen(baseURL)
soup = BeautifulSoup(html, 'lxml')

shows = soup.find_all('table', attrs={"width": 661})

for show in shows:
	location = show.find('font', text='Location')
	loc_parent = location.parent 
	sibling = loc_parent.find_next_sibling('td')
	city = sibling.find('a').string
	print(city)
```

* a note about tables - you can skip the <tbody>

## In-Class Assignments 
* a different and/or shorter way to get to city from location. 
* Share results

* Print the city, date (numbers only), of every encore ever played by the Grateful Dead.

	* intro to datetime
	```python
	import datetime
	date = datetime.date(year, month, day)
	date.strftime('%m/%d/%Y')
	```
* WORK+: do it for more than one year
* WORK++: add the poster image for each encore show (requires the src attribute of the poster's img tag)

* Exporting to csv

## Design
* What is your story
* What data will you need
* How will you display the data
	* [Basic data viz types](http://www.datavizcatalogue.com/)
* Sketch and scrape!



