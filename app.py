from flask import Flask
from flask import render_template
from flask import request
from form import DomainForm
from bs4 import BeautifulSoup as bs
from urllib import request as rq

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	form = DomainForm(request.form)
	parser = Parser()
	url = None
	if request.method == 'POST' and form.validate():
		parser.connect(form.domain.data)
		url = parser.pars()
	return render_template('index.html', form=form, result=url)


class Parser:
	def connect(self, url):
		self.url = url
		self.rq = rq.urlopen(self.url)

	def pars(self):
		self.p = bs(self.rq, "html.parser")
		self.r = []
		for k in self.p.find_all('a'):
			self.r.append(k.get('href'))
		return self.r


if __name__ == '__main__':
	app.run(debug=True)