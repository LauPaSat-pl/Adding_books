import time

import pyautogui
import pyperclip

import lubimy_czytac_site_handling


def open_adding_new_book():
	pyautogui.click(1700, 150)
	time.sleep(10)


def input_book_title(title="Nadeszło jutro, jak pandemia zmienia Europę"):
	pyautogui.click(378, 568)
	pyperclip.copy(title)

	time.sleep(.5)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(2)


def choose_category(category='Literatura'):
	# TODO: "add non book categories"

	pyautogui.click(250, 700)
	time.sleep(1.5)
	pyautogui.click(1042, 1097)
	time.sleep(0.25)
	pyautogui.click(987, 389)
	time.sleep(0.25)
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
	time.sleep(1)
	return 1


def choose_photos(photos=""):
	photos_list = photos.split(",")
	photos = ''

	for photo in photos_list:
		photo = photo.strip()
		photos += ('\"' + photo + '\" ')

	pyautogui.click(370, 1157)
	time.sleep(1)
	pyautogui.click(418, 620)
	pyperclip.copy(photos)
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(1)
	pyautogui.press('enter')

	time.sleep(2)


def enter_price(price=1000, negotiable=True):
	time.sleep(1)
	pyautogui.click(370, 1075)
	time.sleep(1)
	pyautogui.write(str(price))
	pyautogui.mouseInfo()
	if negotiable:
		pyautogui.click(678, 1165)
	time.sleep(1.5)


def enter_book_info(publishing_year=None, is_used=True, private_offer=True):
	time.sleep(0.25)

	if private_offer:
		pyautogui.click(291, 1340)
	else:
		pyautogui.click(556, 1340)

	pyautogui.press("pagedown")
	time.sleep(0.5)
	pyautogui.click(449, 282)
	if publishing_year is None:
		pyautogui.hotkey('ctrl', 'tab')
		time.sleep(0.25)
		if not lubimy_czytac_site_handling.search_for_a_book():
			return 0
		time.sleep(1)
		lubimy_czytac_site_handling.check_publication_date()
		pyautogui.hotkey('ctrl', 'tab')
		time.sleep(0.25)
		pyautogui.hotkey('ctrl', 'v')
	else:
		pyautogui.write(str(publishing_year))
	if is_used:
		pyautogui.click(291, 408)
	else:
		pyautogui.click(556, 402)
	time.sleep(1)


def add_description(desc=""):
	time.sleep(1)
	if desc != "":
		pass
	else:
		pyautogui.hotkey('ctrl', 'tab')
		time.sleep(0.25)
		if not lubimy_czytac_site_handling.check_if_book_found():
			return 0
		desc = lubimy_czytac_site_handling.get_desc()
		pyautogui.hotkey('ctrl', 'tab')

	footnote = '\n\nKontakt telefoniczny jedynie od poniedziałku do piątku w godzinach 19-21. Proszę NIE dzwonić poza tymi godzinami, bo nie odbieram, a często dodaję numer do blokowanych. Kontakt SMS-owy i na OLX dostępny całą dobę. \nOdbiór osobisty w Warszawie. Możliwa wysyłka zgodnie z cennikiem poczty polskiej lub paczkomatem + opakowanie. \nZapraszam również do moich innych ogłoszeń. Przy zakupach hurtem (powyżej 30 zł, przynajmniej trzy rzeczy) ZNIŻKA NAWET DO 10%. Przy zakupie kilku z moich ogłoszeń z przesyłką OLX proszę o informację na OLX, to stworzę ogłoszenie zbiorcze, żeby obniżyć koszty przesyłki.'
	full_desc = desc + footnote
	pyperclip.copy(full_desc)
	# pyautogui.press("pagedown")
	pyautogui.click(540, 644)
	pyautogui.hotkey('ctrl', 'v')
	return 1


def move_through_paying():
	time.sleep(5)
	pyautogui.press("pagedown")
	time.sleep(0.5)
	pyautogui.click(1474, 1219)
	time.sleep(5)


def add_shipping(size='A', weight=1):
	if size == 'A':
		pyautogui.click(420, 1219)
	elif size == 'B':
		pyautogui.click(920, 1219)
	elif size == 'C':
		pyautogui.click(1420, 1219)
	elif size == 'D':
		pyautogui.click(420, 1379)
	time.sleep(0.25)
	pyautogui.press("pagedown")
	time.sleep(0.25)
	if weight < 5:
		pyautogui.click(323, 672)
	elif weight < 20:
		pyautogui.click(500, 672)
	else:
		pyautogui.click(727, 672)
	time.sleep(0.25)

	pyautogui.click(331, 957)
	time.sleep(2)
	pyautogui.click(1699, 1257)
