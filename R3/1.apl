  f←{⌽{⍺+⍵×¯1+⍳⍺}⌿0 ¯1⌽(2,⍴⍵)⍴⍵}
⍝   {                          }  defines a function that
⍝                      (2,⍴⍵)⍴⍵   takes the input array and reshapes it to size 2 by the length of the input
⍝                 0 ¯1⌽           (making two identical rows) and rotates the bottom row back by 1
⍝     {       ⍳⍺}⌿                applies to each column the operation that takes a list of ⍺ integers
⍝      ⍺+⍵×¯1+                    and makes it the sub-array specified in the challenge)
⍝    ⌽                            then reverses the whole array
⍝ f←                              and assigns the whole function to f
