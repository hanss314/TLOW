function contains(tbl, object) for i = 1, #tbl, 1 do if tbl[i] == object then return true; end end return false; end
function slice(avocado_count) if contains({0, 1}, avocado_count) then return false; end 
	for i = avocado_count - 1, 2, -1 do if avocado_count % i == 0 then return i; end end return false; end
function mash(avocado_count) return (avocado_count ^ 2) % 256; end
function eat(avocado_count, spoon) return (avocado_count - spoon) >= 0 and (avocado_count - spoon) or false; end
function trap_bot(avocados, spoon) if #avocados == 0 then return math.random(1, 32); elseif spoon <= 0 then return math.random(1, 32); end
	last = avocados[#avocados]; if not contains(avocados, slice(last)) and slice(last) then return 0;
	elseif not contains(avocados, mash(last)) then return 1; 
	elseif (not contains(avocados, eat(last, spoon))) and eat(last, spoon) >= 0 then return 2; 
	else return 3; end end

