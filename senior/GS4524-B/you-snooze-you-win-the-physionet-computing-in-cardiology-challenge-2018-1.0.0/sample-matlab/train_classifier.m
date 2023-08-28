% run_classifier: This function takes a single record from the
% challenge training set, and uses that record together with the
% accompanying arousal annotations to tune model parameters
% appropriately. You may want to use this function as a basis for your
% own training code.
%
% Written by Mohammad Ghassemi and Benjamin Moody, 2018

function train_classifier(header_file_name)
        % Read record info from the header file
        data = parse_header(header_file_name);

        X_tr = []; Y_tr = [];

        %load all the the data associated with this subject
        signals      = load(data.signal_location); signals = signals.val;
        arousal      = load(data.arousal_location); arousal = arousal.data.arousals;
        fs           = str2num(data.fs);
        n_samples    = str2num(data.n_samples);
        sid          = data.subject_id;
        signal_names = data.signal_names;

        % select the window size and step size we want to use to
        % compute features
        window_size = 300 * fs;
        window_step = 300 * fs;

        % find the index of the SaO2 signal.
        sao2_ind = find(contains(signal_names,'SaO2'));

        % For each 'window', extract the variance of the SaO2
        ind = 1;
        for j = 1:window_step:n_samples-window_step
                X_tr(ind) = var(signals(sao2_ind,j:j+window_step));
                Y_tr(ind) = max(arousal(j:j+window_step));
                ind = ind + 1;
        end

        % Set the -1 regions as 1 (treat unscored regions the same as
        % arousals... you may not want to do this.)
        toss = find(Y_tr == -1);
        Y_tr(toss) = 1;

        % Fit a logistic regression for each subject and save their model
        display('Training Model...')
        coeff = glmfit(X_tr,Y_tr','binomial');
        
        % save the model for submission to challenge.i
        display('Saving Model...')
        save([sid '_model'],'coeff');
