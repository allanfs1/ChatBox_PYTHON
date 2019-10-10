import pyttsx3


def main ():
    speak = pyttsx3.init('sapi5')
    while True:
        phrase = input("Entre com um Texto:")
        speak.say(phrase)
        speak.runAndWait()

main()
