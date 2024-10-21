from subprocess import PIPE, Popen
from statistics import mean, median
import logging


class Controller:
    """
    Controller, that runs a given python program
    in a separate process and interacts with it using STDIO
    """

    def __init__(self, responder):
        self.responder = responder
        self.process = Popen(
            ["python", "-u", responder],
            stdin=PIPE,
            stdout=PIPE,
            bufsize=0,
            universal_newlines=True,
        )

        formatter = logging.Formatter("[%(message)s]")
        file_handler = logging.FileHandler("controller.log", mode="a", encoding="utf-8")
        file_handler.setFormatter(formatter)
        self.logger = logging.getLogger()
        self.logger.addHandler(file_handler)
        self.logger.setLevel("INFO")

        self.logger.info("controller: init")

    def read(self):
        self.logger.info("controller: read request")
        res = self.process.stdout.readline().strip()
        self.logger.info(f"controller: received <{res}>")

        return res

    def write(self, message):
        self.logger.info(f"controller: write request <{message}>")
        self.process.stdin.write(f"{message.strip()}\n")
        self.process.stdin.flush()

    def write_read(self, command):
        self.write(command)
        return self.read()


if __name__ == "__main__":
    c = Controller("run_responder.py")

    hiReceived = c.write_read("Hi")
    assert hiReceived == "Hi", f"expected Hi but received {hiReceived}"

    getRandoms = 100 * ["GetRandom"]
    randReceived = []
    for cmnd in getRandoms:
        resp = c.write_read(cmnd)
        randReceived.append(int(resp))

    c.write("Shutdown")

    print("Sorted received numbers:")
    print(sorted(randReceived))

    print(f"Median is: {median(randReceived)}")
    print(f"Average is: {mean(randReceived)}")
