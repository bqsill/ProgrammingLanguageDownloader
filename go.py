import os 

class go():
    def __init__(self):
        self.name = "go"
        self.versions = ["1.16.7", "1.17.1", "1.18.0"]

    def run(self,version):
        os.system("sudo apt search golang-go")
        os.system("sudo apt-get install golang-go=" + version + "-lubuntul -y")
        print("Go has been installed, use golang --version to confirm")

    def detect(self):
        try:
            os.system("go version")
        except Exception as e:
            pass
