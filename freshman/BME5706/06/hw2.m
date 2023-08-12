%%  Pie chart

a = [10 5 20 30];

subplot(1, 3, 1);   pie(a);
subplot(1, 3, 2);   pie(a, [0, 0, 0, 1]);
subplot(1, 3, 3);   pie3(a, [0, 0, 0, 1]);

%%  ex2

a = [10 5 20 30];

subplot(1, 3, 1);   pie(a);
subplot(1, 3, 2);   pie(a, [1, 1, 1, 1]);
subplot(1, 3, 3);   pie3(a, [1, 1, 1, 1]);

title('Separate all the pieces')

%%  Polar chart

x = 1: 100;

subplot(2, 2, 1);
theta = x/10;                   rho = log10(x);                 polarplot(theta, rho);

subplot(2, 2, 2);
theta = linspace(0, 2*pi);      rho = cos(4*theta);             polarplot(theta, rho);

subplot(2, 2, 3);
theta = linspace(0, 2*pi, 6);   rho = ones(1, length(theta));   polarplot(theta, rho);

subplot(2, 2, 4);
theta = linspace(0, 2*pi);      rho = 1 - sin(theta);           polarplot(theta, rho);

%%  ex3

x = 1: 100;

subplot(2, 2, 1);
theta = x/10;                   rho = log10(x);                 polarplot(theta, rho);

subplot(2, 2, 2);
theta = linspace(0, 2*pi);      rho = cos(4*theta);             polarplot(theta, rho);

subplot(2, 2, 3);
theta = linspace(0, 2*pi, 7);   rho = ones(1, length(theta));   polarplot(theta, rho);
title('Hexagon');

subplot(2, 2, 4);
theta = linspace(0, 2*pi);      rho = 1 - sin(theta);           polarplot(theta, rho);