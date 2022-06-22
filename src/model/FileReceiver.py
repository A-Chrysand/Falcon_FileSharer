import cgi
import os
import falcon
from src.func.Pathinit import PathInit


class FileReceiver:
	def __init__(self):
		self.o_path = PathInit()

	def on_post(self, req, resp, parm_status):
		if parm_status == 'n':
			file_dir = self.o_path.path_dir_upload
		elif parm_status == 's':
			file_dir = self.o_path.path_dir_share
		else:
			resp.status = falcon.HTTP_403
			resp.content_type = 'text/plain'
			resp.text = '上传失败，请求路径错误'
			return

		# 从表单的file字段获取文件，myfile为该表单的name值
		form = req.get_media()
		post_file = {}
		for part in form:
			post_file["content_type"] = part.content_type
			post_file["data"] = part.stream.read()
			post_file["filename"] = part.filename

		status = self.file_saver(post_file, file_dir)

		if status == 200:
			resp.status = falcon.HTTP_200
			resp.content_type = 'text/plain'
			resp.text = '上传成功'
		elif status == 4031:
			print("ERROR>>>[4031]存在同名文件 | " + req.path + post_file["filename"])
			resp.status = falcon.HTTP_403
			resp.content_type = 'text/plain'
			resp.text = '上传失败，存在同名文件'
		elif status == 4032:
			print("ERROR>>>[4032]未接受到文件 | " + req.path)
			resp.status = falcon.HTTP_403
			resp.content_type = 'text/plain'
			resp.text = '上传失败，未接收到文件'

	@staticmethod
	def file_saver(parm_file, parm_path):
		if parm_file:
			file_path = os.path.join(os.path.join(parm_path, parm_file["filename"]))
			if os.path.isfile(file_path):
				return 4031  # 存在同名文件
			else:
				f = open(file_path, 'wb')
				# for i in parm_file.data:
				f.write(parm_file["data"])
				f.close()
				return 200  # OK
		else:
			return 4032  # 未接受到文件
