function beep(boop)
  table.sort(boop)
  return tonumber(boop[#boop]) * tonumber(boop[#boop-1])
end
