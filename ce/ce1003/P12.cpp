#include <iostream>

using namespace std;

void add (float ax, float ay, float bx, float by, float *cx, float *cy) {
    *cx = (ax + bx);
    *cy = (ay + by);
}

void scale (float ax, float ay, double s, float *cx, float *cy) {
    *cx = (ax * s);
    *cy = (ay * s);
}

int main () {
    float ax, ay, bx, by, cx, cy, s;

    cout << "A: ";
    cin >> ax >> ay;
    cout << "B: ";
    cin >> bx >> by;
    cout << "s: ";
    cin >> s;

    add(ax, ay, bx, by, &cx, &cy);
    cout << "A + B = " << "(" << cx << ", " << cy << ")" << endl;

    scale(ax, ay, s, &cx, &cy);
    cout << "A * s = " << "(" << cx << ", " << cy << ")" << endl;

    return 0;
}
