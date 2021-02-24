// writing on a text file
#include <iostream>
#include <fstream>


#include <stdio.h>
#include <inttypes.h>
#define BUFFER_SIZE (32*1024)

using namespace std;

int main(int argc, char * argv[]){
    char inBuffer[BUFFER_SIZE];
    char outBuffer[BUFFER_SIZE];
    char c; 

    c = 'A';
  
  
    //ifstream infile;
    ofstream outfile;
    outfile.rdbuf()->pubsetbuf(outBuffer, BUFFER_SIZE);
    outfile.open("23Oct2020_stitch/test.txt",ios::out|ios::binary|ios::trunc);
    outfile.write(reinterpret_cast<char *>(&c),sizeof(c));
    outfile.close();
}
