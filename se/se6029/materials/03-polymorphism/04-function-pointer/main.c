Color newColor;
int Cont = 1;

void main() {
    int E = 0;
    struct {
        int (*Draw) (void (*)(), void (*)());
        void (*Move);
        void (*Act);
    } F[] = {
        {gRegion, XorCircle, PutCircle},
        {gRegion, XorCircle, PutPie},
        {gRegion, XorEllipse, PutEllipse},
        {gRegion, XorEllipse, PutEllipsePie},
        {gRegion, XorRect, PutRect},
        {gRegion, XorLine, PutBar},
        {gExit, NULL, NULL}
    };

    if (Initial()) {
        while (Cont) {
            E = GetEvent();
            (*F[E].Draw)(F[E].Move, F[E].Act);
        }
        End();
    }
}