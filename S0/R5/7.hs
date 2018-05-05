avocado :: [Int] -> Int -> Int
avocado [] _ = 60 -- Mostly arbitrary
avocado a n
    | n < 0 = 59 -- Completely arbitrary
    | not $ elem (((last a) ^ 2) `mod` 256) a = 1 -- slice if square is not in list
    | not $ elem (((last a) - n) `mod` 256) a = 2 -- eat if result is not in list
    | not $ elem (((last a) + n) `mod` 256) a = 3 -- buy if result not in list
    | otherwise = 0 -- if everything else loses, just pray slice is valid
