%%

I = imread('pout.tif');
imshow(I);

for i = 1: size(I, 1)
    for j = 1: size(I, 2)
        if rem(i, 2) == 0 && rem(j, 2) == 0
            I(i, j) = 0
        end
    end
end

%%

I = imread('rice.png');
subplot(1, 2, 1);   imshow(I);
J = immultiply(I, 1.5); % (i, j) j adjust pixel
subplot(1, 2, 2);   imshow(J);

%%

I = imread('rice.png');
J = imread('cameraman.tif');
K = imadd(I, J);    % Cross

subplot(1, 3, 1);   imshow(I);
subplot(1, 3, 2);   imshow(J);
subplot(1, 3, 3);   imshow(K);

%%

