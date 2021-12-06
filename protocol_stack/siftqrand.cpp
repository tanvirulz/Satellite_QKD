#include <iostream>
#include <fstream>


#include <stdio.h>
#include <inttypes.h>


#define BUFFER_SIZE (32*1024)
#define H 1
#define V 2
#define A 4
#define D 8


#define AD_BASIS 3
#define HV_BASIS 12

#define FILE_NAME_SIZE 256

using namespace std;

int main(int argc, char* argv[]){
    char bimask_Buffer[BUFFER_SIZE];

    char rawkey_Buffer[BUFFER_SIZE];
    char siftedkey_Buffer[BUFFER_SIZE];
    
    uint8_t raw_bit;
    uint8_t basis_matched; 

    uint32_t sifted_bits_count;
    
    ifstream bitmap_infile;

    ifstream rawkey_infile;
    

    ofstream sifted_raw_qrn_outfile;

    char bitmap_infile_name[FILE_NAME_SIZE];
    char rawkey_infile_name[FILE_NAME_SIZE];
    char sifted_raw_qrn_outfile_name[FILE_NAME_SIZE];
    
    if(argc<3){
        printf("sift [workfolder] [player name]\n");
        exit(0);
    }
    
 
    sprintf(bitmap_infile_name,"%s/%s",argv[1],"basis_match_bitmask.out");

    sprintf(rawkey_infile_name,"%s/%s_raw.txt",argv[1],argv[2]); 
    
    sprintf(sifted_raw_qrn_outfile_name,"%s/%s_sifted_raw_qrn.txt",argv[1],argv[2]); // contwill contain raw key bits where the basis mismatched. 


    bitmap_infile.rdbuf()->pubsetbuf(bimask_Buffer, BUFFER_SIZE);
    rawkey_infile.rdbuf()->pubsetbuf(rawkey_Buffer, BUFFER_SIZE);
    sifted_raw_qrn_outfile.rdbuf()->pubsetbuf(siftedkey_Buffer, BUFFER_SIZE);

 
    bitmap_infile.open(bitmap_infile_name,ios::in|ios::binary);

    rawkey_infile.open(rawkey_infile_name,ios::in|ios::binary);
    sifted_raw_qrn_outfile.open(sifted_raw_qrn_outfile_name,ios::out|ios::binary|ios::trunc);


    while(1){
        bitmap_infile.read(reinterpret_cast<char *> (&basis_matched),sizeof(basis_matched));
        if (bitmap_infile.eof()) break;
        rawkey_infile.read(reinterpret_cast<char *> (&raw_bit),sizeof(raw_bit));
        if (bitmap_infile.eof()) break;


        if (!basis_matched){ // if the basis mismatch generate raw random bits from here. 
            sifted_raw_qrn_outfile.write(reinterpret_cast<char *> (&raw_bit), sizeof(raw_bit) );
            sifted_bits_count ++;
        }

    }

    printf("Number of sifted raw quantum random bits: %d\n", int(sifted_bits_count));
    bitmap_infile.close();
    rawkey_infile.close();
    sifted_raw_qrn_outfile.close();

    return 0;

}