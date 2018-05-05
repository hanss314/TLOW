public static char atbash(char input){
    string abc = "aAbBcCdDeEfFgGhHiIjJkKlLmMNnOoPpQqRrSsTtUuVvWwXxYyZz";
    int i = 0;
    foreach(char j in abc){
        i++;
        if(input == j) 
            return abc[52-i];
    }
    return input;
}
