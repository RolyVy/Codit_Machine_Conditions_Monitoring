import pandas as pd
from zipfile import ZipFile
import time

def get_filenames(file):
    file_names = []
    with ZipFile(zip_file, 'r') as zipObj:
        listOfiles = zipObj.namelist()
        for elem in listOfiles:
            if "wav" in elem:
                file_names.append(elem)
    return file_names

def create_df(zip_file, file_names):
    df = pd.DataFrame(file_names, columns=["File Path"])
    df['File Path'] = df['File Path'].apply(lambda x: zip_file.split(".")[0] + "/" + x) 
    df['Type of SNR'] = df['File Path'].apply(lambda x: x.split("/")[1])
    df['Type of Machine'] = df['File Path'].apply(lambda x: x.split("/")[2])
    df['Model Number'] = df['File Path'].apply(lambda x: x.split("/")[3])
    df['Status'] = df['File Path'].apply(lambda x: x.split("/")[4])
    df['File Name'] = df['File Path'].apply(lambda x: x.split("/")[5])
    return df


start_time = time.time()
zip_file = input("Enter file path: ")
file_names = get_filenames(zip_file)
df = create_df(zip_file, file_names)
df.to_csv(f'{zip_file.split(".")[0]}_filepath.csv', index=False)
end_time = time.time()
print(f"Successfully created the filepath csv for {zip_file.split('.')[0]}")
print(f"Program runs for {end_time - start_time} seconds.")

