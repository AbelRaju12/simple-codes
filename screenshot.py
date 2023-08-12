import pyscreenshot as py
import time

n = int(input("Enter after how lng you want to take the screenshot: "))

time.sleep(n)

image = py.grab()

image.show()

# image.save("screenshot/ss.png")
