% run_classifier: This function takes a single record from the
% challenge training or test set, and outputs a vector of
% probabilities per sample.  You will need to edit this file to suit
% your algorithm.
%
% Written by Mohammad Ghassemi and Benjamin Moody, 2018

function predictions = run_classifier(header_file_name)
        % Read record info from the header file
        data = parse_header(header_file_name);

        X_te = [];

        % collect a list of all the trained models
        files = dir(); files = {files.name};
        models = find(contains(files,'_model'));

        % load all the the data associated with this subject
        signals      = load(data.signal_location); signals = signals.val;
        fs           = str2num(data.fs);
        n_samples    = str2num(data.n_samples);
        sid          = data.subject_id;
        signal_names = data.signal_names;

        % select the window sie and step size we want to use to
        % compute features
        window_size = 300 * fs;
        window_step = 300 * fs;

        % find the index of the SaO2 signal.
        sao2_ind = find(contains(signal_names,'SaO2'));

        % For each 'window', extract the variance of the SaO2
        ind = 1;
        for j = 1:window_step:n_samples-window_step
                X_te(ind) = var(signals(sao2_ind,j:j+window_step));
                ind = ind + 1;
        end

        % generate the probability vectors
        display('Generating Scores')
        for k = 1:length(models)
                % loading model
                load(files{models(k)});

                % generate the probability vectors
                pred_short = glmval(coeff,X_te,'logit');
                pred = mean(pred_short)*ones(n_samples,1);
                for j = 1:length(pred_short)
                        paste_in = (j-1)*window_step+1 : j*window_step;
                        pred(paste_in) = pred_short(j)*ones(window_step,1);
                end

                % Compute average of the predictions.
                if k > 1
                        avg_pred = avg_pred + (pred - avg_pred) / (j+1);
                else
                        avg_pred = pred;
                end

        end
        predictions = avg_pred;
