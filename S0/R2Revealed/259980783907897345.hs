import Data.List
tlow :: [Int] -> Int
tlow = product . take 2 . reverse . sort
