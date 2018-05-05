import Data.List(elemIndex)

atbash :: Char -> Char
atbash c
    | Just x  <- index = outSet !! x
    | Nothing <- index = c
        where
            index  = elemIndex c inSet
            inSet  = ['a'..'z']     ++ ['A'..'Z']
            outSet = ['z','y'..'a'] ++ ['Z','Y'..'A'] 
