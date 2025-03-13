import os 

class ruby():
    def __init__(self, packagemanager=None):
        self.packagemanager = packagemanager
        self.name = "ruby"
        self.versions = [1.8, 1.9, 2.0, 2.1, "Latest"]
        
    def run(self):
        if self.packagemanager is not None:
            if self.packagemanager == "snap":
                os.system("sudo snap install ruby --classic")
            elif self.packagemanager == "yum": 
                os.system("sudo yum install ruby")
        else:
            os.system("sudo apt-get install ruby-full")
            print("Use the RVM for more versions of Ruby")

    def detect(self):
        try:
            os.system("ruby -v")
        except Exception as e:
            return e