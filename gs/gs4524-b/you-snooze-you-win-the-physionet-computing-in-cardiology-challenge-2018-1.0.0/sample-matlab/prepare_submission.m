% prepare_submission: This file illustrates how to prepare an entry
% for the PhysioNet/CinC 2018 Challenge.  It first trains a classifier
% for each record in the training set, then runs the classifiers over
% each record in both the training and test sets. The results from the
% training set are used to calculate scores (the average AUROC and
% average AUPRC), and the results from the test set are saved as .vec
% files for submission to PhysioNet.
%
% Written by Mohammad Ghassemi and Benjamin Moody, 2018

% PLEASE NOTE: The script assumes that you have downloaded the data, and is meant
%             to be run from the directory containing the '/training' and '/test'
%             subdirectories

clear all

% STEP 0: Get information on the subject files
[headers_tr, headers_te] = get_file_info;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% STEP 1: For each of the training subjects, let's build a model.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for i = 1:length(headers_tr)
        display('--------------------------------------------------')
        display(['Working on Subject ' num2str(i) '/' num2str(length(headers_tr))])
        train_classifier(headers_tr{i});
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% STEP 2: Apply the models to the training set, and check performance
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Initialize scoring function
score2018();

for i = 1:length(headers_tr)
        display('---------------------------------------------------------------')
        display(['Evaluating Models on Training Subject ' num2str(i) '/' num2str(length(headers_tr))])
        predictions = run_classifier(headers_tr{i});

        data = parse_header(headers_tr{i});
        arousal = load(data.arousal_location); arousal = arousal.data.arousals;

        % Calculate AUPRC and AUROC scores
        [auprc_g, auroc_g, auprc_r, auroc_r] = score2018(arousal, predictions);

        display(['Gross AUROC (so far): ' num2str(auroc_g)]);
        display(['Gross AUPRC (so far): ' num2str(auprc_g)]);
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% STEP 3: Apply the models to the testing set, and save .vec files
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for i = 1:length(headers_te)
        display('--------------------------------------------------')
        display(['Scoring Test Subject ' num2str(i) '/' num2str(length(headers_te))])
        predictions = run_classifier(headers_te{i});

        % Save the predictions for submission to the challenge
        display(['Saving predictions'])
        [~, recbase, ~] = fileparts(headers_te{i});
        fileID = fopen([recbase '.vec'], 'w');
        fprintf(fileID, '%.3f\n', predictions);
        fclose(fileID);
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% STEP 4: Generate a zip file for submission to PhysioNet
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Delete any files if they existed previously
delete('entry.zip');
% Note: this will not package any sub-directories!
zip('entry.zip', {'*.m', '*.c', '*.mat', '*.vec', '*.txt', '*.sh'});
