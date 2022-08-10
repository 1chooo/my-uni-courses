%%  Value

a = [9 -5 3 7];
x = -2: 0.01: 5;
f = polyval(a, x);

plot(x, f, 'LineWidth', 2);
xlabel('x');
ylabel('f(x)');
set(gca, 'Fontsize', 14);

%%  derivative

a = [5 0 -2 0 1];

polyder(a);
polyval(polyder(a), 7);

%%  ex1

u = [5 -7 5 10];
v = [4 12 -3];
w = conv(u, v);
x = -2: 0.01: 1;
f = polyval(w, x);
a = polyder(w);
y = polyval(a, x);

hold on
plot(x, f, 'b--', 'LineWidth', 2);
plot(x, y, 'r'  , 'LineWidth', 2);
hold off

xlabel('x');
legend('f(x)', 'f\prime(x)');

%%  integral

p = [5 0 -2 0 1];
polyint(p, 3);
polyval(polyint(p, 3), 7);

%%  diff

x = [1 2 5 2 1];
diff(x);

%%  ex2

x = [1 2];
y = [5 7];

slope = diff(y) ./ diff(x);

%%  ex3

for i = 1: 7
    i = i + 1;
    x0 = pi/2;
    x = [x0 x0+h];
    y = [sin(x0) sin(x0+h)];
    h = 0.1^i;
    
    m(i) = diff(y) ./ diff(x);
    disp(m(i));
end

%%

h = 0.5
x = 0: h: 2*pi;
y = sin(x);
w = polyder(y);

disp(w);

%%

x = 0: 0.01: 2*pi;
y = sin(x);
m = diff(y)./ diff(x);

hold on
plot(x, y);
plot(x(1: end-1), m);   % m為間隔 -1
hold off

set(gca, 'XLim', [0, 2*pi]);
set(gca, 'XTick', 0:pi/2:2*pi);
set(gca, 'YTick', [-1, 2]);
set(gca, 'XTickLabel', {'0', '\pi/2', '\pi', '3\pi/2', '2\pi'});
set(gca, 'Fontsize', 12);

xlabel('x');
legend('sin(x)', 'sin\prime(x)');

%%

