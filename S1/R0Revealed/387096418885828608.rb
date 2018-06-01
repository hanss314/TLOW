def s1r0 str, key
	key = key.downcase.chars.map {|x| [*"a".."z"].index x} * str.length
	str.chars.map.with_index do |e, i|
		if e =~ /[a-z]/i
			e = e.ord
			((key[i] + (e % 32 - 1)) % 26 + (e[5] * 32) + 65).chr
		else e
		end
	end .join ''
end