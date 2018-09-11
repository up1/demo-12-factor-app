import time
import signal


def busy_work(seconds):
    print("Start busy_work")
    time.sleep(seconds)
    print("Stop busy_work")


class Transporter:
    def __init__(self):
        self.stopped = False

    def run(self):
        while not self.stopped:
            busy_work(10)

    def stop(self, signal, frame):
        print("Stop the transporter ...")
        self.stopped = True


def main():
    # Setup transporter
    transporter = Transporter()
    # Setup signal handler
    signal.signal(signal.SIGINT, transporter.stop)
    signal.signal(signal.SIGTERM, transporter.stop)
    transporter.run()


if __name__ == "__main__":
    main()