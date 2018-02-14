r3 :: [Int] -> [[Int]]
r3 xs = reverse $ buildList (last xs) xs where
    buildList _ [] = []
    buildList p (x:xs) = take x [x, x+p..] : buildList x xs
