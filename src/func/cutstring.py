def cutstring(operation_string, splicechar=";", para_num_of_splicechar=0):
	try:
		operation_string.index(splicechar)  # 检测operation_string里是否含有切割标记字符
	except ValueError:
		print("切割的字符串不含切割标记字符")
		return
	temp = []
	if para_num_of_splicechar:
		num_of_splicechar = para_num_of_splicechar
	else:
		num_of_splicechar = operation_string.count(splicechar)
	# 如果num_of_splicechar设置错误，那么会导致最后一个splicechar之后为一整块(分割不完全)
	for i in range(num_of_splicechar + 1):
		if i != num_of_splicechar:
			temp.append(operation_string[:operation_string.index(splicechar)]
			            )  # 切割从开头到分割标记字符之前的字符串并push到列表中
			operation_string = operation_string.lstrip(
				temp[i])  # 从左向右删除刚刚切割掉的字符
			operation_string = operation_string.lstrip(
				splicechar)  # 从左向右删除标记字符
		else:
			temp.append(operation_string)
			break
	return temp
