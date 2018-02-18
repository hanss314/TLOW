(defn tlow3 [arr] (do
  (reverse (for [[index item] (map-indexed vector arr)]
    [(for [i (range item)]
      (+ item (* i (nth arr
        (mod (+ (dec index) (count arr)) (count arr))
      )))
    )]
  ))
))
