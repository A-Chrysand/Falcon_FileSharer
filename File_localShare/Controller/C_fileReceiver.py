import re
from django.http import HttpResponse
from File_localShare.Model.fileStorage import file_saver

from File_localShare.Model.PathInit import PathInit
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_upload(request):
	o_path = PathInit()
	if re.match(r"^/jsStream/upload/n/", request.path):
		file_dir = o_path.path_dir_upload
	elif re.match(r"^/jsStream/upload/s/", request.path):
		file_dir = o_path.path_dir_share
	else:
		return HttpResponse(
			status_code=404,
			content='上传失败，请求路径错误'
		)
	# 从表单的file字段获取文件，myfile为该表单的name值
	o_incoming_file = request.FILES.get('file')
	status = file_saver(o_incoming_file, file_dir)
	if status == 200:
		return HttpResponse('上传成功')
	elif status == 4031:
		print("ERROR>>>[4031]存在同名文件 | " + request.path + o_incoming_file.name)
		return HttpResponse(
			status=403,
			content="上传失败 存在同名文件"
		)
	elif status == 4032:
		print("ERROR>>>[4032]未接受到文件 | " + request.path)
		return HttpResponse(
			status=403,
			content="上传失败 未接受到文件"
		)
