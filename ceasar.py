#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Instrucciones:
# Ejecutar desde consola e ingresar texto y clave de desplazamiento
# despues ingresar cadena a decifrar y misma de desplazamiento


abc = 'abcdefghijklmnopqrstuvwxyz,..?:; !'

def cifrar(cadena, clave):

    text_cifrado = ''

    for letra in cadena:
        suma = abc.find(letra) + clave
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])
       # print suma
       # print modulo
       # print text_cifrado

    return text_cifrado

def decifrar(cadena, clave):

    text_cifrado = ''

    for letra in cadena:
        suma = abc.find(letra) - clave
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])

    return text_cifrado

def main():
    c = str(raw_input('cadena a cifrar: ')).lower()
    n = int(raw_input('clave numerica 0-32: '))
    print cifrar(c,n)
    cc = str(raw_input('cadena a decifrar: ')).lower()
    cn = int(raw_input('clave numerica 0-32: '))
    print decifrar(cc,cn)

if __name__ == '__main__':
    main()
