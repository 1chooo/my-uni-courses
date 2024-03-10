%%  Multiple Figures

x = -10: 0.1: 10;
y1 = x .^ 2 - 8;
y2 = exp(x);

figure, plot(x, y1);
figure, plot(x, y2);
figure('Position', [left, bottom, width, height]);

%%  Plot in one figure

t = 0: 0.1: 2*pi;
x = 3*cos(t);
y = sin(t);

subplot(2, 2, 1); plot(x, y); axis normal
subplot(2, 2, 2); plot(x, y); axis square
subplot(2, 2, 3); plot(x, y); axis equal    %   real
subplot(2, 2, 4); plot(x, y); axis equal tight

saveas(gcf, '<filename>', '<formattype>');
