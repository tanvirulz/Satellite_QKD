import sys
import time




from QKD_Modules.data_module import DataModule
from QKD_Modules.operations_module import OperationsModule
from QKD_Modules.communicatoin_module import CommunicationModule



dm = DataModule(pname = 'alice',data_dir="./alice/data", source_path="data_source",
                source_file="5_4mW00dB.ttbin",timestamp_reader="./protocol_stack/rrswabian")
om = OperationsModule(pname="alice",data_dir="./alice/data",protocol_dir="./protocol_stack")

cm = CommunicationModule(pname='alice',data_dir="./alice/data",destination_dir="./bob/data")

alcie_detector_delays = "0 -750 -1250 0"
#bob_detector_delays = "0 250 250 250"


print("arguments given:", sys.argv)

if len(sys.argv) == 1: 
    print("please provide a command and associated parameters")
    exit(0)

command = sys.argv[1]

if command=="read_data":
    start = time.time()
    print("Data Acquisiton Started")
    dm.start_data_acquisitaion()
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))
elif command == "correctdd":
    start = time.time()
    print("Detector Delay Correction Started")
    om.correctdd(alcie_detector_delays)
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))
elif command == "sendtt":
    start = time.time()
    print("Sending timestamp to Bob")
    cm.sendtimestamp("alice_corrected.out")
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))

elif command == "genrawkey":
    start = time.time()
    print("Generating rawkey for [{}]".format("Alice"))
    om.gen_raw_key()
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))

elif command == "siftkey":
    start = time.time()
    print("Generating rawkey for [{}]".format("Alice"))
    om.sift_key()
    end = time.time()
    print("[Done] in {0} seconds".format(end-start))

else:
    print ("Error:unknown command")
    exit(1)
