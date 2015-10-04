import web

web.config.debug = False

urls = (
	"/count", "Count",
	"/reset", "Reset"
)

app = web.application(urls, locals())

store = web.session.DiskStore('sessions')

session = web.session.Session(app, store, initializer={'count': 0})

class Count(object):
	def GET(self):
		session.count += 1
		return str(session.count)
		
class Reset(object):
	def GET(self):
		session.kill()
		return ""
		
if __name__ == "__main__":
	app.run()
