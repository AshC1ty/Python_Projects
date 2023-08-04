import pyautogui as pa
import time

f=open("the_path_to_your_text_file","r")

print("a")
time.sleep(5)

"""If there is autocomplete for quotes, only then run the three loops else just typewrite"""
for i in f:
	for j in i:
		if j in ("(","{","["):
			pa.typewrite(j)
			pa.press("delete")
		else:
			pa.typewrite(j)
print("d")
