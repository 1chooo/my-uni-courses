%%  imagesc

subplot(1, 2, 1);
[x, y] = meshgrid(-3: .2: 3, -3: .2: 3);
z = x .^ 2 + x .* y + y .^2;
surf(x, y, z);
box on;
set(gca, 'Fontsize', 16);
xlabel('x');    xlim([-4 4]);
ylabel('y');    ylim([-4 4]);
zlabel('z');

subplot(1, 2, 2);
imagesc(z);
axis square;
xlabel('x');
ylabel('y');
colorbar;

% colormap(cool);
% colormap(hot);
% colormap(gray);

%%  ex6

x = [1: 10; 3: 12; 5: 14];
imagesc(x);
colorbar;

map = zeros(256, 3);
map(:, 2) = (0: 255) / 255;
colormap(map);

%%  sin

x = 0: 0.1: 2*pi;
plot(x, sin(x));

%%  plot3

x  = 0: 0.1: 3*pi;
z1 = sin(x);            z2 = sin(2 .* x);   z3 = sin(3 .* x);
y1 = zeros(size(x));    y3 = ones(size(x)); y2 = y3 ./ 2;

plot3(x, y1, z1, 'r', x, y2, z2, 'b', x, y3, z3, 'g');
grid on;
xlabel('x-axis');
ylabel('y-axis');
zlabel('z-axis');

%%  more plot3

subplot(1, 2, 1);
t = 0: pi/50: 10*pi;
plot3(sin(t), cos(t), t);
grid on;

subplot(1, 2, 2);
turns = 40*pi;
i = linspace(0, turns, 4000);
x = cos(i) .* (turns - i) ./ turns;
y = sin(i) .* (turns - i) ./ turns;
z = i ./ turns;

plot3(x, y, z);
grid on;
axis square;

%%

x = -2: 1: 2;
y = -2: 1: 2;
[X, Y] = meshgrid(x, y);

%%  mesh(c) & surf(c)

x = -3.5: 0.2: 3.5;
y = -3.5: 0.2: 3.5;

[X, Y] = meshgrid(x, y);
Z = X .* exp(-X .^ 2 - Y .^ 2);

subplot(2, 2, 1);   mesh(X, Y, Z);
subplot(2, 2, 2);   surf(X, Y, Z);
subplot(2, 2, 3);   meshc(X, Y, Z);
subplot(2, 2, 4);   surfc(X, Y, Z);

%%  contour

x = -3.5: 0.2: 3.5;
y = -3.5: 0.2: 3.5;
[X, Y] = meshgrid(x, y);
Z = X .* exp(-X .^ 2 - Y .^ 2);

subplot(1, 2, 1);   mesh(X, Y, Z);      axis square;
subplot(1, 2, 2);   contour(X, Y, Z);   axis square;

