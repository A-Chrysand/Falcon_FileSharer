from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from File_localShare.Model.readImage import read_image


def index(request):
	return render(request, 'index.html')


def favicon(request):
	tmp_path = settings.TEMPLATES[0]["DIRS"][0]
	result = read_image(parm_img_dir=tmp_path, parm_img_file_name="favicon.ico")
	return HttpResponse(result, content_type='image/ico')
