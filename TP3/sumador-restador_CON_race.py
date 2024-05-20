import time
import threading


acumulador = 0


def sumador():
    global acumulador

    for _ in range(1000):
        tmp = acumulador

        time.sleep(0)
        tmp = tmp + 5
        time.sleep(0)

        acumulador = tmp


def restador():
    global acumulador

    for _ in range(1000):
        tmp = acumulador

        time.sleep(0)
        tmp = tmp - 5
        time.sleep(0)

        acumulador = tmp


hilo1 = threading.Thread(target=sumador)
hilo2 = threading.Thread(target=restador)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()


print(f'El valor calculado final es: {acumulador}')