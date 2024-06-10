import threading
import time

done = False

def worker():
    count = 0
    while done != "b":
        time.sleep(1)
        count += 1
        print(count)

threading.Thread(target=worker).start()

while done != "para":
    done = input("Informe uma letra: ")
