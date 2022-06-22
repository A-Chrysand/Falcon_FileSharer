import falcon


class FalconHtml:
	def __init__(self, parm_filename=""):
		self.filename = parm_filename

	def on_get(self, request, response):
		response.status = falcon.HTTP_200
		response.content_type = 'text/html'
		response.text = read_html_file(self.filename)


class FalconHtmlRedirection:
	def __init__(self, parm_location=""):
		self.location = parm_location

	def on_get(self, request, response):
		response.location = self.location
		response.status = falcon.HTTP_301


class FalconSink:
	def __init__(self, parm_sink_file=""):
		self.sink_file = parm_sink_file

	def sink(self, request, response):
		response.status = falcon.HTTP_200
		response.content_type = 'text/html'
		response.text = read_html_file(self.sink_file)


class FalconSinkRedirection:
	def __init__(self, parm_redirect_location="/"):
		self.rdl_lct = parm_redirect_location

	def sink_redirection(self, request, response):
		response.location = self.rdl_lct
		response.status = falcon.HTTP_301


def read_html_file(parm_filename, parm_encoding='utf-8'):
	with open("dist/" + parm_filename, 'r', encoding=parm_encoding) as f:
		temp_response = f.read()
		f.close()
		return temp_response
