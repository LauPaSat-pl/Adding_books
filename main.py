import time

import pyautogui

import olx_site_handling as olx
import startup

if __name__ == "__main__":
	list_of_items_to_sell = startup.set_up_environment()
	for item in list_of_items_to_sell:
		olx.input_book_title(item.title)
		olx.choose_category(item.category)
		olx.choose_photos(item.photos)

		pyautogui.press("pagedown")
		olx.add_description(item.desc)
		olx.enter_price(item.price, item.negotiable)
		pyautogui.press("pagedown")
		olx.enter_book_info(item.publishing_date)
		olx.add_shipping(item.size)
		pyautogui.hotkey('ctrl', 'w')
		time.sleep(0.5)
		pyautogui.hotkey('ctrl', 't')
		time.sleep(0.5)
		pyautogui.write("https://www.olx.pl/d/nowe-ogloszenie/?bs=homepage_adding")
		pyautogui.press("enter")
		time.sleep(10)
