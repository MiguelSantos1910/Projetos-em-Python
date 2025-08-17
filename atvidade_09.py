import os
import time
contador_m = 0
contador_s = 0
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    contador_s += 1
    clear()
    print(f"{contador_m}:{contador_s}")
    time.sleep(1)
    if contador_s == 59:
        contador_m = 1
        contador_s = 0
        clear()
        print(f"{contador_m}:{contador_s}")
    if contador_m == 1:
        if contador_s == 28:
            clear()
            print(f"{contador_m:}:{contador_s}")
            break
