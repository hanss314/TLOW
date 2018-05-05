char f(char c){
  return  c >= 'A' && c <= 'Z' ? 155 - c : // If between A and Z rotate around 155 == 'A' + 'Z' 
          c >= 'a' && c <= 'z' ? 219 - c : // If between a and z rotate around 219 == 'a' + 'z'
                                 c;        // Else just return c
}
