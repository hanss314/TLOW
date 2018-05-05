using System.Linq; //for list.Max() and list.Min()
int f(int[] input){
        if (input.Length < 2)
            throw new ArgumentException();
        int[] list = new int[input.Length];
        input.CopyTo(list, 0); //doesn't break input list
        int output = list.Max(); //stores max value
        list[Array.IndexOf(list, output)] = Int32.MinValue; //removes max value
        return output * list.Max();
    }
