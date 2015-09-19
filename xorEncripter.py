#la llave puede ser alfanumerica, numerica o solo alfabetica
#la llave se ingresa en un string que soporta espacion y caracteres especiales
#el algoritmo sirve para encriptar y desencriptar
#losAmo #bestTeamEver #friends
def crypt(textoPlano, key):
    key_len = len(key)#tamaño de cada caracter
    key = [ord(character) for character in key]#saca el valor de cada caracter
    textoPlano = [ord(caracter) ^ key[index % key_len] for (index, caracter) in enumerate(textoPlano)]#xor entre el texto que se esta insertando y la llave, se enumera el texto plano para darle un valor
    return ''.join([chr(character_valor) for character_valor in textoPlano])#concatena los resultados y los muestra como un string
