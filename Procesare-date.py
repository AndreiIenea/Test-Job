import os
import docx
import pandas as pd


def read_docx(file_path):
    doc = docx.Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])


directory = 'path_to_docx_files'


documents = []
for filename in os.listdir(directory):
    if filename.endswith(".docx"):
        file_path = os.path.join(directory, filename)
        content = read_docx(file_path)
        documents.append(content)


df = pd.DataFrame(documents, columns=['exemple_oferte'])


train_data = [{'prompt': ex, 'completion': ''} for ex in df['exemple_oferte'].tolist()]


import json

with open('train_data.json', 'w') as f:
    json.dump(train_data, f, indent=2)
