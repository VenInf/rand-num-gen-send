from subprocess import PIPE, Popen
from statistics import mean, median

class Controller():
    def __init__(self, responder):
        self.responder = responder
        self.process = Popen(["python", "-u", responder], stdin=PIPE, stdout=PIPE, bufsize=0, universal_newlines=True)

    def read(self):
        return self.process.stdout.readline().strip()

    def write(self, message):
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





