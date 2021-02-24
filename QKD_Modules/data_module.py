import os

class DataModule:
    def __init__(self, pname = 'alice',data_dir="./alice/data", source_path="data_source",source_file="5_4mW00dB.ttbin",timestamp_reader="./protocol_stack/rrswabian"):
        self.pname = pname #Player Name
        self.data_dir = data_dir
        self.source_path = source_path
        self.source_file = source_file
        self.timestamp_reader = timestamp_reader

    def start_data_acquisitaion(self):
        print("Data Acquisiton Started at [{}]".format(self.pname))
        #txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
        command_str = "{reader} {input_dir} {input_file} {output_dir}".format(reader=self.timestamp_reader,input_dir=self.source_path,input_file=self.source_file,output_dir=self.data_dir)
        print (command_str)
        os.system(command_str)
        if self.pname == 'alice':
            os.system("rm {}/bob.out".format(self.data_dir))
        elif self.pname=='bob':
            os.system("rm {}/alice.out".format(self.data_dir))
        else:
            "Error in Data Module: player name unknown. given:{}".format(self.pname)
            exit(1)