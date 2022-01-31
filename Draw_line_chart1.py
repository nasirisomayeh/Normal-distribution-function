
from cProfile import label
import matplotlib.pyplot as nem

x = ["mordad", "shahrivar","mehr","aban", "azar","dey","bahman"]
y = [300, 600, 1000, 2000, 3100, 4052, 4950]

nem.plot(x,y,label="learnPY Followers")
nem.legend()

nem.show()