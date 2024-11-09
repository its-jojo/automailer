import pyautogui as pg

name=input("Enter your name: ")
email=input("enter your email id:")
print("Dont press any key or move mouse ")
pg.sleep(1)
pg.hotkey("win","s")
pg.write("camera",interval=0.23)
pg.press("Enter")

pg.sleep(2)

pg.sleep(1)
pg.moveTo(1846,526,1)
pg.click()
pg.sleep(2)
pg.hotkey("win","1")

pg.sleep(2)

pg.hotkey("ctrl","t")
pg.sleep(1)
pg.write("mail")
pg.press("enter")
pg.sleep(7)
pg.moveTo(88,203,1)
pg.click()
pg.sleep(1)
pg.write(email,interval=0.05)
pg.press("enter")
pg.moveTo(1092,519)
pg.click()
pg.write("Hello ",interval=0.05)
pg.write(name,interval=0.10)
pg.write("  thank you for using my laptop",interval=0.08)

pg.sleep(1)

pg.moveTo(1314,1031)
pg.click()

pg.sleep(2)
pg.moveTo(1359,894)
pg.click()

pg.sleep(2)
pg.moveTo(114,666)
pg.click()
pg.sleep(1)
pg.moveTo(268,184)
pg.click()
pg.sleep(1)
pg.press("enter")
pg.sleep(1)
pg.sleep(2)
pg.hotkey("ctrl","enter")
pg.sleep(1)
pg.alert("Successfully mailed")



