#!/usr/bin/env python3
"""Parse a FASTA into SequenceRecord objects and report per-record stats.
Complete each TODO. Run: python3 seqrecord.py data/sequences.fasta
"""
import sys


class SequenceRecord:
    def __init__(self, identifier: str, seq: str) -> None:
        self.identifier: str = identifier
        self.seq: str = seq.upper()

    def __len__(self) -> int:
        return len(self.seq)

    def gc_content(self) -> float:
        if not self.seq:
            return 0.0
        return sum(1 for base in self.seq if base in ("G", "C")) / len(self)


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
