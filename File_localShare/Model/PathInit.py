import os


class PathInit:
	def __init__(self):
		self.dir_projectRoot = "Django_fileSharer"
		self.dir_share = "f_share"
		self.dir_upload = "f_upload"
		self.dir_service = "Service"
		self.dir_falcon_resource = "FalconResource"
		##########################################
		self.file_stdout = "stdout.log"
		# self.file_jvdb = "jvdb.db"

		##########################################
		self._path_dir_current = os.getcwd()
		self.pathSlash = (('/' in self._path_dir_current) and '/' or "\\")

		self.path_dir_root_parent = self._path_dir_current[:self._path_dir_current.find(self.dir_projectRoot)]
		self.path_dir_root = self.path_dir_root_parent + self.dir_projectRoot + self.pathSlash

		self.path_dir_share = self.path_dir_root + self.dir_share + self.pathSlash
		self.path_dir_upload = self.path_dir_root + self.dir_upload + self.pathSlash

		self.path_dir_log = self.path_dir_root + self.dir_service + self.pathSlash + "run" + self.pathSlash
		self.path_file_log_stdout = self.path_dir_log + self.file_stdout

	def __path_check(self, parm_string):
		if not parm_string.endswith(self.pathSlash):
			parm_string += self.pathSlash
		return parm_string
