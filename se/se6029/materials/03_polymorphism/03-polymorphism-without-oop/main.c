Color newColor;     // Currecnt drawing color

void main() {
    int Cont = 1;   // Continue flag
    int Event = 0;  // Event code

    if (Initial()) {    // Enter the drawing mode and other settings
        while (Cont) {
            Event = GetEvent(); // Get the event code
            switch (Event) {    // Determine the event code
                case Circle:
                case Pie:
                case Ellipse:
                case EllipsePie:
                    gCircle(Event, NowColor); // if circle function related, call gCircle function
                    break;
                case Rect:
                case RoundRect:
                case Box:
                    gRect(Event, NowColor); // if rectangle function related, call gRect function
                    break;
                ...

                case Exit:
                    Cont = !gExit();    // if exit function related, call gExit function
                    break;
            }
        End();      // Release memory and exit the drawing mode
        }
    }
}