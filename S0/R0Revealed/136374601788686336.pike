string atbash(string input) {                                           /* run with pike 8.0. you probably will want to create a main function as well, think c syntax            */
    array key = enumerate(65) + enumerate(26,-1,90) + enumerate(6,1,91) /* pike is so obscure that discord doesn't know how to highlight it LOL                                   */
              + enumerate(26,-1,122) + enumerate(133,1,123);            /* enumerate produces an array range (similar to python 2's range); -1's to reverse.                      */
    return ((string)key[input[0]..input[0]]);                           /* this construction required to take a substring - can't do a straight index since that autocasts to int */
}                                                                       /* and sadly I couldn't find a good way other than inbuilt functions to cast int to strings by char value */

