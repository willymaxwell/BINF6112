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
            # TODO: increment n (one record was read)
            # TODO: add len(seq) to total_len
            # TODO: add the sum of Phred scores of qual to total_qual
            #       (a Phred score is ord(char) - 33)
            # TODO: add len(qual) to total_qbases
    print(f"reads: {n}")
    # TODO: print "mean read length: X" with X = total_len / n, one decimal
    # TODO: print "mean quality (Phred): X" with X = total_qual / total_qbases, two decimals


if __name__ == "__main__":
    main(sys.argv[1])
