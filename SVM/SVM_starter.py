import pandas as pd
import numpy as np
from sklearn import svm, metrics
import matplotlib.pyplot as plt

'''
Author: Levi Schanding


    [Notes]
    - Had to fiddle with the data slightly, copied and pasted the first row of the csv to the end of the file

'''


def plot_histogram(title, values):
    plt.hist(values, len(values))
    plt.title(title)
    plt.show()


def prepare_raw():
    raw = pd.read_csv('dataset/mnist_subset.csv')
    new_headers = [f'l{x}' for x in range(len(raw.columns))]
    current_headers = raw.columns
    replacement_mapping = {}

    for i in range(len(current_headers)):
        replacement_mapping[current_headers[i]] = new_headers[i]
    raw.rename(columns=replacement_mapping, inplace=True)

    numbers = [
        raw.index[raw['l0'] == 0].tolist(),
        raw.index[raw['l0'] == 1].tolist(),
        raw.index[raw['l0'] == 2].tolist(),
        raw.index[raw['l0'] == 3].tolist(),
        raw.index[raw['l0'] == 4].tolist(),
        raw.index[raw['l0'] == 5].tolist(),
        raw.index[raw['l0'] == 6].tolist(),
        raw.index[raw['l0'] == 7].tolist(),
        raw.index[raw['l0'] == 8].tolist(),
        raw.index[raw['l0'] == 9].tolist(),
    ]

    return raw, numbers


# splits the raw dataset into a training set and testing set based on a given ratio. Ensures that the ratio is upheld
# for all labels
def split_train_test(ratio, raw, numbers):
    if not isinstance(raw, pd.DataFrame):
        raise TypeError



    training_indices = []
    testing_indices = []

    for number_frame in numbers:
        indices = [x for x in range(len(number_frame))]
        training_count = round(len(number_frame) * ratio)
        testing_count = len(number_frame) - training_count

        for i in range(training_count):
            training_indices.append(indices.pop(np.random.randint(0, len(indices))))

        for i in range(testing_count):
            testing_indices.append(indices.pop(np.random.randint(0, len(indices))))

    training_frame = raw.iloc[training_indices]
    testing_frame = raw.iloc[testing_indices]

    return training_frame, testing_frame


def accuracy(predictions, expected):
    if not isinstance(expected, pd.Series):
        raise TypeError
    correct = 0
    total = len(predictions)

    for i in range(total):

        if predictions[i] == expected.iloc[i]:
            correct += 1

    return correct/total


def testing_suite(ratios, raw, raw_ordered_indices, kernels):
    kernel_accuracies = {}
    for kernel in kernels:
        i = 1
        accuracies = {}
        values = []
        for ratio in ratios:
            print(f"[Kernel: {kernel}] : Test {i} commencing: {ratio*100}% Training, {round(100 - ratio*100)}% Testing")
            train, test = split_train_test(ratio, raw, raw_ordered_indices)
            train_X = train.drop('l0', axis=1)
            train_Y = train['l0']
            test_X = test.drop('l0', axis=1)
            test_Y = test['l0']

            svm_classifier = svm.SVC(gamma=0.001, kernel=kernel)
            svm_classifier.fit(train_X, train_Y)

            predictions = svm_classifier.predict(test_X)
            accu = accuracy(predictions, test_Y)
            accuracies[ratio] = accu
            print(f"[Kernel: {kernel}] : Test {i} ended: accuracy = {round(accu*100, 2)}%")
            values.append([accu, ratio])

            i += 1
        plot_histogram(kernel, values)
        kernel_accuracies[kernel] = accuracies



    return kernel_accuracies


def main():
    raw, raw_ordered_indices = prepare_raw()
    ratios = [x/100 for x in range(5, 100, 5)]
    kernels = [
        'linear',
        'poly',
        'rbf',
        'sigmoid'
    ]
    ratio_accuracies = testing_suite(ratios, raw, raw_ordered_indices, kernels)


    for kernel in kernels:
        for ratio in ratios:
            print(f"[{kernel}][Ratio: {ratio}][Accuracy: {round(ratio_accuracies[kernel][ratio] * 100, 2)}]")







main()
