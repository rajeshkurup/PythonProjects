import web
import markdown
from rajesh_family_trust.family_member import *

urls = (
	'/', 'Index',
	'/family_members', 'FamilyMembers',
	'/family_member', 'FamilyMember'
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'page': None})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/')

md = markdown.Markdown(output_format='html4')

class Index(object):
	def GET(self):
		html_content = '<h1>Rajesh Family Trust</h1>'
		html_content += '<br><p>The trust of Rajesh family members to handle all family matters</p>'
		html_content += '<br><p><a href="/family_members">Family Members</a></p>'
		content = md.convert(html_content)
		return render.layout(content=content)
		
class FamilyMembers(object):
	def GET(self):
		html_content = '<h1>Family Members</h1>'
		html_content += '<br><p>List of family members of Rajesh Family Trust</p>'
		html_content += '<br><p><form action="/family_member" method="POST">'
		limit = len(family_members) + 1

		for position in range(1, limit):
			str_position = str(position)
			html_content += '<input type="radio" name="member_name" value="'
			html_content += str_position
			
			if position == 1:
				html_content += '" checked="true"/> '
			else:
				html_content += '"/> '

			html_content += family_members[str_position].name
			html_content += '<br>'
			position += 1

		html_content += '<input type="submit" name="view_details" value="View Details"/>'
		html_content += '</form></p>'
		content = md.convert(html_content)
		return render.layout(content=content)
		
class FamilyMember(object):
	def POST(self):
		form = web.input(member_name=[])
		family_member = family_members[form.member_name[0]]
		html_content = '<h1>Family Member</h1>'
		html_content += '<br><p>Details of Family Member</p>'
		html_content += '<br><p>Name: '
		html_content += family_member.name
		html_content += '</p><br><p>Age: '
		html_content += family_member.age
		html_content += '</p><br><p>Gender: '
		html_content += family_member.gender
		html_content += '</p><br><p>Job: '
		html_content += family_member.job
		html_content += '</p><br><p>Office: '
		html_content += family_member.office
		html_content += '</p>'
		content = md.convert(html_content)
		return render.layout(content=content)

if __name__ == "__main__":
	app.run()
