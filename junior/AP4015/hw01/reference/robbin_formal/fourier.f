C     INCLUDE '/opt/anaconda3/envs/Fortran_env/include/ncarg/ncargC.h'
C
      DIMENSION D(365),NN(3),WORK(730),dm(365)
      COMPLEX A(365),t(365)

      open(20,file='linu850.txt',form='formatted',status='old')
      open(30,file='linu850f.data',form='unformatted',status='unknown')
C
      R365=1./365.
      NN(1)=365
      NN(2)=0
      NN(3)=0
      NDIM=1
      ISIGN=-1
      ISIGP= 1
      IFORM=1
C
C  Read the external file "linu850.txt" identified by 20,
C  and use the specific format indentified by 99, finally store
C  in variabe d/D (case-insensitive in Fortran), means days
      READ(20,99) d
  99  format(10f8.2)
      write(30) d
C
      DO I=1,365
      A(I)=CMPLX(D(I),0.0)
      ENDDO
C
      CALL FOURT(A,NN,NDIM,ISIGN,IFORM,WORK)
      DO I=1,365
      A(I)=A(I)*R365
      t(i)=a(i)
      ENDDO
C
      DO I=1,365
      dm(i)=real(a(1))
      ENDDO
      write(30) dm
C
C  For annual cycle
C
      DO i=1,365
      a(i)=cmplx(0.,0.)
      ENDDO
      a(2)=t(2)
      a(365)=t(365)
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For semi-annual cycle
C
      DO i=1,365
      a(i)=cmplx(0.,0.)
      ENDDO
      a(3)=t(3)
      a(364)=t(364)
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For ~122-day cycle
C
      DO i=1,365
      a(i)=cmplx(0.,0.)
      ENDDO
      a(4)=t(4)
      a(363)=t(363)
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For seasonal cycle
C
      DO i=1,365
      a(i)=cmplx(0.,0.)
      ENDDO
      a(5)=t(5)
      a(362)=t(362)
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For (annual + semi-annual + 122-day + seasonal) cycle
C
      DO i=1,365
      a(i)=cmplx(0.,0.)
      ENDDO
      DO I=1,4
      A(I+1)=t(I+1)
      A(366-I)=t(366-I)
      ENDDO
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For 6-12 cycle
C
      DO i=1,365
      a(i)=cmplx(0.,0.)
      ENDDO
      DO I=6,12
      A(I+1)=t(I+1)
      A(366-I)=t(366-I)
      ENDDO
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For filter out annual cycle
C
      A=t
      a(2)=cmplx(0.,0.)
      a(365)=cmplx(0.,0.)
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For filter out (annual + semi-annual) cycle
C
      A=t
      DO I=1,2
      A(I+1)=cmplx(0.,0.)
      A(366-I)=cmplx(0.,0.)
      ENDDO
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For filter out (annual + semi-annual + 122-day) cycle
C
      A=t
      DO I=1,3
      A(I+1)=cmplx(0.,0.)
      A(366-I)=cmplx(0.,0.)
      ENDDO
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For filter out (annual + semi-annual + 122-day + seasonal) cycle
C
      A=t
      DO I=1,4
      A(I+1)=cmplx(0.,0.)
      A(366-I)=cmplx(0.,0.)
      ENDDO
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For filter out (annual + semi-annual + 122-day + seasonal + 6-12) cycle
C
      A=t
      DO I=1,4
      A(I+1)=cmplx(0.,0.)
      A(366-I)=cmplx(0.,0.)
      ENDDO
      DO I=6,12
      A(I+1)=cmplx(0.,0.)
      A(366-I)=cmplx(0.,0.)
      ENDDO
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For (annual + semi-annual) cycle
C
      DO i=1,365
      a(i)=cmplx(0.,0.)
      ENDDO
      DO I=1,2
      A(I+1)=t(I+1)
      A(366-I)=t(366-I)
      ENDDO
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For (annual + semi-annual + 122-day) cycle
C
      DO i=1,365
      a(i)=cmplx(0.,0.)
      ENDDO
      DO I=1,3
      A(I+1)=t(I+1)
      A(366-I)=t(366-I)
      ENDDO
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
C  For (annual + semi-annual + 122-day + seasonal + 6-12) cycle
C
      DO i=1,365
      a(i)=cmplx(0.,0.)
      ENDDO
      DO I=1,4
      A(I+1)=t(I+1)
      A(366-I)=t(366-I)
      ENDDO
      DO I=6,12
      A(I+1)=t(I+1)
      A(366-I)=t(366-I)
      ENDDO
C
      CALL FOURT(A,NN,NDIM,ISIGP,IFORM,WORK)
C
      DO I=1,365
      D(I)=real(A(I))
      ENDDO
      write(30) d
C
      STOP
      END
