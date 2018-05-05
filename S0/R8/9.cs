public static int tlow8(int input){
        
    if (input < 0)
        return input * (input % 7 + 2);
    else
        return (int)Math.Round(Math.Sqrt(input), 0);

}
