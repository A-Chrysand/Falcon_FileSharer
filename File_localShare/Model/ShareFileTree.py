import os
from copy import deepcopy
from pathlib import Path
import json
from File_localShare.Model.PathInit import PathInit


class ShareFileTree:
	tree_json = []
	o_path = PathInit()
	path = o_path.path_dir_share

	def print_tree(self):
		self.generate_tree(Path(self.path), 0)
		result = deepcopy(self.tree_json)
		self.tree_json.clear()  # reignite
		return json.dumps(result)

	def generate_tree(self, pathname, n=0):
		if pathname.is_file():
			self.tree_json.append(
				self.jsonTree_generator(p_type='file', filename=pathname, layer=n, filesize=self.get_FileSize(pathname))
			)
		elif pathname.is_dir():
			self.tree_json.append(
				self.jsonTree_generator(p_type='dir', filename=str(pathname.relative_to(pathname.parent)), layer=n)
			)
			for cp in pathname.iterdir():
				self.generate_tree(cp, n + 1)

	def jsonTree_generator(self, p_type, filename, layer, filesize=""):
		tmp_dict = {}
		if p_type == 'file':
			str_filedir = self.cutstring(str(filename.parent), '\\', 4)
			str_filedir = str(str_filedir[4]).replace("\\", "/")
			str_filedir += '/'
			str_filename = str(filename.name)
			tmp_dict["type"] = "file"
			tmp_dict["layer"] = str(layer)
			tmp_dict["filename"] = str_filename
			# tmp_dict["url"] = '/share/' + str_filedir + str_filename
			tmp_dict["url"] = '/share/' + str_filename
			tmp_dict["size"] = filesize
			return tmp_dict
		elif p_type == 'dir':
			tmp_dict["type"] = "dir"
			tmp_dict["filename"] = filename
			tmp_dict["layer"] = str(layer)
			return tmp_dict

	@staticmethod
	def get_FileSize(parm_file_path):
		file_size = os.path.getsize(parm_file_path)
		if file_size > 1024 * 1024:
			file_size = file_size / (1024 * 1024)
			return str(round(file_size, 1)) + "MB"
		else:
			file_size = file_size / 1024
			return str(round(file_size, 1)) + "KB"

	@staticmethod
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
