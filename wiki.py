from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3

speak = pyttsx3.init('sapi5')
# Create a new chat bot named Charlie
# Create a new ChatBot instance
bot = ChatBot(
    'Allan',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://localhost:27017/chat'
)

print('Cnexao sucesso begin...')


trainer = ListTrainer(bot)

trainer.train([

   "Oi, posso ajudá-lo?",
    "Claro, eu gostaria de reservar um voo para a Islândia.",
    "O seu voo foi reservado.",
    "Bom Dia",
    "Como vai você",
    "Tudo Bem?",
    "Qual eo seu nome?"
    "Eu gostaria de saber com voce estar hoje?",
    "Queria te conhecer melhor",
    "na intimidade?",
    "E mesmo",
    "Vamos para outro lugar",
    "como você estar se vestindo Hoje?",
    "Quantos ano você tem",
    "voçê e legal",
    "Gostei de você",
    "A onde você mora?"
])


# Get a response to the input text 'I would like to book a flight.'
# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)
        bot_response = bot.get_response("conta")
        print(bot_response)


        fala = bot_response
        speak.say(fala)
        speak.runAndWait()

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
