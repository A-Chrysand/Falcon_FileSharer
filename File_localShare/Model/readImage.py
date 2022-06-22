import os


def read_image(parm_img_dir="/dist/img/", parm_img_file_name="null"):
	tmp_file = os.path.join(parm_img_dir, parm_img_file_name)
	# print(tmp_file)
	if (os.path.isfile(tmp_file)):
		# print('ok')
		file = open(tmp_file, 'rb')
		result = file.read()
	else:
		result = "".encode('utf-8')
	return result
