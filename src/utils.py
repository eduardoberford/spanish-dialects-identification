import pandas as pd

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

fold_label = {
    'EML' : 0,
    'NAP' : 1,
    'PMS' : 2,
    'FUR' : 3,
    'LLD' : 4,
    'LIJ' : 5,
    'LMO' : 6,
    'ROA_TARA' : 7,
    'SCN' : 8,
    'VEC' : 9,
    'SC' : 10
}

human_readable_label = {
    0 : 'Emilian-Romagnol',
    1 : 'Neapolitan',
    2 : 'Piedmontese',
    3 : 'Friulian',
    4 : 'Ladin',
    5 : 'Ligurian',
    6 : 'Lombard',
    7 : 'Tarantino',
    8 : 'Sicilian', 
    9 : 'Venetian',
    10 : 'Sardinian'
}

def explain_label(label : int) -> str:
    """ 
    Given an integer label, convert it to the corresponding string label

    :param int label: integer label to be converted
    :return: string corresponding to the given label

    """
    return dial_label[label]

def encode_label(label : str) -> int:
    """ 
    Given a string label, encode it to the corresponding index

    :param string label: string label to be converted
    :return: int corresponding to the given label

    """
    return fold_label[label]

def human_readable_label(label) -> str:
    """
    Given a label, produce a human readable label for the corresponding dialect.
    """
    if isinstance(label, str): label = fold_label(label)
    return human_readable_label[label]



def load_data(train_path = "data/train.csv", val_path="data/dev.txt"):
    """
    Load training and evaluation data.
    """
    if train_path is not None:
        data_train = pd.read_csv(train_path)
        X_train, y_train = data_train['text'].values, data_train['label'].values.astype(int)
        if val_path is None: return X_train, y_train

    if val_path is not None:
        data_val = pd.read_csv(val_path, sep = "\t", names=["label", "text"])
        data_val['label'] = data_val['label'].apply(encode_label)
        X_val, y_val = data_val['text'].values, data_val['label'].values.astype(int)
        if train_path is None: return X_val, y_val
        
    return X_train, y_train, X_val, y_val