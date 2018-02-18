def difference_maker(list):
	new_list = []

	for pos, item in enumerate(list[::-1]):		
		prev = list[-(pos - 1)]
		new_list.append(sorted(range(item, item + item * prev, prev)))
			# Thanks Python for somehow TypeErroring when using list() instead

	return new_list