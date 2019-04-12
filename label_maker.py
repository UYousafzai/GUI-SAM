from builder import *
from tkinter import *
from data_grabber import *

class labels:
    labels = [] 
    root = 0
    def __init__(self, root):
        self.root = root

    def build_labels(self, data_object):
        strings = data_object.get_labels_strings()
        for i in range(len(strings)):
            temp = Label(self.root, text = strings[i])
            self.labels.append(temp)

    def get_labels(self):
        return self.labels
