using System.Linq;
public static int r4(bool[] pancakes, int k){
    int count = 0;
    while(pancakes.Contains(false) && ++count > 0){
        int blank = Array.IndexOf(pancakes, false);
        if(blank > pancakes.Length - k) return -1; //impossible
        for(int i = 0; i < k; i++) pancakes[blank + i] ^= true; //flips pancakes
    }
    return count;
}
