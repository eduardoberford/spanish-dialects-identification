# csnlp-project

## How to create the dataset
To download and parse the dataset, use the following commands.
```
pip install wikiextractor
chmod 700 create.sh
./create.sh
```
The script `create.sh` will automatically download, preprocess and export to csv the Wikipedia dumps used as training data.