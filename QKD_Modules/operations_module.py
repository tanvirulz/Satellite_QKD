import os

class OperationsModule:
    def __init__(self,pname="alice",data_dir="./alice/data",protocol_dir="./protocol_stack"):
        self.pname=pname
        self.data_dir=data_dir
        self.protocol_dir=protocol_dir
    def correctdd(self,delays):
        # Aaice ./crt [workDirectory] [H_Offset] [V_Offset] [A_Offset] [D_Offset]
        #./crt $3 alice 0 -750 -1250 -250
        command_str = "{pstack}/crt {workdir} {name} {delays}".format(pstack=self.protocol_dir,workdir=self.data_dir,name=self.pname,delays=delays)
        print (command_str)
        os.system(command_str)
    def coincidence_match(self,cwindow,shift):
        result_file = "{}/result.csv".format(self.data_dir)

        os.system("touch {}".format(result_file))
        os.system('printf "alice_singles_rate, bob_singles_rate, coincidence_window(ps), coincidence_count_rate, sifted_key_length, num_error, QBER, hv_count,ad_count,alice_efficiency(%%), bob_effeciency(%%),duration(s),hv_QBER,ad_qber\n" > {}'.format(result_file) ) 

        command_str = "{ps}/cm {data_dir} {cwindow} {shift} >> {rf}".format(ps=self.protocol_dir,data_dir=self.data_dir,cwindow=cwindow,shift=shift,rf=result_file)
        #./cm [workDirectory] [coincidenceWindow] [matchingShift]
        #./cm $3 $5 -7500 >> $3/$4
        print (command_str)
        os.system(command_str)
    
    def gen_raw_key(self):
        command_str = "{ps}/grb {data_dir} {pname}".format(ps=self.protocol_dir,data_dir=self.data_dir,pname=self.pname)
        print(command_str)
        os.system(command_str)