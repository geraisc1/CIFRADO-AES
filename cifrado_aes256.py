#importacion de las librerias necesarias

from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
#libreria time para que el progrma espere un timepo antes de terminar y cerrarlo.
import time

#codigo por funciones

#creacion de la clase ecriptar la cual contine los procesos a realizar.
class Encryptor:
#funciones del codigo.
    def __init__(self, key):
        self.key = key
#funcion para el tipo de crifrado.

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

#funcion para encriptar.

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

#funcion encriptar archivo

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()

        #Agregamos la extencion con la cual queremos que se genere el archivo cifrado.

        aes = self.encrypt(plaintext, self.key)
        with open(file_name + ".aes", 'wb') as fo:
            fo.write(aes)
        os.remove(file_name)

#Funcion para decifrar el archivo y cvolverlo a la extencion original .txt

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

#Generacion de las llaves que validan la entrada de el usuario para cifrar/decifrar el archivo.

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
aes = Encryptor(key)
clear = lambda: os.system('cls')

#uso de condicionales if, while, else, para dar una estructura controlada a el resto del codigo.

#if es donde se genera el archivo  cifrado de la llave 

if os.path.isfile('data.txt.aes'):
    while True:

        #Digitamos la contraseña que introducimos al inicio del cifrado para validar que sea correcta.

        #En esta seccion accedemos a desifrar el archivo hola.txt
        password = str(input("DIgite el password: "))
        aes.decrypt_file("data.txt.aes")
        p = ''
        with open("data.txt", "r") as f:
            p = f.readlines()
        if p[0] == password:
            #llave publica
            aes.encrypt_file("data.txt")
            #Asignamos el nombre del archivo que deseamos cifrar/decifrar.
            aes.decrypt_file("hola.txt.aes")
            break

#Asignamos un while para digitar la opcion salir y que el programa termine.

    while True:
        
        choice = int(input("PRESIONE '3 'PARA SALIR:"))
        if choice == 3:
            exit()
        
else:
    while True:

         # Esta seccion en donde introducimos la contraseña para cifrar.*****

        clear()
        password = str(input("Ingrese una password: "))

        #Validacion de contraseña: El usuario tendra que volver a digitar la contrasela para corraborar que sean iguales.

        repassword = str(input("Confirmar password: "))
        if password == repassword:
            #Mnandamos llamar la funcion para encrptar el archivo hola.txt
            aes.encrypt_file("hola.txt")
            break

            #Control de errores de la contraseña en caso que no pasen por el primer if o validacion.
        else:
            print("contrasenas no coinciden")
    f = open("data.txt", "w+")
    f.write(password)
    f.close()
    aes.encrypt_file("data.txt")
    #Aqui es donde se usa la libreria time  darle un tiempo de espera al programa pra que cierre.
    print("Espere un momento....")
    time.sleep(9)

