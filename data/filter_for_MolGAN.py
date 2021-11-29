import rdkit.Chem as Chem
from rdkit.Chem import MolFromSmiles as Mol
import sys
from tqdm import tqdm
from rdkit.Chem.Descriptors import ExactMolWt

def NoStar(s):
    return s.count('*') == 0
def OneMol(s):
    return s.count('.') == 0
def Sanitize(mol):
    return int(Chem.SanitizeMol(mol, catchErrors=True))==0
#def MolWt(mol):
    #return ExactMolWt(mol) < 600

target = sys.argv[1]
with open(target, 'r') as fr:
    data=fr.read().splitlines()

import random
random.shuffle(data)
data=data[:200000]

filtered = []
for smi in tqdm(data):
    mol = Mol(smi)
    if mol is None: continue
    if not NoStar(smi): continue
    if not OneMol(smi): continue
    if not Sanitize(mol): continue
    #if not MolWt(mol): continue
    if mol.GetNumAtoms()>40: continue
    filtered.append(smi)

with open('filtered_for_MolGAN.smi','w') as fw:
    fw.writelines([smi+'\n' for smi in filtered[:150000]])
