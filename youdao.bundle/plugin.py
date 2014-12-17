import urllib,urllib2,json

def results(parsed, original_query):
	search_url = "http://fanyi.youdao.com/openapi.do?keyfrom=ydSpotlight&key=224746121&type=data&doctype=json&version=1.1&q="
	web_url = "http://dict.youdao.com/search?q="
	search_specs = [
		 ["YoudaoQuery", "~youdaotext", "https://www.google.com/search?q=", search_url]
	]
	for name, key, url, yd_url in search_specs:
		if key in parsed:
			web_url = web_url + parsed[key]
			
			youdao_url = yd_url + parsed[key]
			response = urllib2.urlopen(youdao_url).read()
			search_result = json.loads(response)
			basicMeaning = search_result['basic']
			explains = basicMeaning['explains']

			result_text = ""
			for explain in explains:
				result_text = result_text + explain + "<br>"

			return {
				"title": "Youdao : '{0}'".format(parsed[key]),
				"run_args": [web_url],
				"html": """
				<h4 style='font-weight: normal; font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial; line-height: 1.2'>
			    {0}
			    </h4>
				""".format(result_text.encode('utf-8')),
			}

def run(url):
	import os
	os.system('open "{0}"'.format(url))
