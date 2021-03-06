import web
from gothonweb import map

urls = (
	'/', 'Index',
	'/hello', 'Hello',
	'/hello_form', 'HelloForm',
	'/hello_form_layout', 'HelloFormLayout',
	'/game', 'GameEngine'
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'room': None})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/', base="layout")

class Index(object):
	def GET(self):
		#greeting = "Hello World"
		#return render.index(greeting = greeting)
		# this is used to setup a session with starting values
		session.room = map.START
		web.seeother("/game")
		
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
		
class GameEngine(object):
	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			# why is there here? do you need it?
			return render.you_died()
			
	def POST(self):
		form = web.input(action=None)
		
		# there is a bug here, can you fix it?
		if session.room and form.action:
			session.room = session.room.go(form.action)

		web.seeother("/game")
			
if __name__ == "__main__":
	app.run()
