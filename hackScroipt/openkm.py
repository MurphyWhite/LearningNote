import shodan
def search_openkm(API_KEY):
	api = shodan.Shodan(API_KEY)
	results = api.search("openkm")
	print results['total']
	print results['matches']

def main():
	SHODAN_API_KEY = 'wKVILEwGhBalnpICFKwCzBblwLmYJe9R'
	search_openkm(SHODAN_API_KEY)

if __name__ == '__main__':
	main()