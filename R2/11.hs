import Data.List
productOf2Biggest = product . take 2 . reverse . sort
