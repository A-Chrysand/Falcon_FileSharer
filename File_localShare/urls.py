"""File_localShare URL Configuration
    # path('admin/', admin.site.urls),

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve

from File_localShare.Views import views
from File_localShare.Controller import controller, C_fileReceiver

# ###################################### START
urlpatterns = [
	re_path(r'static/(?P<path>.*)$', serve, {'document_root': '/dist'}),
	re_path(r'share/(?P<path>.*)$', serve,
	        {'document_root': settings.MEDIA_ROOT}),
]
# ###################################### STATIC END
urlpatterns += [
	path('', views.index),
	path('favicon.ico', views.favicon),
	re_path(r'^download', controller.default_redirect),
	re_path(r'^upload', controller.default_redirect),
	# path(r'', TemplateView.as_view(template_name="index.html")),
]
# ###################################### FILE END
urlpatterns += [
	re_path(r'jsStream/upload/\w/', C_fileReceiver.api_upload),
	path('jsGet/share/filetree', controller.file_tree),
	path('jsGet/potato/clientip', controller.clientIp)
]
# ###################################### AXIOS END
