% Author Mohammad M. Ghassemi, MIT
% -- April 8, 2018 --
% This function imports information about the training and testing
% set data for the 2018 PhysioNet Challenge. Specifically, it searches
% through the 'training' and 'test' subdirectories, and returns a list
% of header files found in each subdirectory.

% PLEASE NOTE: The script assumes that you have downloaded the data, and is meant
%             to be run from the directory containing the '/training' and '/test'
%             subdirectories

function [headers_tr, headers_te] = get_file_info()

% STEP 1: Collet the location of the training and testing files.
tr_subdir = dir('training');
te_subdir = dir('test');

% toss directories
tr_subdir(~[tr_subdir.isdir]) = [];
te_subdir(~[te_subdir.isdir]) = [];

% keep only the directory names
tr_subdir = {tr_subdir.name};
te_subdir = {te_subdir.name};

% remove '.' and '..' directories
tr_subdir = tr_subdir(3:end);
te_subdir = te_subdir(3:end);

% STEP 2: Get the files for all the training subjects
for i = 1:length(tr_subdir)
        this_subject = tr_subdir{i};
        this_subject_files = dir(['training/' this_subject]);
        this_subject_files([this_subject_files.isdir]) = [];
        this_subject_files = {this_subject_files.name};

        header_ind = find(contains(this_subject_files,'.hea'));
        headers_tr{i} = ['training/' this_subject '/' this_subject_files{header_ind}];
end

% STEP 3: Get the files for all the testing subjects
for i = 1:length(te_subdir)
        this_subject = te_subdir{i};
        this_subject_files = dir(['test/' this_subject]);
        this_subject_files([this_subject_files.isdir]) = [];
        this_subject_files = {this_subject_files.name};

        header_ind = find(contains(this_subject_files,'.hea'));
        headers_te{i} = ['test/' this_subject '/' this_subject_files{header_ind}];
end
