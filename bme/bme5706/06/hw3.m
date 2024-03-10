%%  Stairs & Stem Chart

x = linspace(0, 4*pi, 40);
y = sin(x);

subplot(1, 2, 1);   stairs(y);
subplot(1, 2, 2);   stem(y);

%%  ex4

t = 0: 0.2: 10 ;
t1 = 0: 0.01: 10;
y = sin((pi .* (t .^ 2)) / 4);
y1 = sin((pi .* (t1 .^ 2)) / 4);

hold on
plot(t1, y1);
stem(t, y);
hold off

title('5Hz');

%%  Boxplot

load carsmall
boxplot(MPG, Origin);

%%  Error Bar

x = 0: pi/10: pi;
y = sin(x);
e = std(y)*ones(size(x));

errorbar(x, y, e);

%%  Fill

t = (1: 2: 15) .* pi/8;
x = sin(t);
y = cos(t);

fill(x, y, 'r');
axis square off;
text(0, 0, 'STOP', 'Color', 'w', 'Fontsize', 80, ...
    'Fontweight', 'bold', 'HorizontalAlignment', 'center');
title('Stop Sign');

%%  ex5

t = (1: 1: 4) .* pi/2;
x = sin(t);
y = cos(t);

fill(x, y, 'y', 'LineWidth', 5.0);
axis square off;
text(0, 0, 'WAIT', 'Color', 'k', 'Fontsize', 80, ...
    'Fontweight', 'bold', 'HorizontalAlignment', 'center');
title('Wait Sign');

%%  Medal

G = [46 38 29 24 13];
S = [29 27 17 26  8];
B = [29 23 10 32  7];

h = bar(1: 5, [G' S' B']);
h(1).FaceColor = [230/255, 184/255, 000/255];
h(2).FaceColor = [191/255, 191/255, 181/255];
h(3).FaceColor = [184/255, 115/255, 051/255];

xlabel('Country')
ylabel('Number of Medals');
set(gca, 'XTickLabel', {'USA', 'CHN', 'GBR', 'RUS', 'KOR'});
title('Metal count for top 5 countries in 2012 Olympics');
legend('Gold', 'Silver', 'Bronze')

