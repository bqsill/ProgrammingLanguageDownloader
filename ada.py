import os 

class ada:
    def __init__(self):
        self.name = "ada"
        self.versions = ["2012", "2020"]

    def run(self,choice):
        os.system("sudo apt-get install gnat gprbuild")
        print("Ada has been installed, use gnat --version to confirm")

    def detect(self):
        try:
            os.system("gnat --version")
        except Exception as e:
            pass