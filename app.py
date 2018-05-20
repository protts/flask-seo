import os, random
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from form import DomainForm
from bs4 import BeautifulSoup as bs
from urllib import request as rq


app = Flask(__name__, static_folder='static')

@app.route('/', methods=['POST', 'GET'])
def index():
	form = DomainForm(request.form)
	parser = Parser()
	file = File()
	url = None
	save = None
	if request.method == 'POST' and form.validate():
		parser.connect(form.domain.data)
		url = parser.pars_url()
		save = file.save(url)
	return render_template('index.html', form=form, result=url)

@app.route('/download/', methods=['GET'])
def download():
	return send_from_directory(directory='static', filename='links.txt', as_attachment=True)

class Parser:
	def connect(self, url):
		self.url = url
		self.rq = rq.urlopen(self.url)

	def pars_url(self):
		self.p = bs(self.rq, "html.parser")
		self.r = []
		for k in self.p.find_all('a'):
			self.r.append(k.get('href'))
		return self.r

class File:
	def save(self, url):
		self.file = str(random.random())+".txt"
		self.f = open('./static/%s' %file, 'w')
		for k in url:
			self.f.write(k+'\n')
		self.f.close()



if __name__ == '__main__':
	app.run(debug=True)