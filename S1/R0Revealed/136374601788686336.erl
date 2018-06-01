charadd(A, $A) -> A; charadd(A, $a) -> A; charadd($z, B) -> charadd($a, B-1); 
charadd($Z, B) -> charadd($A, B-1); charadd(A, B) -> charadd(A+1, B-1).
front(Str) -> lists:nth(1, Str). rest(Str) -> string:sub_string(Str, 2). 
cycle(Str) -> rest(Str) ++ [front(Str)].

s1r0("", Key) -> ""; s1r0(Str, Key) -> 
  case string:to_lower([front(Str)]) /= string:to_upper([front(Str)]) of
    true  -> [charadd(front(Str), front(Key))] ++ s1r0(rest(Str), cycle(Key));
    false -> [front(Str)]                      ++ s1r0(rest(Str), cycle(Key))
  end.
