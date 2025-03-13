import os 
class gcc():
    def __init__(self):
        self.name = "c/cpp"
        self.versions = ["4:8.2.0", "4:11.5.0", "4:12.4.0", "4:14.2.0"]    
    
    def run(self,version):
        self.getPass = input("What is the root password")
        os.write(f"sudo apt-get install gcc={version}-lubuntul -y")
        os.write(self.getPass)
        print("Gnu Compiler (C/C++) has been installed.")

    def detect(self):
        try:    
            os.write("rustc --version")
        except Exception as e:
            return e