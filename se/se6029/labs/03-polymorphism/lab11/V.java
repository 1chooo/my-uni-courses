public class V {
    public static void main(String[] args) {
        // 弦樂四重奏
        Instrument[] stringQuartet = { new Violin(), new Violin(), new Viola(), new Cello() };
        // play the music for me
        for (Instrument instrument : stringQuartet) {
            instrument.play();
        }
    }
}

abstract class Instrument {
    abstract public void play();
}

// 小提琴
class Violin extends Instrument {
    @Override
    public void play() {
        System.out.println("旋律");
    }
}

// 中提琴
class Viola extends Instrument {
    @Override
    public void play() {
        System.out.println("合旋");

    }
}

// 大提琴
class Cello extends Instrument {
    @Override
    public void play() {
        System.out.println("低音");

    }
}