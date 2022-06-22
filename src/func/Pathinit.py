import os


class PathInit:
	def __init__(self):
		self.dir_projectRoot = "Falcon_FileShare"
		self._path_dir_current = os.getcwd()
		self.pathSlash = (('/' in self._path_dir_current) and '/' or "\\")

		self.path_dir_root_parent = self._path_dir_current[:self._path_dir_current.find(self.dir_projectRoot)]
		# self.path_dir_root = self.path_dir_root_parent + self.dir_projectRoot + self.pathSlash
		self.path_dir_root = self._path_dir_current + self.pathSlash
		self.path_dir_share = self.__path_generator(['files', 'share'])
		self.path_dir_upload = self.__path_generator(['files', 'upload'])
		self.path_file_log_stdout = self.__path_generator(['service', 'stdout.log'])

	def __path_generator(self, parm_dir_list):
		tmp_path = self.path_dir_root
		for index, item in enumerate(parm_dir_list):
			tmp_path += item
			if index < len(parm_dir_list) - 1:
				tmp_path += self.pathSlash
		return tmp_path


'''	def __path_check(self, parm_string):
		if not parm_string.endswith(self.pathSlash):
			parm_string += self.pathSlash
		return parm_string'''
