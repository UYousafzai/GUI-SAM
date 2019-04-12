from builder import window
from data_grabber import data
from label_maker import *


root = window()
root = root.get_window()
text = ["this is a test", "this is a second test"]
data_object = data()

data_object.assign_labels(text)

label_object = labels(root)
label_object.build_labels(data_object)

my_labels = label_object.get_labels()
my_labels[0].grid(row=0)
my_labels[1].grid(row=1)

root.mainloop()