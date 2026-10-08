"""pdb_tools -- a small toolkit for summarizing PDB structures.
LAB 08: complete each TODO. (Our sample PDB is whitespace-separated for simplicity;
real PDB files use fixed columns.)

Field layout after line.split():
  [0]=ATOM  [1]=serial  [2]=atom  [3]=residue  [4]=chain  [5]=resSeq  ...
"""


def atom_records(path):
    """Yield the whitespace-split fields of each ATOM line in a PDB file."""
    with open(path) as fh:
        for line in fh:
            if line.startswith("ATOM"):
                yield line.split()


def count_atoms(path):
    # TODO: return the number of ATOM records
    pass


def count_chains(path):
    # TODO: return the number of DISTINCT chain IDs (field index 4)
    pass


def count_residues(path):
    # TODO: return the number of DISTINCT (chain, resSeq) pairs (indices 4 and 5)
    pass
