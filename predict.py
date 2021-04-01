#importing the necessary libraries
from features import Features
import pandas as pd
import time
import pickle
from os import listdir
from typing import Dict


def get_files(file_path: str) -> Dict[str, str]:
    onlyfiles = [f for f in listdir(file_path)]
    files = {}
    for i in onlyfiles:
        files[i] = file_path + i
    return files


def machine(machine_type):
    if machine_type.lower() == "fan":
        model = "models/fan/fan_full_with_smote_89P-89R-89F1.sav"
        return model
    elif machine_type.lower() == "valve":
        model = ""
        return model
    elif machine_type.lower() == "pump":
        model = "datasets/models/pump_models/pump_ALLft_resample.sav"
        return model
    elif machine_type.lower() == "slider":
        model = ""
        return model


def predict(df, model):
    with open(model, 'rb') as f:
        fm = pickle.load(f)
        prediction = fm.predict(df)
        print(f"Machine is {prediction}.")

    if prediction == 1:
        print("Machine is Abnormal.")
        return prediction
            #send an alert

    elif prediction == 0:
        print("Machine is Normal.")
        return predict

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

print(pred) #dictionary

count= 0
for i in pred.values():
    if i == 1 :
        count +=1
            
print(f'{count} / {len(pred.values())}')

end_time = time.time()
print(f"Program runs for {end_time - start_time} seconds.")