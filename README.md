______________________________________________________________________________________________________________________________________________________
# CODIT Machine Conditions Monitoring

- Developer Names : `Vincent Rolin and Arlene Postrado`
- Level: `Junior Data Scientist`
- Duration: `2 weeks`
- Deadline: `02/04/2021 09:00 AM`
- Team challenge : `Group Project`
- Type of Challenge: `Learning`
- Promotion: `AI Theano 2`
- Coding Bootcamp: `Becode  Artificial Intelligence (AI) Bootcamp`


### Mission Objectives

- Be able to work and process data from audio format
- Find insights from data, build hypothesis and define conclusions
- Build machine learning models for predictive classification and/or regression
- Select the right performance metrics for your model
- Evaluate the distribution of datapoints and evaluate its influence in the model
- Be able to identify underfitting or overfitting that might exist on the model
- Tuning parameters of the model for better performance
- Select the model with better performance and following your
  customer's requirements
- Define the strengths and limitations of the model

__________________________________________________________________________________________________________________________________________________

## About The Repository

This is a project about developing a machine learning model that is able to monitor the operations and identify anomalies audio sounds of the equipment.

The implementation of this model can allow the clients to operate the manufacturing equipment at full capacity and detect signs of failure before the damage is so critical that the production line has to be stopped.


## Repository


**README.md**
  - has all the necessary information regarding the project

**predict.py**
  - python program that will predict the sound file if there is anomaly or not

**features.py**
  - python program that contains all the function to get the features of the sound files

**preprocessing.py**
  - python program that will get all the features of the sound files

**create_csv.py**
  - python program that will create a dataframe with all the file paths of the sound files

**Datasets folder**
  - this is where all the datasets are saved
  - this has 4 files namely:

      1. **fan_full_features.csv**
          - a csv file containing the all the features extracted for the sound files of fan machines


      2. **pump_full_features.csv**
          - a csv file containing the all the features extracted for the sound files of pump machines


      3. **slider_full_features.csv**
          - a csv file containing the all the features extracted for the sound files of slider machines


      4. **valve_full_features.csv**
          - a csv file containing the all the features extracted for the sound files of valve machines



**Models folder**
  - this is where all the models are saved
  - this has 4 files namely:


      1. **fan_model.sav**
          - the machine learning model created for Fan machines


      2. **pump_model.sav**
          - the machine learning model created for Pump machines


      3. **slider_model.sav**
          - the machine learning model created for Slider machines


      4. **valve_model.sav**
          - the machine learning model created for Valve machines


     
   
**Models Creation folder**
  - this is where all the jupyter notebooks to create the models are saved 
  - this has 4 files namely:
      1. **fan_features.ipynb**
          - the jupyter notebook to create the model for Fan machines
      2. **pump_features.ipynb**
          - the jupyter notebook to create the model for Pump machines
      3. **slider_features.ipynb**
          - the jupyter notebook to create the model for Slider machines
      4. **valve_features.ipyn**
          - the jupyter notebook to create the model for Valve machines
          



______________________________________________________________________________________________________________________________________________________

## Libraries Used For This Project

**Pandas** https://pypi.org/project/pandas/
  - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
  - In this project, pandas is used to read the csv files as a dataframe.


**Time** https://docs.python.org/3/library/time.html
  - Time module handles time-related tasks.
  - In this project, time is used to calculate the total time the code runs.


**Typing** https://docs.python.org/3/library/typing.html
  - Typing defines a standard notation for Python function and variable type annotations.
  - In this project, typing is used to help document the code properly.

______________________________________________________________________________________________________________________________________________________

## Clone/Fork Repository
  - If you wish to clone/fork this repository, you can just click on the repository, then click the Clone/fork button and follow the instructions.

## Pending...
  - 


### Thank you for reading. Have fun with the code!
