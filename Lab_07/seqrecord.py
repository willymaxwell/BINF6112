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

    with open(path, "r", encoding = "utf8") as fh:
        for line in fh:
            line = line.rstrip("\r\n")
            if line.startswith(">"):
                if identifier is not None:
                    yield SequenceRecord(identifier, "".join(seq))
                identifier, seq = line[1:].strip(), []
            else:
                seq.append(line.strip())
    if identifier is not None:
        yield SequenceRecord(identifier, "".join(seq))


def main(path: str) -> None:
    """Parse FASTA file and print per record stats."""
    try:
        record_count=0
        for record in read_fasta(path):
            record_count += 1
            print(f"{record.identifier}\t{len(record.gc_content():.2f}")

        if record_count == 0:
            print(f"Warning : no FASTA record found in '{path}'.", file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: File '{path}' is not fount.", file = sys.stderr)
        sys.exit(1)
    except Exception as err:
        print(f"Error reading FASTA file '{path}': {err}", file = sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1])
