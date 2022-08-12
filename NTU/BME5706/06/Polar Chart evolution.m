%%

x = 1: 100;

subplot(2, 2, 1);
theta = x/10;                   rho = log10(x);                 polarplot(theta, rho);

subplot(2, 2, 2);
theta = linspace(0, 2*pi);      rho = cos(4*theta);             polarplot(theta, rho);

subplot(2, 2, 3);
theta = linspace(0, 2*pi, 6);   rho = ones(1, length(theta));   polarplot(theta, rho);

subplot(2, 2, 4);
theta = linspace(0, 2*pi);      rho = 1 - sin(theta);           polarplot(theta, rho);

%%
x = 1: 100;

subplot(2, 2, 1);  
theta = x/10;
rho = log10(x); 
polarplot(theta, rho);

subplot(2, 2, 2);   polarplot(theta, rho);
theta = linspace(0, 2*pi);      rho = cos(4*theta);
subplot(2, 2, 3);   polarplot(theta, rho);
theta = linspace(0, 2*pi, 6);   rho = ones(1, length(theta));

subplot(2, 2, 4);   polarplot(theta, rho);
theta = linspace(0, 2*pi);      rho = 1 - sin(theta);


%%

x = 1: 100;

theta = x/10;
r = log10(x);
subplot(2, 2, 1);
polarplot(theta, r);    

theta = linspace(0, 2*pi);  
r = cos(4*theta);
subplot(2, 2, 2);
polarplot(theta, r);    

theta = linspace(0, 2*pi, 6);   r = ones(1, length(theta));
subplot(2, 2, 3);
polarplot(theta, r);    

theta = linspace(0, 2*pi);  r = 1 - sin(theta);
subplot(2, 2, 4);
polarplot(theta, r);


%%  Polar chart

x = 1: 100;

subplot(2, 2, 1);
theta = x/10;                   r = log10(x);               polarplot(theta, r);

subplot(2, 2, 2);
theta = linspace(0, 2*pi);      r = cos(4*theta);           polarplot(theta, r); 

subplot(2, 2, 3);
theta = linspace(0, 2*pi, 6);   r = ones(1, length(theta)); polarplot(theta, r);  

subplot(2, 2, 4);
theta = linspace(0, 2*pi);      r = 1 - sin(theta);         polarplot(theta, r);
