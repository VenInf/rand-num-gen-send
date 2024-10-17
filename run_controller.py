from subprocess import PIPE, Popen

class Controller():
    def __init__(self, receiver):
        self.receiver = receiver
        self.process = Popen(["python", "-u", receiver], stdin=PIPE, stdout=PIPE, bufsize=0, universal_newlines=True)

    def read(self):
        return self.process.stdout.readline().strip()

    def write(self, message):
        self.process.stdin.write(f"{message.strip()}\n")
        self.process.stdin.flush()

    def rep(self, command):
        self.write(command)
        result = self.read()
        print(f"[{result}]")


if __name__ == "__main__":
    c = Controller("run_receiver.py")

    getRands = 100 * ["GetRandom"]
    commands = ["Hi"] + getRands + ["Shutdown"]

    for command in commands:
        c.rep(command)

