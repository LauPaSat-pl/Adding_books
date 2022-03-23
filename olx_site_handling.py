import time

import pyautogui
import pyperclip

import lubimy_czytac_site_handling


def input_book_title(title:str):
	"""
	Function to enter book title
	:param title: Title of the book
	"""
	pyautogui.click(378, 568)
	pyperclip.copy(title)

	time.sleep(.5)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(2)


def choose_category(category='Literatura'):
	"""
	Function to choose book category
	:param category: Category to be chosen
	"""
	# TODO: add non book categories

	pyautogui.click(250, 700)
	time.sleep(1.5)
	pyautogui.click(1011, 1156)
	time.sleep(1)
	pyautogui.click(1020, 379)
	time.sleep(1)
	if category == 'Literatura':
		pyautogui.click(1567, 400)
	elif category == 'Czasopisma':
		pyautogui.click(1567, 500)
	elif category == 'Dla dzieci':
		pyautogui.click(1567, 600)
	elif category == 'Komiksy':
		pyautogui.click(1567, 650)
	elif category == 'Książki naukowe':
		pyautogui.click(1567, 750)
	elif category == 'Podręczniki szkolne':
		pyautogui.click(1567, 850)
	elif category == 'Poradniki i albumy':
		pyautogui.click(1567, 900)
	elif category == 'Pozostałe':
		pyautogui.click(1567, 1000)
	else:
		return 0
	time.sleep(5)
	return 1


def choose_photos(photos: str):
	"""
	Function to choose photos of the book
	:param photos: Name of the photos, separated by commas
	:return:
	"""
	if photos == '':
		print("No photos of the book")
		return 0
	photos_list = photos.split(",")
	photos = ''

	for photo in photos_list:
		photo = photo.strip()
		photos += ('\"' + photo + '\" ')

	pyautogui.click(370, 1157)
	time.sleep(1)
	pyautogui.click(575, 920)
	pyperclip.copy(photos)
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(1)
	pyautogui.press('enter')

	time.sleep(2)
	return 1


def enter_price(price=1000, negotiable=True):
	"""
	Function to enter price of the book and if the price is negotiable
	:param price: Price in PLN
	:param negotiable: if negotiable
	"""
	time.sleep(1)
	pyautogui.click(370, 1075)
	time.sleep(1)
	pyautogui.write(str(price))
	if negotiable:
		pyautogui.click(735, 1231)
	time.sleep(1.5)


def enter_book_info(publishing_year=None, is_used=True, private_offer=True):
	"""
	Function to enter basic info about the book
	:param publishing_year: Publishing year of the book
	:param is_used: If the book is used
	:param private_offer: Is it private or business offer
	"""
	time.sleep(0.25)

	if private_offer:
		pyautogui.click(291, 312)
	else:
		pyautogui.click(556, 312)

	time.sleep(0.5)
	pyautogui.click(433, 417)
	if publishing_year is not None:
		pyautogui.write(str(publishing_year))
	if is_used:
		pyautogui.click(291, 548)
	else:
		pyautogui.click(556, 548)
	time.sleep(1)


def add_description(desc=""):
	"""
	Function to enter description of the book
	:param desc: Description. If empty will get description from lubimyczytac.pl
	:return: 1 - if the description was added
	"""
	time.sleep(1)
	if desc == "":
		pyautogui.hotkey('ctrl', 'tab')
		time.sleep(0.25)
		if not lubimy_czytac_site_handling.search_for_a_book():
			return 0
		desc = lubimy_czytac_site_handling.get_desc()
		pyautogui.hotkey('ctrl', 'tab')

	footnote = '\n\nKontakt telefoniczny jedynie od poniedziałku do piątku w godzinach 19-21. Proszę NIE dzwonić poza tymi godzinami, bo nie odbieram, a często dodaję numer do blokowanych. Kontakt SMS-owy i na OLX dostępny całą dobę. \nOdbiór osobisty w Warszawie. Możliwa wysyłka zgodnie z cennikiem poczty polskiej lub paczkomatem + opakowanie. \nZapraszam również do moich innych ogłoszeń. Przy zakupach hurtem (powyżej 30 zł, przynajmniej trzy rzeczy) ZNIŻKA NAWET DO 10%. Przy zakupie kilku z moich ogłoszeń z przesyłką OLX proszę o informację na OLX, to stworzę ogłoszenie zbiorcze, żeby obniżyć koszty przesyłki.'
	full_desc = desc + footnote
	pyperclip.copy(full_desc)
	pyautogui.click(540, 644)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(0.25)
	return 1


def add_shipping(size='A', weight=1):
	"""
	Function to choose Przesyłka OLX options
	:param size: Size of the book
	:param weight: Weight of the book
	"""
	if size == 'A':
		pyautogui.click(400, 1014)
		time.sleep(0.5)
		if weight < 5:
			pyautogui.click(300, 1150)
			time.sleep(0.5)
			pyautogui.click(300, 1250)
			time.sleep(0.5)
			pyautogui.click(300, 1350)
		elif weight < 25:
			pyautogui.click(300, 1250)
	elif size == 'B':
		pyautogui.click(271, 1219)
		pyautogui.press("pagedown")
		time.sleep(0.5)
		if weight < 10:
			pyautogui.click(300, 200)
			time.sleep(0.5)
			pyautogui.click(300, 300)
			time.sleep(0.5)
			pyautogui.click(300, 400)
		elif weight < 25:
			pyautogui.click(300, 300)
	elif size == 'C':
		pyautogui.click(271, 1319)
		pyautogui.press("pagedown")
		time.sleep(0.5)
		if weight < 20:
			pyautogui.click(300, 350)
			time.sleep(0.5)
			pyautogui.click(300, 450)
			time.sleep(0.5)
			pyautogui.click(300, 550)
		elif weight < 25:
			pyautogui.click(300, 350)
			time.sleep(0.5)
			pyautogui.click(300, 300)
	time.sleep(0.5)
	pyautogui.press("end")
	time.sleep(0.5)

	pyautogui.click(1800, 460)
	time.sleep(1.5)
