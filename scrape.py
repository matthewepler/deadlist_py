# Scraper for www.deadlists.com
# Matthew Epler, 2016 
# matthewepler@gmail.com


from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import csv

# baseURL = "http://www.reddit.com/r/GilmoreGirls/"
baseURL = "http://deadlists.com/deadlists/yearresults.asp?KEY=1972"
html = urlopen(baseURL)
soup = BeautifulSoup(html, 'lxml')
all_encores = []


def writeToCSV(all_encores):
	# using 'with' will automatically close the file after the nested block of code
	with open('encores.csv', 'w') as csvfile:
		fieldnames = ['date', 'city']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		writer.writeheader()
		for encore in all_encores:
			writer.writerow(encore)

		print('file write complete!')



# GG ASSIGNMENT: print the number of posts on the page
# posts = soup.find_all('div', attrs={'data-author': True})
# print(len(posts))



shows = soup.find_all('table', attrs={"width": 661})

for show in shows:
	# location = show.find('font', text='Location')
# 	loc_parent = location.parent 
# 	sibling = loc_parent.find_next_sibling('td')
# 	city = sibling.find('a').string
# 	print(city)
	# city = location.find_next('td').a.string
	
	# date = show.find('font', text='Date')
	# date_str = date.find_next('td').font.string
	# digits = date_str.split(' - ')[0].split('/')
	# if len(digits[2]) == 2:
	# 	digits[2] = "19" + digits[2]
	# date_obj = datetime.date(int(digits[2]), int(digits[0]), int(digits[1]))
	# date_formated = date_obj.strftime('%m/%d/%Y')
	
	encore = show.find('font', text='Encore')
	if encore != None:
		played = encore.find_next('font').string
		
		location = show.find('font', text='Location')
		city = location.find_next('td').a.string
		date = show.find('font', text='Date')
		date_str = date.find_next('td').font.string
		digits = date_str.split(' - ')[0].split('/')
		if len(digits[2]) == 2:
			digits[2] = "19" + digits[2]
		date_obj = datetime.date(int(digits[2]), int(digits[0]), int(digits[1]))
		date_formated = date_obj.strftime('%m/%d/%Y')

		# print('Encore! {}, @ {}'.format(date_formated, city))

		all_encores.append({
				'date': date_formated,
				'city': city
			})

	else:
		# print('No Encore :(')
		continue

writeToCSV(all_encores)



