
from Bio import Entrez as en
from Bio import SeqIO
import os

#email used to access NCBI-GEO
en.email = "bioinfo@gmail.com"

def ncbiFastaFilesDownloaderFunc (geneDic):
      """
      -Input: 
           1: dictionary with gene symbols and IDs
      -Functionality: Downloading sequencing fasta files from NCBI Nucleotide database for multiple 
                      sequence alignment.
      """
      for gene_symbol, gene_id in geneDic.items():
            ncbi_handle = en.efetch(db= 'nucleotide', id= gene_id, rettype='fasta') # download
            record = SeqIO.read(ncbi_handle, 'fasta') # read data
            print("Downloading %s with sequence length %d" % (record.name, len(record.seq)))
            output_name = gene_symbol+'.fasta'
            SeqIO.write(record, output_name, 'fasta') # write data into file


def fileMergerFunc (dirList, outputFile):
    """
    -Input: 
         1: list of fasta files names
    -Functionality: Merge multiple files into single file.
    """
    data = ""
    for i in dirList:
        if '.fasta' in i:
            with open(i) as f1:
                data = f1.readlines()
            with open(outputFile, 'a') as f2:
                f2.writelines(data)
                f2.write("\n")


if __name__ == '__main__':

    # Gene symbol and GenBank ID
    dict={'G3QWX4':'SRLZ01002358.1',
        'E7F9E5':'CU652893.6',
        'F7AH40':'QNVO02003165.1',
        'Q5EGZ1':'CH474014.2',
        'Q8R0I0':'AL671706.8',
        'F6WXR7':'AAFR03034356.1',
        'G1KTF3':'AAWZ02007819.1',
        'Q56H28':'JAFEKA010000012.1',
        'Q5RFN1':'NDHI03003400.1'}
    ncbiFastaFilesDownloaderFunc(dict)
    fileMergerFunc(os.listdir(),"merged_fasta_files.fasta")

