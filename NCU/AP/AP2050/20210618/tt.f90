implicit none
!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
! To produce a square wave;
!
integer i
integer j
integer k
integer plon
parameter (plon=361)
real p(plon)
real pai    !3.14;
real d2r    !degree to radium;   pi/180;
real x(plon)
real y(plon)   !summation of all wave;
real term1  !4/pai;
real n
real L      !pai;
!
!
real vlo
real vro
real vbo
real vto
real vli
real vri
real vbi
real vti
real xl
real xr
real yb
real yt
!
call opngks

call gscr(1,6,1.00,0.00,0.00) 
call gscr(1,7,0.00,1.00,0.00) 
call gscr(1,8,0.00,0.00,1.00) 
call gscr(1,9,0.00,0.00,0.00) 
call gscr(1,10,1.00,1.00,1.00) 
call setusv('LW',3000)


pai=acos(-1.)
d2r=pai/180.

!* initialization;
do i=1,plon
y(i)=0.
enddo


vlo=0.00
vro=1.00
vbo=0.00
vto=1.00
vli=0.15
vri=0.85
vbi=0.15
vti=0.85
xl=0.0
xr=float(plon)
yb=-1.5
yt=1.5

L=pai
term1=4./pai

call set(vli,vri,vbi,vti,xl,xr,yb,yt,1)
!open a channel to output data for grads analysis;
open(1,file='square_wave.data',form='unformatted')

j=0
do 100 k=1,36,2
j=j+1
!n=1.
n=float(k)
print*,'wave',j,'wave number n=',n
do i=1,plon
x(i)=float(i-1)  !degree;
p(i)=term1*(1./n)*sin(n*pai*x(i)*d2r/L)
y(i)=y(i)+p(i)
enddo
!output data;
write(1) p

call gsplci(8)   !pl-> plot line  ci->color index;
call gstxci(8)   !tx-> text;
call curve(x,p,plon) ! a single wave;
call gsplci(6)
call gstxci(6)
call curve(x,y,plon) !a summation of all waves;

!call frame
100 continue
call frame
!output data for a summation of all waves;
write(1) y
close(1)
call clsgks
stop
end

