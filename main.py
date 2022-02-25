import keyboard,time

time.sleep(5)
with open('bdd.py','r',encoding='UTF-8') as f:
    for line in f.readlines():
        keyboard.write(line, delay=0.01)
