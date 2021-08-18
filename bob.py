import sys
import time



from QKD_Modules.data_module import DataModule
from QKD_Modules.operations_module import OperationsModule
from QKD_Modules.communicatoin_module import CommunicationModule

dm = DataModule(pname = 'bob',data_dir="./bob/data", source_path="data_source",
                source_file="5_4mW00dB.ttbin",timestamp_reader="./protocol_stack/rrswabian")
            
om = OperationsModule(pname="bob",data_dir="./bob/data",protocol_dir="./protocol_stack")

cm = CommunicationModule(pname='bob',data_dir="./bob/data",destination_dir="./alice/data")


bob_detector_delays = "0 250 250 250"
coincidence_shift = "-7500"
coincidence_window = "1500"
print("arguments given:", sys.argv)

if len(sys.argv) == 1: 
    print("please provide a command and associated parameters")
    exit(0)

command = sys.argv[1]

if command=="read_data":
    start = time.time()
    dm.start_data_acquisitaion()
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))
elif command == "correctdd":
    start = time.time()
    print("Detector Delay Correction Started")
    om.correctdd(bob_detector_delays)
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))
elif command == "coinmatch":
    start = time.time()
    print("Detector Delay Correction Started")
    om.coincidence_match(cwindow=coincidence_window,shift=coincidence_shift)
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))
elif command == "sendci":
    start = time.time()
    print("Sending Coincidence Index to Alice")
    cm.sendCoincidenceIndex("alice_coin.out")
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))

elif command == "sendbi":
    start = time.time()
    print("Sending Basis Match Index to Alice")
    cm.sendBasisMatchIndex("basis_match_bitmask.out")
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))

elif command == "genrawkey":
    start = time.time()
    print("Generating rawkey for [{}]".format("Bob"))
    om.gen_raw_key()
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))

elif command == "siftkey":
    start = time.time()
    print("Generating rawkey for [{}]".format("Bob"))
    om.sift_key()
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))

else:
    print ("Error:unknown command")
    exit(1)
