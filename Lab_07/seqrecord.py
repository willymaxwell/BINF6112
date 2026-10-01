#!/usr/bin/env python3
"""Parse a FASTA into SequenceRecord objects and report per-record stats.
Complete each TODO. Run: python3 seqrecord.py data/sequences.fasta
"""
import sys


class SequenceRecord:
    def __init__(self, identifier, seq):
        # TODO: store identifier on self, and store seq uppercased on self
        pass

    def __len__(self):
        # TODO: return the length of the stored sequence
        pass

    def gc_content(self):
        # TODO: return the fraction of G or C bases in the stored sequence
        pass


def read_fasta(path):
    """Yield SequenceRecord objects from a FASTA file."""
    identifier, seq = None, []
    with open(path) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith(">"):
                if identifier is not None:
                    yield SequenceRecord(identifier, "".join(seq))
                identifier, seq = line[1:], []
            else:
                seq.append(line)
    if identifier is not None:
        yield SequenceRecord(identifier, "".join(seq))


def main(path):
    for record in read_fasta(path):
        print(f"{record.identifier}\t{len(record)}\t{record.gc_content():.2f}")


if __name__ == "__main__":
    main(sys.argv[1])
