import os


def file_saver(parm_file, parm_path):
	if parm_file:
		file_path = os.path.join(os.path.join(parm_path, parm_file.name))
		if os.path.isfile(file_path):
			return 4031  # 存在同名文件
		else:
			f = open(file_path, 'wb')
			for i in parm_file.chunks():
				f.write(i)
			f.close()
			return 200  # OK
	else:
		return 4032  # 未接受到文件
