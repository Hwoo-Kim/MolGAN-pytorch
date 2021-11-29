import os

with open('filtered_for_MolGAN.smi', 'r') as fr:
    data =fr.readlines()

with open(f'ChEMBL.smi', 'w') as fw:
    fw.writelines(data[:130000])
os.system(f'python sparse_molecular_dataset.py ChEMBL.smi ChEMBL.sparsedataset')

'''
with open(f'ChEMBL_test.smi', 'w') as fw:
    fw.writelines(data[10:20])
os.system(f'python sparse_molecular_dataset.py ChEMBL_test.smi ChEMBL_test.sparsedataset')
import pickle
with open('ChEMBL_test.sparsedataset','rb') as fr:
    data=pickle.load(fr)
keys=['data', 'atom_encoder_m', 'atom_decoder_m', 'atom_num_types', 'bond_encoder_m', 'bond_decoder_m', 'bond_num_types', 'smiles_encoder_m', 'smiles_decoder_m', 'smiles_num_types', 'smiles', 'data_S', 'data_A', 'data_X', 'data_D', 'data_F', 'data_Le', 'data_Lv', '_SparseMolecularDataset__len', 'vertexes', 'features', 'all_idx', 'train_idx', 'validation_idx', 'test_idx', 'train_counter', 'validation_counter', 'test_counter', 'train_count', 'validation_count', 'test_count']
print(data['data_A'].shape)
'''
