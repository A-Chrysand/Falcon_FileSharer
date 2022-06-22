import os
from copy import deepcopy
from pathlib import Path
import json
import server_conf
from src.func.Pathinit import PathInit
from src.func.cutstring import cutstring


class Share_FileTree:
	tree_json = []
	o_path = PathInit()
	path = o_path.path_dir_share

	def get_tree_json(self):
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
			str_filedir = cutstring(str(filename.parent), self.o_path.pathSlash, 4)
			str_filedir = str(str_filedir[4]).replace(self.o_path.pathSlash, "/")
			str_filedir += '/'
			str_filename = str(filename.name)
			tmp_dict["type"] = "file"
			tmp_dict["layer"] = str(layer)
			tmp_dict["filename"] = str_filename
			tmp_dict["url"] = server_conf.nginx_static + 'share/file/' + str_filename
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
