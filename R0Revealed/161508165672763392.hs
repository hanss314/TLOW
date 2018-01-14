import Data.Maybe
import Data.List 

atbash :: Char -> Char
atbash c = if c `elem` plain
           then cipher !! fromJust (elemIndex c plain)
           else c
   where
     plain  = ['a'..'z'] ++ ['A'..'Z']
     cipher = ['z','y'..'a'] ++ ['Z','Y'..'A']
