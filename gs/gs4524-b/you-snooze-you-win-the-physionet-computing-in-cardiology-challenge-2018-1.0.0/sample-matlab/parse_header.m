% Author Mohammad M. Ghassemi, MIT
% -- April 8, 2018 --
% This function imports information about the training and testing
% set data for the 2018 PhysioNet Challenge. Specifically, it reads a
% header file and returns a matlab structure containing:
%     - subject id
%     - signal sampling rate
%     - number of samples
%     - location of the signals file
%     - location of the arousal annoataions (for training set)

function data = parse_header(header_file_name)
        % Import the header file
        fid = fopen(header_file_name,'rt');
        raw_header = textscan(fid,'%s','Delimiter','\n');
        raw_header = raw_header{1};
        fclose(fid);

        % Process the first row of the header file
        header_first_row = strsplit(raw_header{1}, ' ');
        data.subject_id = header_first_row{1};
        data.fs = header_first_row{3};
        data.n_samples = header_first_row{4};

        % Extract the signal names from the remainder of the file.
        for j = 2:length(raw_header)
                header_row = strsplit(raw_header{j}, ' ');
                signal_names{j-1} = header_row{end};
        end
        data.signal_names = signal_names;

        % Extract the signal location
        [rec_dir, rec_name, ~] = fileparts(header_file_name);
        data.signal_location = [rec_dir filesep rec_name '.mat'];
        data.arousal_location = [rec_dir filesep rec_name '-arousal.mat'];
