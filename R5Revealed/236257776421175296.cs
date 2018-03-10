using System.Linq;
public static int r5(int[] avocadoes, int spoon){
    int least = 1280; int move = 0; int a; try {a = avocadoes[avocadoes.Length - 1];} catch {return 4;}
    if (spoon <= 0) return a == 4 ? 1 : 260 - a;
    foreach(int n in next(a,spoon)){
    int score = n + 256 * next(n, spoon).Count(x => !avocadoes.Contains(x) & x > -1);
    if(!avocadoes.Contains(n) && n > -1 && score < least){
        move = Array.IndexOf(next(a,spoon), n); least = score;}} return move; }
public static int[] next(int x, int spoon, int o = -1){ for (int i = x - 1; i > 1; i--) if ((double)x / i == x / i) o = x / i;
    return new int[]{ o % 256, (x * x) % 256, (x - spoon) % 256, (x + spoon) % 256}; }
