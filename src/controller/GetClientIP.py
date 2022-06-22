import falcon
import time

from src.func.Pathinit import PathInit


class GetClientIP:

	def on_get(self, request, response, ):
		tmp_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		tmp_request_ip = self.get_clientIp(request, None)
		with open(PathInit().path_file_log_stdout, 'a', ) as f:
			f.writelines(tmp_time + " - " + str(tmp_request_ip) + "\n")
			f.close()
		response.status = falcon.HTTP_200
		response.content_type = 'text/plain'
		response.text = self.ip_masker(tmp_request_ip, parm_list_mask=[0, '*', 0, '*'])

	def get_clientIp(self, request, parm_list_mask):
		tmp_request_route = request.access_route
		if len(tmp_request_route) == 1 or (len(tmp_request_route) == 2 and tmp_request_route[0] != '127.0.0.1'):
			request_ip = tmp_request_route[0]
		elif len(tmp_request_route) > 2:
			request_ip = tmp_request_route
		else:
			request_ip = ""
		if parm_list_mask and len(parm_list_mask) == 4:
			request_ip = self.ip_masker(request_ip, parm_list_mask)
		return request_ip

	def ip_masker(self, parm_ip, parm_list_mask):
		"""
		parm_list_mask=[], 0=visiable, !0=masked
		"""
		list_request_ip = parm_ip.split('.')
		tmp_result_ip = ""
		for i in range(0, 4):
			if parm_list_mask[i] != 0:
				tmp_result_ip += str(parm_list_mask[i])
			else:
				tmp_result_ip += list_request_ip[i]
			if i < 3:
				tmp_result_ip += "."
		return tmp_result_ip
