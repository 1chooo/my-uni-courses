%%  Various Contour Plots

x = -3.5: 0.2: 3.5;
y = -3.5: 0.2: 3.5;
[X, Y] = meshgrid(x, y);
Z = X .* exp(-X .^ 2 - Y .^ 2);

subplot(1, 3, 1);   contour(Z, [-.45: .05: .45]);   axis square;
subplot(1, 3, 2);   [C, h] = contour(Z);    clabel(C, h);   axis square;
subplot(1, 3, 3);   contourf(Z);    axis square;

%%  ex7

x = -2.0: 0.2: 2.0;
y = -2.0: 0.2: 2.0;
[X, Y] = meshgrid(x, y);
Z = X .* exp(-X .^ 2 - Y .^ 2);

hold on
contourf(Z);    
[C, h] = contour(Z, [-.45: .05: .45]);    
clabel(C, h);   
hold off

set(gca, 'XTickLabel', -2: 1: 2);
set(gca, 'YTickLabel', -2: 0.5: 2);
axis square;
colorbar;

%%  view

sphere(50);
shading flat;
light('Position', [1 3 2]);
light('Position', [-3 -1 3]);
material shiny;
axis vis3d off;
set(gcf, 'Color', [1 1 1]);

% view(-45, 20)

%%  light

[X, Y, Z] = sphere(64);
h = surf(X, Y, Z);
axis square vis3d off;
reds = zeros(256, 3);
reds(:, 1) = (0: 256.-1)/255;
colormap(reds);
shading interp;
lighting phong;
set(h, 'AmbientStrength', 0.75, 'DiffuseStrength', 0.5);
L1 = light('Position', [-1, -1, 1]);

% set(L1, 'Position', [-1 -1 1]);
% set(L1, 'Color', 'g');

%%  patch

v = [0 0 0; 1 0 0; 1 1 0; 0 1 0; 0.25 0.25 1; ...
    0.75 0.25 1; 0.75 0.75 1; 0.25 0.75 1];
f = [1 2 3 4; 5 6 7 8; 1 2 6 5; 2 3 7 6; 3 4 7 8; 4 1 5 8];

subplot(1, 2, 1);
patch('Faces', f, 'Vertices', v, ...
    'FaceVertexCData', hsv(6), 'FaceColor', 'flat');
view(3);
axis square tight;
grid on;

subplot(1, 2, 2);
patch('Faces', f, 'Vertices', v, ...
    'FaceVertexCData', hsv(8), 'FaceColor', 'interp');
view(3);
axis square tight;
grid on;

%%  ex8

load cape
X = conv2(ones(9, 9)/81, cumsum(cumsum(randn(100, 100)), 2));
surf(X, 'EdgeColor', 'none', 'EdgeLighting', 'Phong', ...
    'FaceColor', 'interp');

colormap(map);
caxis([-10, 300]);
grid off;
axis off;