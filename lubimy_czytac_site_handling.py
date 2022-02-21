import re
import time

import pyautogui
import pyperclip
import requests


def search_for_a_book():
	pyautogui.press('home')
	time.sleep(0.25)
	pyautogui.click(1443, 200)
	time.sleep(0.25)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(2.5)
	pyautogui.click(1443, 300)
	time.sleep(2)
	return check_if_book_found()


def check_publication_date():
	pyautogui.click(825, 1029)
	time.sleep(1)
	pyautogui.moveTo(1015, 1083)
	time.sleep(0.25)
	pyautogui.mouseDown()
	pyautogui.drag(39, 0)
	pyautogui.mouseUp()
	time.sleep(0.25)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.25)


def get_desc():
	pyautogui.click(1445, 66)
	pyautogui.click(1445, 66)
	pyautogui.hotkey('ctrl', 'c')
	full_site_text = requests.get(pyperclip.paste())

	desc_regex = re.compile(r'<div class="collapse-content">\n\s+<p>\s+(.+\s)+</p>')
	raw_desc = desc_regex.search(full_site_text.text)

	raw_desc = raw_desc.group()[50:-4]
	raw_desc = raw_desc.strip()
	raw_desc = raw_desc.replace("<br />", "")

	print(raw_desc)
	return raw_desc


def check_if_book_found():
	pyautogui.click(1445, 66)
	pyautogui.hotkey('ctrl', 'c')
	website = pyperclip.paste()
	print(website)
	if website == "https://lubimyczytac.pl/mapaksiegarn":
		print("Book not found")
		return 0
	return 1
