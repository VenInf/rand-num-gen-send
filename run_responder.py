from lib.prng import PRNG
import logging

class Responder:
    """
    Wrapper for answering given commands
    """

    def __init__(self):
        self.generator = PRNG()

        formatter = logging.Formatter("[%(message)s]")
        file_handler = logging.FileHandler("controller.log", mode="a", encoding="utf-8")
        file_handler.setFormatter(formatter)
        self.logger = logging.getLogger()
        self.logger.addHandler(file_handler)
        self.logger.setLevel("INFO")

        self.logger.info("responder: init")

    def eval_loop(self):
        while True:
            command = input()
            self.logger.info(f"responder: received command <{command}>")

            match command:
                case "Hi":
                    ans = "Hi"
                    self.logger.info(f"responder: send {ans}")
                    print(ans)

                case "GetRandom":
                    ans = self.generator.get_random()
                    self.logger.info(f"responder: send {ans}")
                    print(ans)

                case "Shutdown":
                    break


if __name__ == "__main__":
    r = Responder()
    r.eval_loop()
