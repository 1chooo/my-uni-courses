// RunRunGuineaPigCarCarRace.java

import java.util.ArrayList;
import GuineaPig.GuineaPigCarCar;

public class RunRunGuineaPigCarCarRace {
    // 應該放在 Main 裡面，如此才能做到把參加者加到比賽，而不是直接被綁在比賽裡
    public ArrayList<GuineaPigCarCar> contestants;

    public ArrayList<Integer> distances;

    public RunRunGuineaPigCarCarRace(ArrayList<GuineaPigCarCar> contestants) {
        this.contestants = contestants;
        this.distances = new ArrayList<Integer>();
        this.reset();
    }

    private void reset() {
        this.distances.clear();
        for (int i = 0; i < this.contestants.size(); i++) {
            this.distances.add(0);
        }
    }

    // 跑道長度可能會改
    final static int RUNWAY_LENGTH = 4000;

    // on 1 sec passed
    private void onTime() {
        for (int i = 0; i < contestants.size(); i++) {
            // distances.get(i) += contestants[i].getSpeed();
            distances.set(i, distances.get(i) + contestants.get(i).getSpeed());
        }
    }

    private void on10Sec() {
        int first = 0, last = 0;
        int firstDist = -1, lastDist = RUNWAY_LENGTH;
        for (int i = 0; i < contestants.size(); i++) {
            if (distances.get(i) > firstDist) {
                firstDist = distances.get(i);
                first = i;
            }
            if (distances.get(i) < lastDist) {
                lastDist = distances.get(i);
                last = i;
            }
        }
        contestants.get(first).eat("vegetable");
        contestants.get(last).eat("carrot");
    }

    // Main 來呼叫的
    public void run() {
        int t = 0;
        boolean racing = true;

        this.reset();

        while (racing) {
            for (int d : this.distances) {
                if (d >= RUNWAY_LENGTH) {
                    racing = false;
                    break;
                }
            }

            t = incrementTime(t);
            
            // this.onTime(); <- 先加速再移動
            if (t % 10 == 0) {
                this.on10Sec();
            }
            this.onTime();
        }

        // 比賽結束，印出距離
        for (int i = 0; i < this.contestants.size(); i++) {
            System.out.println(this.contestants.get(i).getName() + ": " + Integer.toString(this.distances.get(i)));
        }

        // 判斷冠軍
        for (int i = 0; i < this.contestants.size(); i++) {
            if (this.distances.get(i) >= RUNWAY_LENGTH) {
                System.out.println("冠軍得主是:" + this.contestants.get(i).getName());
                break;
            } else {
                // do nothing ...
            }
        }
    }

    private int incrementTime(int time) {
        return time + 1;
    }
}
