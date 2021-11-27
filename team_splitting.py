#importing all
import random
from sklearn.preprocessing import LabelEncoder
import numpy as np

#Loop
while True:
    #List
    leaders = ["Dhoni","Raina"]
    names = ["Athif","Asif","Games","pc","coca","sherin","Faizal","Suresh","Rammesh","Kamesh","kamalkannan","pratap","siva"]

    #LabelEncoding
    le = LabelEncoder()

    #Two lists
    list_1 = []
    list_2 = []

    #Making sum in length of names
    sum1 = len(names)//2
    sum2 = len(names)//2 + len(names)%2

    #Appending values to list
    list_1.append(random.sample(names, sum1))
    list_2.append(random.sample(names,sum2))

    #Making 2d array to 1d array
    list_1 = np.array(list_1)
    list_1= list_1.flatten()


    list_2 = np.array(list_2)
    list_2 = list_2.flatten()


    #Fit and transform using Label Encoding
    le = LabelEncoder()
    le.fit(list_1)
    le.transform(list_1)
    le.fit(list_2)
    le.transform(list_2)


    #Checking if its done correct
    if set(list_1)&set(list_2) != set():
        pass
    else:
        list_1 = list_1.tolist()
        list_2 = list_2.tolist()
        print("Team splitted")
        print("----------------------------")
        print("Team : 1")
        print({leaders[0]:list_1})
        print("")
        print("Team : 2")
        print({leaders[1]:list_2})
        print("-----------------------------")
        print("Process Done")
        break
# --------------------- Finished----------------------------#


