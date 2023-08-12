%%  Logarithm Plots

x = logspace(-1, 1, 100);
y = x .^ 2;

subplot(2, 2, 1);   plot(x, y);     title('Plot');
subplot(2, 2, 2);   semilogx(x, y); title('Semilogx');
subplot(2, 2, 3);   semilogy(x, y); title('Semilogy');
subplot(2, 2, 4);   loglog(x, y);   title('Loglog');

set(gca, 'Xgrid', 'on');    %   only subplot(2, 2, 4)

%%  Plotyy 兩個y軸

x = 0: 0.01: 20;
y1 = 200*exp(-0.5*x) .* sin(x);
y2 = 0.8*exp(-0.5*x) .* sin(10*x);
[AX, H1, H2] = plotyy(x, y1, x, y2);

set(get(AX(1), 'Ylabel'), 'String', 'Left Y-axis')
set(get(AX(2), 'Ylabel'), 'String', 'Right Y-axis')
set(H1, 'LineStyle', '--');
set(H2, 'LineStyle', ':');

title('Labeling plotyy');

%%  Histogram

y = randn(1, 1000);

subplot(2, 1, 1);   hist(y, 10);    title('Bins = 10');
subplot(2, 1, 2);   hist(y, 50);    title('Bins = 50');

%%  Bar Chart

x = [1 2 5 4 8];
y = [x; 1: 5];

subplot(1, 3, 1);   bar(x);     title('A bargraph of vector x');
subplot(1, 3, 2);   bar(y);     title('A bargraph of vector y');
subplot(1, 3, 3);   bar3(y);    title('A 3D bargraph');

%%  Stacked & Horizontal

x = [1 2 5 4 8];
y = [x; 1: 5];

subplot(1, 2, 1);   bar(y, 'stacked');  title('Stacked');
subplot(1, 2, 2);   barh(y);            title('Horizontal');

%%  ex1

x = [1 2 5 4 8];
y = [x; 1: 5];

barh(y, 'stacked');            title('Horizontal add stacked');