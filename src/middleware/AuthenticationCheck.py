import re
import time

import falcon
import jwt

from src.model.Userdb import Userdb
from src.resource.database_user import secret_key, user_status
import server_conf


class AuthenticationCheck:
	def __init__(self):
		self.o_userdb = Userdb()
		self.check_status = 0

	def process_request(self, req, resp):
		if server_conf.enable_static_serve and re.search(r'(.html|.css|.js|.map|.woff|.ttf|.ico)$', req.url):
			self.check_status = user_status.ok
		elif not re.match(r'\S{0,30}' + server_conf.nginx_static + 'jsPost/auth/login', req.url):
			# print("Not login page, middleware working")
			cookie_nibiru_token = req.get_cookie_values("nibiru_token")
			if cookie_nibiru_token:
				# print("checking nibiru_token")
				decoded_token = jwt.decode(cookie_nibiru_token[0], secret_key, algorithms="HS256")
				last_time = int(decoded_token["time"])
				this_time = int(time.time())
				if this_time - last_time >= 1800:
					self.check_status = user_status.timeExpired
				else:
					username = decoded_token["username"]
					status = self.o_userdb.search_username(username)
					if status == user_status.ok:
						self.check_status = user_status.ok
					else:
						self.check_status = user_status.userNotFound

			else:
				# print("unfounded nibiru_token")
				self.check_status = user_status.tokenNotFound
		else:
			# print("Login page, middleware pass")
			self.check_status = user_status.ok

	def process_resource(self, req, resp, resource, params):
		pass

	def process_response(self, req, resp, resource, req_succeeded):
		if self.check_status == 0:
			# print("status==0")
			resp.status = falcon.HTTP_500
		elif self.check_status == user_status.userNotFound:
			resp.status = falcon.HTTP_401
			# print("userNotFound")
			resp.location = server_conf.nginx_static + "login"
		elif self.check_status == user_status.tokenNotFound:
			resp.status = falcon.HTTP_401
			# print("tokenNotFound")
			resp.location = server_conf.nginx_static + "login"
