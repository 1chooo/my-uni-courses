        program upair
        implicit none
        integer i,j,k,n,a
        real,dimension(20000) :: Si,P,H,Tx,Td,Wd,Ws,RH
        integer,dimension(20000) ::stn,date
        character*10 :: aa,bb,cc
        integer :: station,time
        
        station=466920!想讀的測站
        time=2021010100!想讀的時間
        !打開要畫的資料
        open(10,file='202101_upair.txt')

        do i=1,13 !省略文字敘述
                read(10,*)
        enddo

        !讀取的層數
        n=13014 !總共資料多少行

        do i=1,n 
                read(10,*)stn(i),date(i),si(i),p(i),h(i),tx(i),td(i),wd(i),ws(i),rh(i)
        enddo
        
        write(cc,'(I2)') a
        !寫入二進位檔    
        a=0    
        do i=1,n
                if(stn(i)==station) then
                if(date(i)==time) then
                      a=a+1
                endif
                endif
        enddo
 
        write(bb,'(I6)') station
        write(cc,'(I10)') time
        open(20,file=''//cc//'.dat',status='unknown',&
                         &form='unformatted',access='direct',recl=4*a)
        open(25,file=''//cc//'.txt')
        do i=1,n
               
                if (stn(i)==station .and.date(i)==time) then

                    k=i
                        write(20,rec=1)(tx(i),i=k,k-1+a)
                        write(20,rec=2)(td(i),i=k,k-1+a)
                        write(20,rec=3)(ws(i),i=k,k-1+a)
                        write(20,rec=4)(wd(i),i=k,k-1+a)
                        write(20,rec=5)(rh(i),i=k,k-1+a)
                endif
        enddo
        
        write(aa,'(i3)') a
 
        !寫入ctl檔
        open(30,file=''//cc//'.ctl')
        write(30,*)'dset  ./'//cc//'.dat'
        write(30,*)'undef  999.9'
        write(30,*)'title 2021010100'
        write(30,*)'xdef 1 linear   0 1'
        write(30,*)'ydef 1 linear   0 1'
        write(30,*)'zdef '//aa//' levels  '
        write(30,*)(p(i),i=k,k-1+a)
        write(30,*)'tdef 1  linear 00z01jan2021 1hr'!改日期
        write(30,*)'vars  5'
        write(30,*)'tx   '//aa//' 99 temperature'
        write(30,*)'td   '//aa//' 99 Dew point temperature'
        write(30,*)'ws   '//aa//' 99 wind speed'
        write(30,*)'wd   '//aa//' 99 wind direction'
        write(30,*)'rh   '//aa//' 99 relative humidity'
        write(30,*)'endvars'

        close(30)

        !剖面圖        
        open(40,file='plot.gs')
        write(40,*)'''reinit'''
        write(40,*)'''set background 1'''
        write(40,*)'''c'''
        write(40,*)'''open '//cc//'.ctl'''
        write(40,*)'''set t 1'''
        write(40,*)'''set x 1'''
        write(40,*)'''set y 1'''
        write(40,*)'''set lev 1030 150'''
        write(40,*)'''set timelab off'''
        write(40,*)'''set grads off'''
        write(40,*)'''set zlog on'''
        write(40,*)'''d tx'''
        write(40,*)'''gxprint '//cc//'.png'''

        !斜溫圖    
        open(50,file='skew.gs')
        write(50,*)'''reinit'''
        write(50,*)'''set background 1'''
        write(50,*)'''c'''
        write(50,*)'''open '//cc//'.ctl'''
        write(50,*)'''set t 1'''
        write(50,*)'''set x 1'''
        write(50,*)'''set y 1'''
        write(50,*)'''set lev 1030 150'''
        write(50,*)'''plotskew.gs'''
        write(50,*)'''gxprint '//cc//'_skew.png'''
        

        stop
        end
