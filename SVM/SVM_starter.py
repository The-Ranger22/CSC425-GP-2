import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Author: Levi Schanding


    [Notes]
    - Had to fiddle with the data slightly, copied and pasted the first row of the csv to the end of the file

'''


# Reads the MNIST dataset into a DataFrame and organizes it so that there is a balanced training/testing split
def data_preprocessing(ratio):
    raw = pd.read_csv('dataset/mnist_subset.csv')
    new_headers = [f'l{x}' for x in range(len(raw.columns))]
    current_headers = raw.columns
    replacement_mapping = {}

    for i in range(len(current_headers)):
        replacement_mapping[current_headers[i]] = new_headers[i]
    raw.rename(columns=replacement_mapping, inplace=True)
    numbers = [
        raw[raw['l0'] == 0],
        raw[raw['l0'] == 1],
        raw[raw['l0'] == 2],
        raw[raw['l0'] == 3],
        raw[raw['l0'] == 4],
        raw[raw['l0'] == 5],
        raw[raw['l0'] == 6],
        raw[raw['l0'] == 7],
        raw[raw['l0'] == 8],
        raw[raw['l0'] == 9]
    ]
    print(raw.head(10))
    training_frame = pd.DataFrame(columns=new_headers)
    testing_frame = pd.DataFrame(columns=new_headers)

    for number_frame in numbers:
        training_count = round(len(number_frame) * ratio)
        testing_count = len(number_frame) - training_count

        for i in range(training_count):
            rand = np.random.randint(0, len(number_frame))
            training_frame.append(number_frame.iloc[rand])


        for i in range(testing_count):
            rand = np.random.randint(0, len(number_frame))
            testing_frame.append(number_frame.iloc[rand])


    return training_frame, testing_frame






def main():
    train, test = data_preprocessing(0.7)


main()
