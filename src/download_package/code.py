import requests
import os
import urllib.request
from bs4 import BeautifulSoup
import datetime


url = ''

def which_years():
	"""
	Returns those years for which data is available

	Parameters
	----------

	Returns
	-------
	list
		a list of strings representing the years for which data is available
	"""

	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	years = []
	for i in range(len(soup.find_all('a'))-6):
		years.append(soup.find_all('a')[5+i].get_text()[0:-1])

	for i in years:
		print(i,end="\t")

	return years


def which_months(select_year):
	"""
	Returns those years for which data is available

	Parameters
	----------
	select_year: int

	Returns
	-------
	list
		a list of strings representing the months for which data is available in the given year
	"""


	# errors handling
	assert (len(str(select_year)) == 4 and type(select_year) == int), "Year must be a 4-digit integer."
	
	# if this function returns None, then it means there is no data for the year
	
	select_year_str = str(select_year)
	while True:
		try:
			if(select_year_str in which_years()):
				break
		except:
		# executed if which_years() hasn't been called before
			return None
			
	# following code is executed only if break occurs in the if conditions above
	url_year = url + select_year_str + '/'
	page = requests.get(url_year)
	soup = BeautifulSoup(page.content, 'html.parser')
	months = []
	for i in range(len(soup.find_all('a'))-5):
		months.append(soup.find_all('a')[5+i].get_text()[0:-1])

	for i in months:
		print(i,end="\t")
		
	return months 


def which_days(select_year, select_month):
	"""
	Returns those days for which data is available in the given month and year

	Parameters
	----------
	select_year: int
	select_month: int
	
	Returns
	-------
	list
		a list of strings representing the days for which data is available in the given month and year
	"""

	# errors handling
	assert (len(str(select_year)) == 4 and type(select_year) == int), "Year must be a 4-digit integer."
	assert (select_month >= 1 and select_month <=12 and type(select_month) == int), "Month must be a valid number."
	
	# if this function returns None, then it means there is no data for the month in a given year
	
	if select_month < 10:
		select_month_str = '0'+str(select_month)
	else:
		select_month_str = str(select_month)
	select_year_str = str(select_year)
	
	while True:
		try:
			if(select_month_str in which_months(select_year)):
				break
			else:
				# when the given year doesn't have data for the given month
				return None
		except:
			# when the given year doesn't have any data 
			return None
		
	url_month = url + select_year_str + '/' + select_month_str + '/'
	page = requests.get(url_month)
	soup = BeautifulSoup(page.content, 'html.parser')
	days = []
	
	for i in range(len(soup.find_all('a'))-5):
		days.append(soup.find_all('a')[5+i].get_text()[0:-1])

	for i in days:
		print(i,end='\t')	
	return days



def which_instruments(select_year, select_month, select_day):
	"""
	Returns those days for which data is available in the given month and year

	Parameters
	----------
	select_year: int
	select_month: int
	select_day: int
	
	Returns
	-------
	list
		a list of strings representing the instrument/location IDs for which data is available in the given date
	"""

	if select_month < 10:
		select_month_str = '0'+str(select_month)
	else:
		select_month_str = str(select_month)
	select_year_str = str(select_year)
	if select_day < 10:
		select_day_str = '0'+str(select_day)
	
	# errors handling
	try:
		select_date = datetime.date.fromisoformat('{}-{}-{}'.format(select_year_str, select_month_str, select_day_str))
	except ValueError:
		raise ValueError("The date combination in which_instruments() is invalid") from None 
	
	assert (select_date <= datetime.date.today()), "The date combination in which_instruments() has not yet occurred"
	url_day = url + select_year_str + '/' + select_month_str + '/' + select_day_str + '/'
	page = requests.get(url_day)
	soup = BeautifulSoup(page.content, 'html.parser')
	assert ('404 Not Found' not in soup), "No data for the selected date"
	print('asdf')
	ids = []
	for i in range(len(soup.find_all('a'))-5): # SLOW
		id_temp = soup.find_all('a')[5+i].get_text().split('_')[0] + "_" + soup.find_all('a')[5+i].get_text().split('_')[-1][0:2]
		if(id_temp not in ids):
			ids.append(id_temp)

	for i in ids:
		print(i,end="\t")

	return ids




