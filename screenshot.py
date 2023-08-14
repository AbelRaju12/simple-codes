import time
import pyscreenshot as py #imports time and screesnhot modules

n = int(input("Enter after how lng you want to take the screenshot: "))

time.sleep(n)

image = py.grab()

image.show()

# image.save("screenshot/ss.png")
