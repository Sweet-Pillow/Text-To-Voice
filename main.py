import pyttsx3
import PySimpleGUI as sg


class Aplicacao:
    def __init__(self):

        sg.theme('DarkAmber')
        
        # Layout
        self.layout = [
            [sg.Text('Discurso'), sg.Input()],
            [sg.Button('Falar')]
        ]

        # Janela
        self.janela = sg.Window(title='Dados do Usuário').layout(self.layout)

    def Iniciar(self):
        while True:
            event, self.values = self.janela.read()
            if event == sg.WIN_CLOSED:
                break

            speak.say(self.values[0])
            speak.runAndWait()
            print(self.values[0])

if __name__ == '__main__':

    # Defining the engine 
    speak = pyttsx3.init('sapi5')
    voices = speak.getProperty("voices")
    for voice in voices:
        print(voice.id, voice.name, voice.languages)

    speak.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0")
    speak.setProperty("rate", 120)
    speak.setProperty("volume", 1.)

    tela = Aplicacao()
    tela.Iniciar()
