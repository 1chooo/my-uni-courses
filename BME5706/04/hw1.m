%% reverse the order

s1 = 'I like the letter E';
s2 = reverse(s1);   

%% field

field = 'student';

student(1).name   = 'Ho'; 
student(1).id     = 'lcho@g.ncu.edu.tw';
student(1).number = 109601003;
student(1).grade  = [100, 75, 73; 95, 91, 85.5; 100, 98, 72];

student;
student(2).name   = 'HoHo'; 
student(2).id     = 'hugo970217@g.ncu.edu.tw';
student(2).number = 109601003;
student(2).grade  = [95, 100, 90; 95, 82, 97; 100, 98, 72];

%% Cell

B(1, 1) = {[1 4 3; 0 5 8; 7 2 9]};
B(1, 2) = {'Ho'};
B(2, 1) = {3 + 7i};
B(2, 2) = {-pi: pi: pi};

B;

%% Cell ex

C{1, 1} = 'This is the first cell';
C{1, 2} = [5 + 1j*6 4 + 1j*5];
C{2, 1} = [1 2 3; 4 5 6; 7 8 9];
C{2, 2} = {'Tim', 'Chris'};

C;

%% reshape ex

d = [1:3; 4:6];
D = reshape(d, 3, 2);

