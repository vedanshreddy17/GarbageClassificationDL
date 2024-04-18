import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import sys

def view(rlist):
    height=rlist
    bars = ('Accuracy','PrScore','Recall\nScore','F1Score')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=['red','cyan','yellow','pink'])
    plt.xticks(y_pos, bars)
    plt.xlabel('Algorithms')
    plt.ylabel('Accuracy')
    plt.title('Algorithms Performance')
    plt.show()


