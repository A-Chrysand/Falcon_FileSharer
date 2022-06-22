from django.http import HttpResponse, HttpResponseRedirect
from File_localShare.Model.ShareFileTree import ShareFileTree


def file_tree(request):
	o_fileTree = ShareFileTree()
	json_fileTree_result = o_fileTree.print_tree()
	return HttpResponse(json_fileTree_result)


def default_redirect(request):
	if request.method == "GET":
		return HttpResponseRedirect('/')
	else:
		return HttpResponse('')


def clientIp(request):
	if 'HTTP_X_FORWARDED_FOR' in request.META:
		ip = request.META.get('HTTP_X_FORWARDED_FOR')
	else:
		ip = request.META.get('REMOTE_ADDR')
	return HttpResponse(ip)
