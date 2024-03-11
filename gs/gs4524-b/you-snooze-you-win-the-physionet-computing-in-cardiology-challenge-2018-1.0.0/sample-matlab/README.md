# Physionet Challenge 2018: Example Submission in Matlab
This repository contains an example submission written in Matlab for the 2018 Physionet Challenge: "You Snooze, You Win". Please note that this code is meant for illustrative purposes only. My aim is to help you understand how to: (1) import the challenge dataset, (2) train models using the data and, (3) generate the output files necessary to grade your algorithm's performance on the test set.

# What the code does
The code imports the SaO2 for each training subject, and uses the variance of the SaO2 in 60 second windows to predict the arousal regions. Importantly, the code trains an ensemble of logistic regression models: one for each subject. To predict arousals, I use the average prediction across all the models. 

# Pre-requisites to run the example submission script
1. Matlab 2017a (or higher)
2. Download the /training and /test data from: https://physionet.org/challenge/2018/
3. Place the files in the same directory as the /training and /test data folders
