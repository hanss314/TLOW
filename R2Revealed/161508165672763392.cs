using System.Linq;

public static int tlow2(int[] array) {
    array = array.OrderByDescending(x => x).ToArray();
        
    return array[0] * array[1];
}
