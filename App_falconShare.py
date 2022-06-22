from wsgiref.simple_server import make_server
import falcon
import server_conf
import gunicorn_conf
# ##################################################Package
import os
# ##################################################Middleware
from src.middleware.AuthenticationCheck import AuthenticationCheck

# ##################################################Router
from src.controller.Authentication import ApiResource
from src.model.FileReceiver import FileReceiver
from src.view.JsGetFileTree import JsGetFileTree
from src.controller.GetClientIP import GetClientIP
from src.view.Html_render import FalconHtml, FalconHtmlRedirection, FalconSink, FalconSinkRedirection

# ##################################################App
app = falcon.App(
	middleware=[
		AuthenticationCheck()
	]
)

# 是否忽略结尾中结尾的'/'以匹配路由
falcon.RequestOptions.strip_url_path_trailing_slash = True

app.add_route(server_conf.nginx_static + 'jsPost/auth/login', ApiResource())
app.add_route(server_conf.nginx_static + 'jsGet/potato/clientip', GetClientIP())
app.add_route(server_conf.nginx_static + 'jsGet/share/filetree', JsGetFileTree())
app.add_static_route(server_conf.nginx_static + 'share/file/', os.getcwd() + "/files/share/", True)
app.add_route(server_conf.nginx_static + 'jsStream/upload/{parm_status}', FileReceiver())
if server_conf.enable_static_serve:
	app.add_static_route(server_conf.nginx_static, os.getcwd() + "/dist/", False)
	app.add_route(server_conf.nginx_static + 'login', FalconHtml(parm_filename='login.html'))
	app.add_route(server_conf.nginx_static + 'home', FalconHtml(parm_filename='index.html'))
	app.add_route('/ignister/darkinfant', FalconHtml(parm_filename='index.html'))

if __name__ == '__main__':
	host = "0.0.0.0"
	port = gunicorn_conf.bind.split(':')[1]
	print(port)
	with make_server(host, int(port), app) as httpd:
		print("Serving on {0}:{1} >>> http://127.0.0.1:{1}".format(host, port))
		httpd.serve_forever()
