import os

class CommunicationModule:
    def __init__(self,pname='alice',data_dir="./alice/data",destination_dir="./bob/data"):
        self.pname=pname
        self.data_dir=data_dir
        self.destination_dir=destination_dir
    def sendtimestamp(self,file):
        command_str = "cp {data_dir}/{file} {dest_dir}/".format(data_dir=self.data_dir,file=file,dest_dir=self.destination_dir)
        print (command_str)
        os.system(command_str)
    
    def sendCoincidenceIndex(self,file):
        command_str = "cp {data_dir}/{file} {dest_dir}/".format(data_dir=self.data_dir,file=file,dest_dir=self.destination_dir)
        print (command_str)
        os.system(command_str)
    
    def sendBasisMatchIndex(self,file):
        command_str = "cp {data_dir}/{file} {dest_dir}/".format(data_dir=self.data_dir,file=file,dest_dir=self.destination_dir)
        print (command_str)
        os.system(command_str)
    