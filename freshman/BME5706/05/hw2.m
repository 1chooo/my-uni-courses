%%  Graphical Objects

x = linspace(0, 2*pi, 1000);
y = sin(x);
plot(x, y);
set(gcf, 'Color', [1, 1, 1]);

%%  Handle

x = linspace(0, 2*pi, 1000);
y = sin(x);
plot(x, y);
h = plot(x, y);

set(gca, 'XLim', [0, 2*pi]);
set(gca, 'YLim', [-1.2, 1.2]);
set(gca, 'Fontsize', 25);
% set(gca, 'XTick', 0:pi/2:2*pi);
% set(gca, 'XTickLabel', 0:90:360);
set(gca, 'FontName', 'symbol');
set(gca, 'XTickLabel', {'0', 'pi/2', 'pi', '3pi2', '2pi'});
get(h);   
% get(gca); % axis
% get(gcf); % figure
set(h, 'LineStyle', '-.', 'LineWidth', 7.0, 'Color' , 'g');

%%  Marker Specification

x = rand(20, 1);
set(gca, 'Fontsize', 18);
plot(x, '-md', 'LineWidth', 2, 'MarkerEdgecolor', 'k',...
    'MarkerFaceColor', 'g', 'MarkerSize', 10);
xlim = ([1, 20]);

%%  Mini Assignment #2

t = linspace(1, 2);
f = t.^2;
g = sin(2*pi.*t);

%   用以描繪多條函數
hold on
plot(t, f, 'k', 'LineWidth', 4.0);
plot(t, g, 'o', 'MarkerFaceColor', [1, 0.4, 0.6], 'MarkerSize', 5);
hold off

%   Axis
set(gca, 'XLim', [1.0, 2.0]);
set(gca, 'YLim', [-1.0, 4.0]);
set(gca, 'Fontsize', 20);

%   Label & Title
xlabel('Time(ms)', 'Fontsize', 20); 
ylabel('f(t)', 'Fontsize', 20);
title('Mini Assignment #2', 'Fontsize', 20);

%   Legend
legend('t^2', 'sin(2 \pi t)','Location','northwest', 'Fontsize', 20);