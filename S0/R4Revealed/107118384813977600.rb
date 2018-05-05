def r4(pancakes, k, count = 0)
  for i in 0 ... pancakes.length - k + 1
    if !pancakes[i] 
      for j in i ... i + k
        pancakes[j] = !pancakes[j] end
      count += 1
    end 
  end
  pancakes.all? ? count : -1
end
