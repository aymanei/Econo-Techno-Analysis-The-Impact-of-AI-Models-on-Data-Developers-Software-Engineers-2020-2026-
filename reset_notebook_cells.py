import nbformat as nbf
import os

target_file = r'c:\Users\a\Desktop\vstest\ai_impact_on_data_developers.ipynb'

# 1. Regenerate 14-cell notebook with reset execution counts and clean metadata
import create_14cell_notebook

# 2. Read generated notebook and explicitly clean execution counts and outputs
nb = nbf.read(target_file, as_version=4)

for cell in nb.cells:
    if cell.cell_type == 'code':
        cell.execution_count = None
        cell.outputs = []
    if 'metadata' in cell:
        cell.metadata = {}

nbf.write(nb, target_file)

print("Successfully reset all notebook cell execution counts and metadata.")
