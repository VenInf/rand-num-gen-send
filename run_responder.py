from lib.prng import PRNG


class Responder:
    """
    Wrapper for answering given commands
    """

    def __init__(self):
        self.generator = PRNG()

    def eval_loop(self):
        while True:
            command = input()
            match command:
                case "Hi":
                    print("Hi")
                case "GetRandom":
                    print(self.generator.get_random())
                case "Shutdown":
                    break


if __name__ == "__main__":
    r = Responder()
    r.eval_loop()
