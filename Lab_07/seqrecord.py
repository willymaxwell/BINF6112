#!/usr/bin/env python3
"""Parse a FASTA into SequenceRecord objects and report per-record stats."""

"""AI Tool: Gemini Notebook (Gemini 1.5 Pro)
Purpose: Consulted as a technical reference for PEP 484 class type-hinting,
Python magic methods (__len__, __repr__), and handling zero-length sequence edge cases.

All class logic, parsing, and execution were independently written and verified.

Prompt:How to annotate class methods in Python with PEP 484 type hints and 
implement magic methods for sequence data objects?"

"""


import sys


class SequenceRecord:   """Constructor"""
    def __init__(self, identifier: str, seq: str) -> None:
        self.identifier: str = identifier
        self.seq: str = seq.upper()

    def __len__(self) -> int:
        """Returns the length of the object's actual sequence."""
        return len(self.seq)

    def __repr__(self) -> str:
        """Return developer representation of the object"""
        return f"SequenceRecord(identifier={self.identifier!r}, seq={self.seq!r})"

    def gc_content(self) -> float:
        if not self.seq:
            return 0.0
        gc_count = sum(1 for base in self.seq if base in ("G", "C"))
        return gc_count / len(self)


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
