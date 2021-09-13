from flask import Flask,Response,request,jsonify
import requests
import re
app=Flask(__name__)
def headers(response):
	response=jsonify({"content":content})
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response
def get_mp4link(episodeid):
	url="https://streamani.net/streaming.php?id="+episodeid
	ssn=requests.Session()
	data=ssn.get(url).text
	link=data.split(' data-provider="serverwithtoken" data-video="')[1].split('">Multiquality Server</li>')[0]
	data2=ssn.get(link).text
	mp4s=re.findall("https://.*?mp4",data2)
	print(mp4s)
	



@app.route('/<path:path>')
def catch_all(path):
	if request.args.get('episodeid') is None:
		return "This is the homepage please add episodeid paramater"
	else:
		episodeid=request.args.get('episodeid')
		get_mp4link(episodeid)

app.run(debug=True) 