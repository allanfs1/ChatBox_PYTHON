import  speech_recognition as sr

r = sr.Recognizer()


def main(args):
      with sr.Microphone() as s:
        r.adjust_for_ambient_noise(s)
      while True:
          audio = r.listen(S)
          speech = recognize_google(audio,languagem= 'pt')
          print("voce disse:",speech)

if __name__ == '__main__':
     import sys
     sys.exit(main(sys.argv))
