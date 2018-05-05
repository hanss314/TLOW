public static int[][] function(int[] input){
    int len = input.Length;
    int[][] output = new int[input.Length][];
    for (int i = 0; i < len; i++){
        output[len - i - 1] = new int[input[i]];
        for (int j = 0; j < output[len - 1 - i].Length; j++)
            output[len - i - 1][j] = input[i] + j * input[(len + i - 1) % len];
    }
    return output;
}
