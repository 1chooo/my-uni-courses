%%

for i = 1:10
    x = linspace(0, 10, 101);
    plot(x, sin(x+i));
    print(gcf, '-deps', strcat('plot', num2str(i), '.ps'));
   
end

%%

a = 3;
if rem(a, 2) == 0
    disp('a is even')
else 
    disp('a is odd')
end

%%

input_num = 1;
switch input_num
    case -1
        disp('negative 1')
    case 0 
        disp('zero')
    case 1 
        disp('positive 1')
    otherwise
        disp('other value')
end  

%%

n = 1;
while prod(1:n) < 1e100
    n = n + 1;
end

%%

n = 1;
sum = 1;
while n < 999    % 要999因為 n = n + 1 代表998會再+1
    n = n + 1; 
    sum = sum + n
end

print(sum)

%%

for n = 1:2:10
    a(n) = 2 ^ n
    a(a==0)=[]    % a==0是為了判斷a出現0的地方要以[]取代
end

%%