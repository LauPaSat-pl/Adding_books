import time
import pyautogui

import to_sell_class


def set_up_environment():
	start_opera()
	a = create_list_of_items_to_sell()
	time.sleep(5)
	return a

def start_opera():
	pyautogui.press("winleft")
	time.sleep(0.5)
	pyautogui.write("Opera")
	time.sleep(0.5)
	pyautogui.press("enter")
	time.sleep(2.5)
	pyautogui.write("lubimyczytac.pl")
	pyautogui.press("enter")
	time.sleep(0.5)
	pyautogui.hotkey("ctrl", 't')
	time.sleep(0.5)
	pyautogui.write("olx.pl")
	pyautogui.press("enter")


def create_list_of_items_to_sell():
	with open("books_to_be_added.txt", 'r', encoding='utf8') as file:
		to_sell = file.readlines()

	list_to_sell = [0] * len(to_sell)

	for item in range(len(list_to_sell)):
		data = to_sell[item].split(";")
		for i in range(len(data)):
			data[i] = data[i].strip()


		if len(data[0]) < 14 or len(data[0]) > 70:
			with open("errors.txt", 'a', encoding='utf8') as file:
				file.write(f"Book {data[0]} has too short/long title. Fix it and try again\n")
		else:
			list_to_sell[item] = to_sell_class.ToSell(data[0], data[2], data[1], data[3], data[4], data[5], data[6], data[7])
	print(list_to_sell)
	return list_to_sell
