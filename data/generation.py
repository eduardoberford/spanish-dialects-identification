import os 
import json
import pandas as pd
import re
from tqdm import tqdm
import numpy as np

print("Generating the dataset...")

# list of dialects in the training set
dialects = [d for d in os.listdir(".") if not os.path.isfile(d) and d != '.ipynb_checkpoints']

# define dictionaries for string->int and int->label conversion
fold_label = {
    'eml_texts' : 0,
    'nap_texts' : 1,
    'pms_texts' : 2,
    'fur_texts' : 3,
    'lld_texts' : 4,
    'lij_texts' : 5,
    'lmo_texts' : 6,
    'roa_tara_texts' : 7,
    'scn_texts' : 8,
    'vec_texts' : 9,
    'sc_texts' : 10
}
dial_label = {
    0 : 'EML',
    1 : 'NAP',
    2 : 'PMS',
    3 : 'FUR',
    4 : 'LLD',
    5 : 'LIJ',
    6 : 'LMO',
    7 : 'ROA_TARA',
    8 : 'SCN', 
    9 : 'VEC',
    10 : 'SC'
}

# create training dataset
data = []

for d in tqdm(dialects):
    for name in os.listdir(d + "/AA/"):
        f = open(d + "/AA/" + name, "r")
        lines = f.readlines()
        for l in lines:
            jline = json.loads(l)
            if not jline['text']:
                continue
            data.append([int(jline['id']), jline['url'], jline['title'], jline['text'], fold_label[d]])


columns = {'id':int(), 'url':str, 'title':str, 'text':str, 'label':int()}
df = pd.DataFrame(data, columns = columns)

# clean text
def clean(text):
    text = re.sub(r'==.*?==+', '', text)

    text = text.replace("\n", " ")

    text = text.replace('"', " ")

    regex = re.compile('&[^;]+;') 
    text = re.sub(regex, '', text)


    regex = re.compile('(graph.*/graph|\(.*\)|\[.*\]|parentid>.*/parentid>|BR[^>]+>|bR[^>]+>|Br[^>]+>|br[^>]+>|ns>.*/ns>|timestamp>.*/timestamp>|revision>.*/revision>|contributor>.*/contributor>|model>.*/model>|format>.*/format>|comment>.*/comment>)') 
    text = re.sub(regex, '', text)

    text = text.replace("revision>", "")
    text = text.replace("br>", "")
    text = text.replace("Br>", "")
    text = text.replace("bR>", "")
    text = text.replace("BR>", "")
    text = text.replace("/br>", "")
    text = text.replace("/Br>", "")
    text = text.replace("/bR>", "")
    text = text.replace("/BR>", "")

    text = text.replace("&quot;","")

    text = text.replace("br clear=all>", "")

    if(len(text) < 50):
        text = np.nan

    return text

print("Cleaning text...")

df['text'] = df['text'].apply(clean)

# drop rows with nan values
df.dropna(inplace=True)

df.to_csv("train.csv", index=None)

print("Dataset created.")