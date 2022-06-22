import time

secret_key = 's_Magikey' + str(time.localtime(time.time()).tm_mon) + 'Dragon' + str(
	time.localtime(time.time()).tm_mday)


class user_status:
	ok = 200,
	timeExpired = 4000,
	tokenNotFound = 4001
	badRequestData = 4002

	userNotFound = 4011,
	passwordIncorrect = 4012


database_user = [
	{
		"username": "admin",
		"password": "shootingcodetalker",
	}, {
		"username": "test",
		"password": "test1234"
	}, {
		"username": "accesscodetalker",
		"password": "link42300",
	}, {
		"username": "a",
		"password": "a",
	}
]
