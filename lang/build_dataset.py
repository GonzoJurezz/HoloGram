import json
from sklearn.model_selection import train_test_split
import os
import re


TEST_DATASET_PERCENTAGE=0.15


def load_json(file_name:str):
    '''
    Load json file from json file name.

    @type file_name: string
    @param file_name: path to file

    @rtype list
    @return list of json dicts
    '''
    dump = []

    with open(file_name) as f:
        dump = json.load(f)

    return dump


def build_dataset(json_data:list):
    '''
    Reads list of json dicts, takes 'text' field, prepares texts, and apend them
    to string seperated by newlines.

    @type json_data: list
    @param json_data: List of json dicts

    @rtype: str
    @return: Dataset as string seperated by newlines
    '''
    data = ''
    for dict in json_data:

        text = str(dict['text']).strip()
        # Replace every whitespace character with space
        text = re.sub(r"\s", " ", text)
        # Cut occurring ">" and "<"
        text = re.sub(r"<|>", "", text)

        data += text + "\n"

    return data


def main():

    json_data = []

    # Load all json dumps
    file_names = ["data/"+file_name for file_name in os.listdir("data")]
    for file_name in file_names:
        json_data += load_json(file_name)

    # Split training and test dataset
    train, test = train_test_split(json_data,test_size=TEST_DATASET_PERCENTAGE)

    train_data = build_dataset(train)
    test_data = build_dataset(test)

    # Write datasets as textfiles
    with open('train_data.txt', 'w') as f:
        f.write(train_data)

    with open('test_data.txt', 'w') as f:
        f.write(test_data)


if __name__ == '__main__':
    main()
