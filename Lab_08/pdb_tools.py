"""pdb_tools -- a small toolkit for summarizing PDB structures.
LAB 08: complete each TODO. (Our sample PDB is whitespace-separated for simplicity;
real PDB files use fixed columns.)

Field layout after line.split():
  [0]=ATOM  [1]=serial  [2]=atom  [3]=residue  [4]=chain  [5]=resSeq  ...
"""

from typing import Generator, List, Tuple

"""--- AI-use disclosure -------------------------------------------------------
# AI Tool: Gemini Notebook (Gemini 1.5 Pro)
# Purpose: Consulted as a reference for PEP 484 type-hinting on generators and set
#          comprehension patterns for counting unique tuples in PDB records. All module
#          logic and execution were independently written and verified.
# Prompt: "How to annotate Python generators returning lists of strings with PEP 484
#          and use set comprehensions for distinct tuple counting? With provided sources."
# -----------------------------------------------------------------------------
"""

def atom_records(path: str) -> Generator[Lists[str], None, None]:
    """Yield the whitespace-split fields of each ATOM line in a PDB file."""
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("ATOM"):
                yield line.split()


def count_atoms(path) -> int:
    """Return the total number of ATOM records in the PDB file."""
    return sum(1 for _ in atom_records(path))


def count_chains(path):
    pass

def count_residues(path):
    pass
