let tlow (arr : int list) = List.map (fun i -> List.map (fun j -> arr.[i] + arr.[if i - 1 < 0 then arr.Length - 1 else i - 1] * j) [0..arr.[i] - 1]) (List.rev [0..arr.Length - 1])
