import re
import time

import pyautogui
import pyperclip


def search_for_a_book():
	pyautogui.press('home')
	time.sleep(0.25)
	pyautogui.click(1567, 400)
	time.sleep(0.25)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(2.5)
	pyautogui.click(1443, 470)
	time.sleep(5)
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
	pyautogui.hotkey('ctrl', 'u')
	time.sleep(5)
	pyautogui.hotkey('ctrl', 'a')
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'w')

	full_site_text = pyperclip.paste()
	raw_desc = full_site_text.split('<div class="collapse-content">')[1].split('</div>')[0]

	raw_desc = raw_desc.replace("<br />", "").replace("<p>", "").replace("</p>", "")
	raw_desc = raw_desc.strip()

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
