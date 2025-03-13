import os

class Java():
    def __init__(self):
        self.name = "java"
        PATH = "etc/java/config"
        self.getPass = input("Enter the root password")
        if not os.path.exists(PATH):
            os.makedirs(PATH)
        self.versions = [8, 11, 15, 17, 23]

    def run(self,version):
        os.system("sudo apt install openjdk-" + str(version) + "-jdk")
        os.system(self.getPass)
        os.system("Y")
        print("Java has been installed, use javac --version to confirm")

    def detect(self):
        try:
            os.system("javac --version")
        except Exception as e:
            return e