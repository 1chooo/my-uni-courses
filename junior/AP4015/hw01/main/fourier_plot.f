      PROGRAM PlotData
C
      IMPLICIT NONE
C
      INTEGER :: I
      REAL :: X(365)
C
      OPEN(10, FILE='linu850f.data', FORM='UNFORMATTED')
C
      DO I = 1, 365
         READ(10) X(I)
      END DO
C
      CLOSE(10)
C
      OPEN(20, FILE='plot.gnu', FORM='FORMATTED')
      WRITE(20, *) "set term x11"
      WRITE(20, *) "plot '-' with lines"
      DO I = 1, 365
         WRITE(20, *) I, X(I)
      END DO
      WRITE(20, *) "e"
      CLOSE(20)
C
      CALL SYSTEM("gnuplot plot.gnu")
C
      STOP
      END

