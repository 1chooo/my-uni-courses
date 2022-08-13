implicit none
!------------------------------------------
!20201210: To process sounding data;
!------------------------------------------

! integer i
! integer j
! integer k
! integer hght ! height;
! integer relh ! relative humidity;
! integer drct ! wind direction;
! integer sknt ! wind speed in knot;
integer ilinein
integer len_trim
! real pres ! pressure;
! real temp ! temperature;
! real dwdt ! dew point temperature;
! real mixr ! mixing ratio for water vapor;
! real thta ! potential temperature;
! real thte ! equivalent potential temperature;
! real thtr ! virtual equivalent temperature;
character*100 linein! name string long 100 -> linein

!-------------------------------------------

open(1, file = '47918.txt', form = 'formatted') ! open, name 47918.txt -> 1 by formatted form;
10 continue
read(1, '(a)', end = 20) linein ! read 1 by form(a) -> linein;
ilinein = len_trim(linein) ! 
print *, 'ilinein=', ilinein
print *, linein(1:ilinein)
goto 10
20 continue
close(1)

stop
end
