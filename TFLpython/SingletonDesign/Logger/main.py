class Logger :

    __instance = None

    def __new__(cls):

        if cls.__instance is None:
            print("Creating the Logger...")
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        pass

    def logs():
        print("Logger is loging in...!")
        return 0

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)