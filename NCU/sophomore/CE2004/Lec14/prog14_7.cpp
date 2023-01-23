 #include <iostream>
 #include <cstdlib>

 using namespace std;

 class CWin
 {
    private :
        char id;
        int width, height;

    public :
        CWin(char i, int w, int h) : id(i), width(w), height(h)
        {
            cout << "The constructor has been called..." << endl;
        }

        CWin(const CWin &win)
        {
            cout << "The duplicated constructor has been called..." << endl;
            id = win.id;
            width = win.width;
            height = win.height;
        }

        void showMember(void)
        {
            cout << "Window " << id << ": ";
            cout << "width = " << width << ", height = " << height << endl;
        }
 };

 int main(void)
 {
    CWin win1('A', 50, 40);
    CWin win2(win1);

    win1.showMember();
    win2.showMember();

    system("pause");

    return 0;
 }