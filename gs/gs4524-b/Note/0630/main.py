import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import wfdb
import os
import mat73
import scipy.io

test_path = 'c:\\2023_Fall\\GS4524\\G1\\Physionet\\test'
train_path = 'c:\\2023_Fall\\GS4524\\G1\\Physionet\\training'

def load_data(dir_path, record_name):
    
    record_path = os.path.join(dir_path, record_name, record_name)
    record = wfdb.rdrecord(record_path)
    arousal = wfdb.rdann(record_path, 'arousal')

    record_path = os.path.join(dir_path, record_name, f'{record_name}-arousal.mat')
    aasmlabel = mat73.loadmat(record_path)

    # del record, arousal, aasmlabel
    
    return record, arousal, aasmlabel

record_name = 'tr03-1010'

record, arousal, aasmlabel = load_data(train_path, record_name)

def get_ecg_data(record):
    ecg_data = record.p_signal[:, -1]

    return ecg_data

ecg_data = get_ecg_data(record)
sampling_rate = 200

def plot_ecg_data(ecg_data, sampling_rate, output_path):
    
    time = np.arange(len(ecg_data)) / sampling_rate

    plt.figure(figsize=(10, 4))
    plt.plot(time, ecg_data)
    plt.title('ECG')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.savefig(output_path)
    plt.close()

def get_folder_names(folder_path):
    folder_names = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            folder_names.append(item)
    return folder_names

train_folder_list = get_folder_names(train_path)
test_folder_list = get_folder_names(test_path)

# print('Train Length:', len(train_folder_list), train_folder_list)
# print('Test Length:', len(test_folder_list), test_folder_list)

def plot_train_ecg(dir_path, sampling_rate, folder_list):

    for i in range(len(folder_list)):
        record, arousal, aasmlabel = load_data(dir_path, folder_list[i])
        ecg_data = get_ecg_data(record)
        output_path = 'c:\\2023_Fall\\GS4524\\G1\\Physionet\\imgs\\train\\'
        output_path += str(folder_list[i])
        output_path += '.jpg'
        plot_ecg_data(ecg_data, sampling_rate, output_path)
        del record, arousal, aasmlabel

plot_train_ecg(train_path, sampling_rate, train_folder_list)