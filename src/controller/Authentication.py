import falcon
import jwt
import time
import json
import server_conf
from src.model.Userdb import Userdb
from src.resource.database_user import secret_key, user_status


class ApiResource:
	def __init__(self):
		self.o_userdb = Userdb()

	def on_post(self, req, resp):
		form = req.get_media()
		print(form)
		try:
			username = form["union_carrier"]["username"]
			password = form["union_carrier"]["password"]
			nibiru = form["union_carrier"]["nibiru"]
		except KeyError:
			resp.status = falcon.HTTP_403
			resp.text = ""
			return

		username = form["union_carrier"]["username"]
		password = form["union_carrier"]["password"]
		nibiru = form["union_carrier"]["nibiru"]
		status = self.o_userdb.user_login_check(
			parm_username=username,
			parm_password=password,
			parm_nibiru=nibiru
		)

		if status == user_status.ok:
			resp.status = falcon.HTTP_200
			encoded_token = jwt.encode({
				"username": username,
				"time": str(int(time.time())),
			}, secret_key, algorithm="HS256")
			resp.set_cookie("nibiru_token", encoded_token, max_age=600, domain="127.0.0.1")  # 600s
			resp.append_header(name="nibiru_token", value=encoded_token)
			resp.content_type = "application/json"
			resp.data = json.dumps({
				"info": "Login successful",
				"location": server_conf.nginx_static
				# "location": "/"
			}).encode()
		#
		# resp.location = "http://127.0.0.1" + vue_store.frew
		elif status == user_status.passwordIncorrect:
			resp.status = falcon.HTTP_401
			resp.content_type = "text/plain"
			resp.text = "Incorrect password"
		elif status == user_status.userNotFound:
			resp.status = falcon.HTTP_401
			resp.content_type = "text/plain"
			resp.text = "User not found"
		else:
			resp.status = falcon.HTTP_401
			resp.content_type = "text/plain"
			resp.text = "您看看你提交的什么**玩意"
