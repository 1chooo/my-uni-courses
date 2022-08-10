%%  plot

hold on
plot(cos(0: pi/20: 2*pi));
plot(sin(0: pi/20: 2*pi));
hold off

%%  legend

x = 0: 0.5: 4*pi;

y = sin(x); 
h = cos(x); 
w = 1./(1 + exp(-x)); 
g = (1/(2*pi*2)^0.5).*exp((-1.*(x - 2*pi).^2)./(2*2^2));
plot(x, y, 'bd-', x, h, 'gp:', x, w, 'ro-', x, g, 'c^-');

legend('sin(x)', 'cos(x)', 'Sigmoid', 'Gauss function');

%%  title; label

x = 0: 0.1 :2*pi;
y1 = sin(x);
y2 = exp(-x);

plot(x, y1, '--*', x, y2, ':x');

xlabel('t = 0 to 2 \pi');
ylabel('value of sin(t) and e^{-x}');
title('Function Plots of sin(t) and e^{-x}');

legend('sin(t)', 'e^{-x}');

%%  LaTex

x = linspace(0, 3);
y = x .^2.*sin(x);

plot(x, y);
line([2, 2], [0, 2^2*sin(2)]);
str = '$$ \int_{0}^{2} x^2\sin(x) dx $$';
text(0.25, 2.5, str, 'Interpreter', 'latex');
annotation('arrow', 'X', [0.32, 0.5], 'Y', [0.6, 0.4]);

%%  ex

t = linspace(1, 2);
f = t.^2;
g = sin(2*pi.*t);

plot(t, f, 'k', t, g, 'or');

xlabel('Time(ms)'); 
ylabel('f(t)');
title('Mini Assignment #1');

legend('t^2', 'sin(2 \pi t)','Location','northwest');