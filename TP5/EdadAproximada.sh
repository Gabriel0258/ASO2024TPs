#!/bin/bash
echo -n "Ingrese un nombre para calcular la edad aproximada: "
read nombre
edad=$(curl -s "https://api.agify.io/?name=$nombre")
EdadAproximada=$(echo $edad | jq -r '.age')

if [ "$EdadAproximada" != "null" ]; then
    echo "La edad aproximada que hay para el nombre $nombre es de $EdadAproximada años."
else
    echo "No fue posible calcular la edad aproximada para el nombre $nombre."
fi