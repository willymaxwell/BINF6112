#!/usr/bin/env python3
"""FASTQ read QC. Complete each TODO. Run: python3 fastq_qc.py data/reads.fastq

A FASTQ record is four lines: @id, sequence, '+', quality. A Phred quality score
is ord(char) - 33.
"""
import sys


def main(path):
    n = 0
    total_len = 0
    total_qual = 0
    total_qbases = 0
    with open(path) as fh:
        while True:
            header = fh.readline()
            if not header:
                break
            seq = fh.readline().strip()
            plus = fh.readline()
            qual = fh.readline().strip()
            #Increments n (one record was read)
            n+=1
            
            #Add the length of seq  to total_len
            total_len+=len(seq)

            # Loop through qual then add the sum of Phred scores (ord(char)-33) to total_qual
            total_qual += sum(ord(c) - 33 for c in qual)
            
            # Add the length of qual to total_qbases
            total_qbases+=len(qual)
    print(f"reads: {n}")
    
    print(f"mean read length: {total_len / n:.1f}")
    
    print(f"mean quality (Phred): {total_qual / total_qbases:.2f}")

if __name__ == "__main__":
    main(sys.argv[1])
