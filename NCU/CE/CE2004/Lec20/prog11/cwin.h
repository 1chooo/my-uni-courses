class CWin
{
    protected :
        char id;
        int width;
        int height;

    public :
        CWin(char ch, int w, int h) : id(ch), width(w), height(h)
        {}

        void show(void);
};