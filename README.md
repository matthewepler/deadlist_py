## Setup
* Make sure you have Python installed on your machine. For this workshop, we will be using Python 3. 

#### Mac Instructions
* Open Terminal. Run the command `python -v` to find out what version you have.

* To install Python 3, visit the [Python downloads](https://www.python.org/downloads/) page and download the installer. Open it and follow the instructions.
	* WINDOWS USERS: When you open the installer, be sure to check the box at the bottom of the install screen. It's the one that says "Add Python 3.5 to PATH." It should be checked. 

#### Windows Instructions
* Follow [these instructions](https://docs.python.org/3/using/windows.html)


## Basic Start, feat. Gilmore Girls
* Install Beautiful Soup: `pip3 install beautifulsoup4`

* First scrape:
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

baseURL = "http://www.reddit.com/r/GilmoreGirls"
html = urlopen(baseURL)
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify());
```

## Navigating the Tree 
* Review basic HTML structure
	* parents, children, siblings, descendents
* Show Inspector tools in Chrome
* How to find and scrape a tag
	* review [BS documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
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

* Navigating the tree using parents and siblings.
	* Here's some simple HTML as an example for these new functions:
	```html
		<div class="saucy">
		<a href="http://www.link.com">texty text</a>
		<ul>
			<li> list item #1 </li>
			<li> list item #2 </li>
		</ul>
	</div>
	```
	* And here are how we can use parents and siblings to navigate the tree:
	```python
	myTag = soup.a

	myTag.parent -> <div class="saucy">...</div>
	myTag.find_next_sibling('ul') -> <ul>...</ul>
	myTag.string -> 'texty text'
	```
* Suggested Strategy
	* 1. Find out what makes a show
	* 2. Get all the shows
	* 2b. Loop through all the shows
		* 3. Find out if the show has an encore (hint: use an 'if' statement to check for 'None')
		* 4. print encore data

* Something to get you started. If we were looking for 'Location' data instead, we might do it this way:
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

baseURL = "http://deadlists.com/deadlists/yearresults.asp?KEY=1972"
html = urlopen(baseURL)
soup = BeautifulSoup(html, 'lxml')

shows = soup.find_all('table', attrs={"width": 661})

for show in shows:
	location = show.find('font', text='Location')
	if location != None:
		loc_parent = location.parent 
		sibling = loc_parent.find_next_sibling('td')
		city = sibling.find('a').string
		print(city)
```
* a note about tables - you can skip the 'tbody' tag

## In-Class Assignments 
1. Write a different and/or shorter way to get to city from location. 

2. Print the city, date, of every encore ever played by the Grateful Dead.

	* Hint: you will need datetime to create proper dates
	```python
	import datetime
	date = datetime.date(year, month, day)
	date.strftime('%m/%d/%Y')
	```
* Extra Credit #1: add ability to scrape multiple years
* Extra Credit #2: scrape the direct link to the poster for each show with an encore

## Exporting to csv
```python
import csv

def writeToCSV(all_encores):
	# using 'with' will automatically close the file after the nested block of code
	with open('encores.csv', 'w') as csvfile:
		fieldnames = ['date', 'city']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		writer.writeheader()
		for encore in all_encores:
			writer.writerow(encore)

		print('file write complete!')
```

## Design
* What is your story
* What data will you need
* How will you display the data
	* [Basic data viz types](http://www.datavizcatalogue.com/)
* Sketch and scrape!



