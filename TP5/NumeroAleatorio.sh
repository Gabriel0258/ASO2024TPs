#!/bin/bash
NumeroAleatorio=$(((RANDOM % 100) + 1))
echo "Bienvenido al juego del número escondido."
echo "Se generará un número aleatorio entre 1 y 100 y usted tiene que lograr encontrarlo."
echo "¡Buena Suerte!"
Coinciden=false
while ! $Coinciden; do
    echo -n "Ingrese un número: "
    read NumeroIngresado
    if ! [[ $NumeroIngresado =~ ^[0-9]+$ ]]; then
        echo "El valor ingresado no es válido, por favor intente de nuevo."
        continue
    fi
    if [ $NumeroIngresado -eq $NumeroAleatorio ]; then
        echo "¡Encontraste el número escondio!"
        Coinciden=true
    elif [ $NumeroIngresado -lt $NumeroAleatorio ]; then
        echo "El número escondido es más grande, vuelva a intentarlo."
    else
        echo "El número escondido es más chico, vuelva a intentarlo."
    fi
done