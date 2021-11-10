using System;

namespace HanoiTowers
{
    class Program
    {
        /*
        n: number of disks
        f: 'from' position
        h: 'helper' position
        t: 'target' position
        */
        static void Main(string[] args)
        { 
            //           n  f  t  h
            TowerofHanoi(3, 1, 3, 2);
        }
        public static void TowerofHanoi(int n, int f, int t, int h)
        {
            if (n == 1)
            {
                System.Console.WriteLine("Move disk from pole " + f + " to pole " + t);
            }
            else
            {
                TowerofHanoi(n - 1, f, h, t);
                TowerofHanoi(1, f, t, h);
                TowerofHanoi(n - 1, h, t, f);
            }
        }
    }
}
