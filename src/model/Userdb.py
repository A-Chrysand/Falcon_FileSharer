from src.resource.database_user import database_user, user_status


class Userdb:
	@staticmethod
	def user_login_check(parm_username, parm_password, parm_nibiru):
		'''
		200     login success
		4011    incorrect password
		404     user not found
		'''
		for item in database_user:
			if item["username"] == parm_username:
				if item["password"] == parm_password:
					return user_status.ok
				else:
					return user_status.passwordIncorrect
			else:
				pass
		return 404

	@staticmethod
	def search_username(parm_username):
		for item in database_user:
			if item["username"] == parm_username:
				return user_status.ok
		return user_status.userNotFound
