import nltk

def builtinEngines(whichOne):
    if whichOne == 'eliza':
        nltk.chat.eliza.demo()
    elif whichOne == 'iesha':
        nltk.chat.iesha.demo()
    elif whichOne == 'rude':
        nltk.chat.rude.demo()
    elif whichOne == 'suntsu':
        nltk.chat.suntsu.demo()
    elif whichOne == 'zen':
        nltk.chat.zen.demo()
    else:
        print("알 수 없는 내장 채팅 엔진 {}".format(whichOne))

def myEngine():
    chatpairs = (
        (r"(.*?)Stock price(.*)",
            ("Today stock price is 100",
            "I am unable to find out the stock price.")),
        (r"(.*?)not well(.*)",
            ("Oh, take care. May be you should visit a doctor",
            "Did you take some medicine ?")),
        (r"(.*?)raining(.*)",
            ("Its monsoon season, what more do you expect ?",
            "Yes, its good for farmers")),
        (r"How(.*?)health(.*)",
            ("I am always healthy.",
            "I am a program, super healthy!")),
        (r".*",
            ("I am good. How are you today ?",
            "What brings you here ?"))
    )
    def chat():
        print("!"*80)
        print(" >> 내 엔진 << ")
        print("일반 영어로 프로그램과 대화")
        print("="*80)
        print("완료되면 'quit' 입력")
        chatbot = nltk.chat.util.Chat(chatpairs, nltk.chat.util.reflections)
        chatbot.converse()

    chat()

if __name__ == '__main__':
    for engine in ['eliza', 'iesha', 'rude', 'suntsu', 'zen']:
        print("=== {} 데모 ===".format(engine))
        builtinEngines(engine)
        print()
    myEngine()
