# -*- coding: utf-8 -*-
import random

#crea el abecedario y lo pone en una lista
def alphabet():
    abcd=list(map(chr, range(32, 127)))
    return abcd

#crea la llave de cifrado y la pone en una lista
def createKey():
    abcd=alphabet()
    criptographicKey=list(abcd)
    noRepeted=[random.randint(0,94)]
    for i in range(0,len(criptographicKey),1):
        criptographicKey[i]=abcd[assigment(noRepeted)]
    return criptographicKey

#debido a que se utiliza el comando random las letras se repiten
#esta funcion evita letras repetidas en la llave de cifrado
def assigment(noRepeted):
    if len(noRepeted)<95:
        repeted=0
        assig=random.randint(0,94)
        for i in range(0,len(noRepeted),1):
            if noRepeted[i]==assig:
                repeted+=1
                break
        if repeted==0:
            noRepeted.append(assig)
            return assig
        else:
            return assigment(noRepeted)
    else:
        return 0

#cifra el mensaje
def cypher(msg_lst,abcd,criptographicKey):
    encriptedMsg=[]
    for i in range(0,len(msg_lst),1):
        for j in range(0,len(abcd),1):
            if msg_lst[i]==abcd[j]:
                encriptedMsg.append(criptographicKey[j])
                break
    print('\nCypher message:\n\t', end='')
    print(''.join(encriptedMsg))
    return encriptedMsg

#descifra el mensaje
def Decypher(encriptedMsg,RealKey,abcd):
    deEncriptedMsg=[]
    for i in range(0,len(encriptedMsg),1):
        for j in range(0,len(RealKey),1):
            if encriptedMsg[i]==RealKey[j]:
                deEncriptedMsg.append(abcd[j])
                break
    print('Decypher message:\n\t', end='')
    print(''.join(deEncriptedMsg))
    return deEncriptedMsg

def run():
    #password
    MASTER_KEY='PLATZI'

    #genera el abcdario
    abcd=list(alphabet())
    #genera la llave de cifrado real
    RealKey=createKey()

    msg=str(input('\nType the massage:'))
    msg_lst=list(msg)

    print('\nMessage:\n\t', end='')
    print(''.join(msg_lst))

    #si ingresas el password incorrecto se crea una llave de
    #cifrado falsa y no podras volver a descifrar el msj
    ask_master_key=str(input('\nPassword:'))
    if MASTER_KEY==ask_master_key:
        criptographicKey=list(RealKey)
    else:
        criptographicKey=createKey()

    #cifrar
    encriptedMsg=cypher(msg_lst,abcd,criptographicKey)

    #descifrar
    print('\nDecyphering...')
    input()
    deEncriptedMsg=Decypher(encriptedMsg,RealKey,abcd)

if __name__=='__main__':
    run()