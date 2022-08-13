import speech_recognition as sr
import os
import pyttsx3
import datetime
import webbrowser

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        
        with sr.Microphone() as source:
            audio.adjust_for_ambient_noise(source)   
            print("Estou ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz,language='pt-br')
            comando = comando.lower()
            if 'tina' in comando:
                comando = comando.replace('tina,""')
                print(comando)
                maquina.say(comando)
                maquina.runAndWait()
            
    except:
            print("Desculpe, não entendi.")
    
    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('No momento são' + hora)
        maquina.runAndWait()

    elif 'iniciar excel' in comando:
        os.system("start excel.exe")
        maquina.say('Abrindo excel')
        maquina.runAndWait()

    elif 'iniciar sap' in comando:
        os.system('C:\SAP.rdp')
        maquina.say('Abrindo SAP')
        maquina.runAndWait()

    elif 'iniciar mercado eletrônico' in comando:
        webbrowser.open("https://www.me.com.br/home")
        maquina.say('Abrindo mercado eletronico')
        print('Abrindo mercado eletronico')
        maquina.runAndWait()

comando_voz_usuario()