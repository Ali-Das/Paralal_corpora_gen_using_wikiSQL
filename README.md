## Parallel corpora generation using WikiSQL Dataset
This repo provides parallel corpora developed using the [WikiSQL dataset](https://github.com/salesforce/WikiSQL). The scripts to generate the corpora are written in Python 3.5 and above. These corpora can be used to train a sequence to sequence neural translation model like 
the open-source neural machine translation toolkit [OpenNMT](http://opennmt.net/) for text_to_SQL conversion.

Table of Contents
=================
  * [Installation](#Installation)
  * [generation of parallel corpora](#generation of parallel corpora)
  * [Citation](#citation)
  * [Acknowledgement](#Acknowledgement)


## Installation
WikiSQL data is collected from [WikiSQL dataset](https://github.com/salesforce/WikiSQL) and stored in the directory data/WikiSQL_data. This folder contains files in `jsonl` and `db` format.
The former can be read line by line, where each line is a serialized JSON object.
The latter is a SQLite3 database. Detailed description of WikiSQL dataset can be found in its site: [WikiSQL dataset](https://github.com/salesforce/WikiSQL)

The installation steps are as follows:

    install python3.5  # or above
    pip install -r requirements.txt

## generation of parallel corpora

### Step 1:  Generate tokenized jsonl files
    python3 DataConversion.py
Script `DataConversion.py` generates the following jsonl files which are stored in the data/WikiSQL_data folder: 
* `tokenized_dev.tables.jsonl`
* `tokenized_test.tables.jsonl`
* `tokenized_train.tables.jsonl`

### Step 2: Generate parallel corpora for training, testing and development
    python3 parallel_corpora_gen.py

Script `parallel_corpora_gen.py` generates the following text files which are stored in the data/text_files folder:
* `src_train.txt`
* `tgt_train.txt`
* `src_dev.txt`
* `tgt_dev.txt`
* `src_test.txt`
* `tgt_test.txt`

### Step 3: The above files may be used to train a sequence to sequence neural translation model like: [OpenNMT](http://opennmt.net/) and the model may be used to generate a prediction file `pred.txt`.

### Step 4: Conversion of  `tgt_test.txt`  and `pred.text` files  to text files that contain SQL queries.
    python3 sql_gen.py data/text_files/tgt_test.txt data/WikiSQL_data/tokenized_test.tables.jsonl data/text_files/tgt_test_sql.txt
    python3 sql_gen.py data/text_files/pred.txt data/WikiSQL_data/tokenized_test.tables.jsonl data/text_files/pred_sql.txt

`sql_gen.py` converts lines of text of the above source files to their corresponding SQL queries.

```
usage: sql_gen.py [-h] source_file db_jsonl_file sql_file

positional arguments:
  
  source_file:   text file generated from WikiSQL data or model
  db_jsonl_file: database table jsonl file
  sql_file:      text file containing SQL queries
```

### Step 5: Queries of these two files `tgt_test_sql.txt` and `pred_sql.text`  are executed and compared to test the accuracy of the predicted model.
    python evaluate.py data/text_files/tgt_test_sql.txt data/WikiSQL_data/test.db data/text_files/pred_sql.txt

`evaluate.py` contains the evaluation script.

```
usage: evaluate.py [-h] gold_SQL_file db_file pred_SQL_file

positional arguments:

  gold_SQL_file :   gold SQL queries generated from the test text file
  db_file:          SQLite3 database for test data
  pred_SQL_file:    SQL queries generated from the prediction file by the model
```

## Citation

> Alaka Das, Redefining Text-to-SQL Task as a Machine Translation problem

## Acknowledgement

The implementation is based on 
[OpenNMT: Neural Machine Translation Toolkit](https://arxiv.org/pdf/1805.11462), 
[WikiSQL dataset](https://github.com/salesforce/WikiSQL). 
Please cite them too if you use this code.

