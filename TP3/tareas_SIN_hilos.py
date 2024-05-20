import time


def tarea_1():
    momento_arranque = time.perf_counter()
    print('Inicio tarea 1')

    for x in range(100000000):
        pass

    print('Fin tarea 1')
    momento_parada = time.perf_counter()

    print(f'Tomó {momento_parada - momento_arranque: 0.5f} segundos completar la tarea 1')


def tarea_2():
    momento_arranque = time.perf_counter()
    print('Inicio tarea 2')
    time.sleep(1)
    print('Fin tarea 2')
    momento_parada = time.perf_counter()

    print(f'Tomó {momento_parada - momento_arranque: 0.5f} segundos completar la tarea 2')


def tarea_3():
    momento_arranque = time.perf_counter()
    print('Inicio tarea 3')
    time.sleep(4)
    print('Fin tarea 3')
    momento_parada = time.perf_counter()

    print(f'Tomó {momento_parada - momento_arranque: 0.5f} segundos completar la tarea 3')


momento_arranque = time.perf_counter()
tarea_1()
tarea_2()
tarea_3()
momento_parada = time.perf_counter()


print(f'Tomó un total de{momento_parada - momento_arranque: 0.5f} segundos completar todas las tareas')