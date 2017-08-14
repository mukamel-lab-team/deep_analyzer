"""
Diego Zamora Rodríguez <dzamora@ucsd.edu>

Training log analyzer for the Deepcpg experiments

version 1.0.2

"""

import matplotlib.pyplot as plt
import numpy as np
import sys


def find_data(filename, text):
    file = open(filename, "r")
    i = 0
    for line in file:
        i = i + 1
        if line.find(text) == 0:
            print("Data found in line " + str(i+2))
            return i+2
    file.close()


def get_values(filename, start):    
    loss = []
    acc = []
    file = open(filename, "r")
    for i, line in enumerate(file):        
        l = line.split()
        try:
            if i > (start-1):
                loss.append(l[0])
                acc.append(l[2])
                if l[0] == "Validation":
                    break
        except:
            print("\n")
    file.close()
    if loss[-1] == "Validation" or acc[-1]  ==  "performance:":
        loss.pop()
        acc.pop()
    print("============== Values found ==============")
    print(loss)
    print(acc)
    return [loss, acc]


def plot_acc(training, validation, no_epoch):
    
    X = np.array(list(range(no_epoch)))  # epoch number
    Y1 = np.array(training)
    Y2 = np.array(validation)

    plt.title('Accuracy performance visualization')
    plt.ylabel('Performance')
    plt.xlabel('Number of Epoch')

    plt.xlim(0, no_epoch)
    plt.ylim(0, 1.5)

    plt.grid(True)

    plt.plot(X, Y1, 's', color="red", label="Training")
    plt.plot(X, Y2, 's', color="blue", label="Validation")

    plt.legend()
    plt.show()


def plot_loss(training, validation, no_epoch):
    
    X = np.array(list(range(no_epoch)))  # epoch number
    Y1 = np.array(training)
    Y2 = np.array(validation)

    plt.title('Loss performance visualization')
    plt.ylabel('Performance')
    plt.xlabel('Number of Epoch')

    plt.xlim(0, no_epoch)
    plt.ylim(0, 1.5)

    plt.grid(True)

    plt.plot(X, Y1, 's', color="red", label="Training")
    plt.plot(X, Y2, 's', color="blue", label="Validation")

    plt.legend()
    plt.show()



def startup(filename):
    training = "Training set performance:"
    validation = "Validation set performance:"

    training_start = find_data(filename, training)
    validation_start = find_data(filename, validation)

    training_values = get_values(filename, training_start)
    validation_values = get_values(filename, validation_start)    

    no_epoch = len(training_values[0])
    
    print("\n Number of epoch found: "+str(no_epoch))

    plot_loss(training_values[0], validation_values[0], no_epoch)
    plot_acc(training_values[1], training_values[1], no_epoch)    


if __name__ == "__main__":
    startup(sys.argv[1])
