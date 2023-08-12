% Farhrenheit to Celsius

function F2C

F = input('Temperature in F :');
while isempty(F) == 0
    if F == 0
        break
    else
        C = (F-32) * 5/9;
        disp(['==>Temperature in C = ', num2str(C)])
        F = input('Temperature in F :');
    end
end