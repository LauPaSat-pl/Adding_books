import sys

import pyautogui
import olx_site_handling as olx
import startup


def change_screen_resolution():
	# TODO: "check screen resolution, and adjust clicking points"
	pass


if __name__ == "__main__":
	list_of_items_to_sell = startup.set_up_environment()
	for item in list_of_items_to_sell:
		olx.open_adding_new_book()
		olx.input_book_title(item.title)
		olx.choose_category(item.category)
		olx.choose_photos(item.photos)

		pyautogui.mouseInfo()
	#  	pyautogui.press("pagedown")
	# 	olx.add_description(item.desc)
	# 	olx.enter_price(item.price, item.negotiable)
	# 	olx.enter_book_info(item.publishing_date)
	#
	# 	pyautogui.click(1695, 1433)
	#
	# 	olx.move_through_paying()
	# 	olx.add_shipping(item.size)
	# 	# pyautogui.hotkey('ctrl','w')
	# 	# pyautogui.hotkey('ctrl','w')
	# 	# pyautogui.hotkey('alt','f4')
	# 	# pyautogui.press("enter")
	# 	sys.exit()
