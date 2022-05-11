dial_label = {
    0 : 'emiliano',
    1 : 'napoletano',
    2 : 'piemontese',
    3 : 'friulano',
    4 : 'ladino',
    5 : 'ligure',
    6 : 'lombardo',
    7 : 'tarantino',
    8 : 'siciliano', 
    9 : 'veneto',
    10 : 'sardo'
}

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