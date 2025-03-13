import os
import subprocess

class rust():
    def __init__(self):
        self.filename = "rustup-init.exe"
        self.name = "rust"
        self.versions = ["Latest"]
    
    def run(self):
        try:
            subprocess.run(["curl", "--proto", "'=https'", "--tlsv1.2", "-sSf", "https://sh.rustup.rs", "|", "sh"], check=True)
            PATH = os.path.dirname(self.filename)
            subprocess.run(["start", os.path.join(PATH, self.filename)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

    def detect(self):
        try:
            os.system(["rustc", "--version"], check=True)
        except Exception as e:
            pass
