import pyautogui
import time

num=int(pyautogui.prompt(text='ESCOLHA UM NUMERO PARA REPETIÇÃO: ', title='ELEFANTE' , default=''))

elefante=1
elefante_mais=2
cont=0

pyautogui.alert(text='APÓS CLICAR EM "OK" TERÁ 5 SEGUNDOS PARA SELECIONAR A CAIXA DE TEXTO', title='ELEFANTE', button='OK')
time.sleep(5)

while cont<num:
    
    if(elefante==1):
        elefante=str(elefante)
        elefante_mais=str(elefante_mais)
        texto=elefante+' ELEFANTE INCOMODA MUITA GENTE, '+elefante_mais+' ELEFANTES INCOMODAM MUITO MAIS'
        elefante=int(elefante)
        elefante_mais=int(elefante_mais)
    else:
        elefante=str(elefante)
        elefante_mais=str(elefante_mais)
        texto=elefante+' ELEFANTES INCOMODAM MUITA GENTE, '+elefante_mais+' ELEFANTES INCOMODAM MUITO MAIS'
        elefante=int(elefante)
        elefante_mais=int(elefante_mais)


    pyautogui.typewrite(texto)
    pyautogui.press('enter')
    # time.sleep(0.1)

    elefante+=1
    elefante_mais+=1
    cont+=1



