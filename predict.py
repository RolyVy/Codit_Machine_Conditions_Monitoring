#importing the necessary libraries
from features import Features
import pandas as pd
import time
import pickle
from os import listdir
from typing import Dict


def get_files(file_path: str) -> Dict[str, str]:
    """
    Function to get the list of files inside a file path
    :parameter file_path will contain the file path of the folder
    :attrib onlyfiles is a list of all the files in file_path
    :attrib files is a dictionary which will have the sound file as key,
    and the file path as the value
    This function returns the files as a dictionary
    """
    onlyfiles = [f for f in listdir(file_path)]
    files = {}
    for i in onlyfiles:
        files[i] = file_path + i
    return files


def machine(machine_type: str) ->str:
    """
    Function machine gets the type model depending on the machine type
    :parameter machine_type will contain the type of machine
    """
    if machine_type.lower() == "fan":
        model = "models/fan/fan_full_with_smote_89P-89R-89F1.sav"
        return model
    elif machine_type.lower() == "valve":
        model = ""
        return model
    elif machine_type.lower() == "pump":
        model = ""
        return model
    elif machine_type.lower() == "slider":
        model = ""
        return model


def predict(df, model: str) -> int:
    """
    Function predict will predict the data
    :parameter df contains the file with the features
    :parameter model contains the model to be used in predicting
    :attrib fm will contain the loaded prediction
    :attrib prediction will contain the prediction from the model
    This function returns the variable if 1, means abnormal, if 0 means normal
    
    """
    with open(model, 'rb') as f:
        fm = pickle.load(f)
        prediction = fm.predict(df)
        #print(fm.score(df, df))
        #print(f"Machine is {prediction}.")
    
    if prediction == 1:
        print("Machine is Abnormal.")
        return 1
            #send an alert    
    
    elif prediction == 0:
        print("Machine is Normal.")
        return 0
    


"""
This is where the program starts
:attrib machine_type will contain the input type of machine
:attrib file_path will contain the file path of the sound files
:attrib start_time will contain the time the program started
:attrib model will contain the model to predict the file
:attrib dict_files will contain the files in a dictionary
:attrib pred will contain the prediction in a dictionary
:attrib count will contain the total number of abnormal in the set
:attrib end_time will contain the time the program ended
"""


machine_type = input("Enter the machine type: ")
file_path = input("Enter the file path: ")
start_time = time.time()
model = machine(machine_type)
        
dict_files = get_files(file_path)
pred = {}
for key, value in dict_files.items(): 
    print(value)           
    data = Features.get_features(value)
    df = pd.DataFrame([data])
    print(f"Predicting for {key}...")
    prediction = predict(df, model) 
    pred[key] = prediction
    
count = 0 
for i in pred.values():
    if i == 1:
        count +=1

print(f"Predicted: {count} / {len(pred.values())}")
end_time = time.time()
print(f"Program runs for {end_time - start_time} seconds.")
    


    
