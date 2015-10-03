import web

urls = (
	'/', 'Index',
	'/hello', 'Hello',
	'/hello_form', 'HelloForm',
	'/hello_form_layout', 'HelloFormLayout'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
	def GET(self):
		greeting = "Hello World"
		return render.index(greeting = greeting)
		
class Hello(object):
	def GET(self):
		form = web.input(name="Nobody")
		greeting = "Hello, %s" % form.name
		return render.index(greeting = greeting)

class HelloForm(object):
	def GET(self):
		return render.hello_form()
	
	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)
		
class HelloFormLayout(object):
	def GET(self):
		return render.hello_form_layout()
	
	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)
		
if __name__ == "__main__":
	app.run()
