# Identification of Languages and Dialects of Italy 🇮🇹

Automatic Language Identification represents an important task for improving many real-world applications such as opinion mining and machine translation.
In the case of closely-related languages such as regional dialects, this task is often challenging.

In this project, we propose an extensive evaluation of different approaches for the identification of 11 Italian dialects and languages, spanning from classical machine learning models to more complex neural architectures and state-of-the-art pre-trained language models. 
Surprisingly, shallow machine learning models managed to outperform huge pre-trained language models in this specific task.

This work was developed in the context of the Identification of Languages and Dialects of Italy (ITDI) task organized at VarDial 2022 Evaluation Campaign. Our best submission managed to achieve a weighted F\textsubscript{1}-score of 0.6880, ranking 5th out of 9 final submissions.  

## ITDI Task
We provide participants with Wikipedia dumps (“pages-articles-multistream.xml.bz2”, from 01.03.2022) of 11 languages and dialects of Italy for training (Piedmontese, Venetian, Sicilian, Neapolitan, Emilian-Romagnol, Tarantino, Sardinian, Ligurian, Friulian, Ladin, Lombard). The Standard Italian raw Wikipedia dump may also be used as training data, but there will not be any instances of Standard Italian in the development and test sets. Please use the provided script to download (and extract, if you wish) the dumps to make sure you work with the correct kind and date of the dump.

The task is classification, i.e. the model is required to discriminate between different language varieties. As the training data is provided in the form of raw Wikipedia dumps, careful pre-processing of the data is part of the task. The task is closed, therefore, participants are not allowed to use external data to train their models. Exceptions are off-the-shelf pre-trained language models from the HuggingFace model hub or similar, the use of which has to be clearly stated. The test set will contain newly collected text samples of a subset of the given language varieties for training. The systems will be evaluated on sentence level.

![dialects](https://github.com/giacomocamposampiero/italian-dialects-identification/blob/main/experiments/plots/dialects.png)

## How to install and run the environment
Verify that conda is installed and running on your system by typing:
```
conda --version
```
To install the environment, simply run the following commands in the main project folder:
```
conda env create
conda activate cs4nlp
```

## How to create the dataset
To download and parse the dataset, use the following commands.
```
pip install wikiextractor
cd data/
chmod 700 create.sh
./create.sh
```
The script `create.sh` will automatically download, preprocess and export to csv the Wikipedia dumps used as training data.


##  License 
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>
<br />The wikipedia dataset is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.
