import falcon
from src.model.Share_FileTree import Share_FileTree


class JsGetFileTree:
	def on_get(self, request, response):
		response.status = falcon.HTTP_200
		response.content_type = 'application/json'
		o_filetree = Share_FileTree()
		json_result = o_filetree.get_tree_json()
		response.text = json_result

	def on_post(self, request, response, post_data):
		response.status = falcon.HTTP_403
		response.content_type = "text/plain"
		response.text = ""
