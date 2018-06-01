import Data.List
lower = ['a'..'z']
upper = ['A'..'Z']
indexOf list k = (elemIndices list k) !! 0
enc :: (Char, Char) -> Char
enc (x,y)
    | x `elem` lower = cycle lower !! (indexOf x lower + indexOf y (lower ++ upper))
    | x `elem` upper = cycle upper !! (indexOf x upper + indexOf y (lower ++ upper))
    | otherwise      = x
vig string key = (map enc . zip string . cycle) key
