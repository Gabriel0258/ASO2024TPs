import time


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


sumador()
restador()


print(f'El valor calculado final es: {acumulador}')