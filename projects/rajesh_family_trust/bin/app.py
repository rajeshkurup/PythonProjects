import web
import markdown
from rajesh_family_trust.family_member import *

urls = (
	'/', 'Index',
	'/family_members', 'FamilyMembers',
	'/family_member', 'FamilyMember',
	'/family_member_edit', 'FamilyMemberEdit',
	'/family_member_submit', 'FamilyMemberSubmit',
	'/family_member_add', 'FamilyMemberAdd',
	'/family_member_create', 'FamilyMemberCreate'
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'selected_family_member': None})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/')

md = markdown.Markdown(output_format='html4')

fmo = FamilyMemberOperations()

class Index(object):
	def GET(self):
		first_family_member = fmo.get_first_member()
		if first_family_member:
			session.selected_family_member = first_family_member.get("id")
		else:
			session.selected_family_member = 0
				
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
	
		if session.selected_family_member > 0:
			family_members = fmo.get_all_members()
			for family_member in family_members:
				html_content += '<br><input type="radio" name="member_name" value="%d"' % family_member.get("id")
			
				if session.selected_family_member == family_member.get("id"):
					html_content += ' checked /> %s' % family_member.get("name")
				else:
					html_content += ' /> %s' % family_member.get("name")

			html_content += '<br><br><input type="submit" name="btn_input" value="Home" />'
			html_content += '<input type="submit" name="btn_input" value="View" />'
			html_content += '<input type="submit" name="btn_input" value="Edit" />'
			html_content += '<input type="submit" name="btn_input" value="Delete" />'
		
		html_content += '<input type="submit" name="btn_input" value="Add" /></form></p>'
		content = md.convert(html_content)
		return render.layout(content=content)
		
class FamilyMember(object):
	def GET(self):
		html_content = '<h1>Family Member</h1>'
		html_content += '<br><p>Details of Family Member</p>'
		family_member = fmo.get_member(id=session.selected_family_member)
		
		if family_member:
			html_content += '<br><p><form action="/family_member_edit" method="POST">'
			html_content += '<br><p>Name: %s </p>' % family_member.get("name")
			html_content += '<br><p>Age: %s </p>' % family_member.get("age")
			html_content += '<br><p>Gender: %s </p>' % family_member.get("gender")
			html_content += '<br><p>Job: %s </p>' % family_member.get("job")
			html_content += '<br><p>Office: %s </p>' % family_member.get("office")
	
			father_name = "Not Selected"
			father_id = family_member.get("father")
			if father_id != 0:
				father_name = fmo.get_member(id=father_id).get("name")
	
			html_content += '<br><p>Father: %s </p>' % father_name
			
			mother_name = "Not Selected"
			mother_id = family_member.get("mother")
			if mother_id != 0:
				mother_name = fmo.get_member(id=mother_id).get("name")
			
			html_content += '<br><p>Mother: %s </p>' % mother_name
			
			html_content += '<br><input type="submit" name="btn_input" value="Edit" />'
			html_content += '<input type="submit" name="btn_input" value="Family Members" />'
			html_content += '<input type="submit" name="btn_input" value="Home" /></form></p>'
			
		content = md.convert(html_content)
		return render.layout(content=content)

	def POST(self):
		form = web.input(btn_input=None, member_name=None)
		
		if form.member_name:
			session.selected_family_member = int(form.member_name)

		if form.btn_input == "View":
			web.seeother("/family_member")

		elif form.btn_input == "Edit":
			web.seeother("/family_member_edit")

		elif form.btn_input == "Add":
			web.seeother("/family_member_add")

		elif form.btn_input == "Delete":
			family_member = fmo.delete_member(id=session.selected_family_member)

			if family_member:
				session.selected_family_member = family_member.get("id")
			else:
				session.selected_family_member = 0
	
			web.seeother("/family_members")

		elif form.btn_input == "Home":
			web.seeother("/")
			
		else:
			web.seeother("/")
		
class FamilyMemberEdit(object):
	def GET(self):
		html_content = '<h1>Edit Family Member</h1>'
		html_content += '<br><p>Edit the Details of Family Member</p>'
		family_member = fmo.get_member(id=session.selected_family_member)
		
		if family_member:
			html_content += '<br><p><form action="/family_member_submit" method="POST">'
			html_content += '<br><p>Name: <input type="text" name="name" value="%s" /></p>' % family_member.get("name")
			html_content += '<br><p>Age: <input type="text" name="age" value="%s" /></p>' % family_member.get("age")
			html_content += '<br><p>Gender: <input type="text" name="gender" value="%s" /></p>' % family_member.get("gender")
			html_content += '<br><p>Job: <input type="text" name="job" value="%s" /></p>' % family_member.get("job")
			html_content += '<br><p>Office: <input type="text" name="office" value="%s" /></p>' % family_member.get("office")
			
			html_content += '<br><p>Father: <select name="father">'
			html_content += '<option value="0">Select</option>'
			male_members = fmo.get_members(query={"gender": "Male", "id": {"$ne": session.selected_family_member}})
		
			for father in male_members:
				html_content += '<option value="%d">%s</option>' % (father.get("id"), father.get("name"))
			
			html_content += '</select><br><p>Mother: <select name="mother">'
			html_content += '<option value="0">Select</option>'
			female_members = fmo.get_members(query={"gender": "Female", "id": {"$ne": session.selected_family_member}})
		
			for mother in female_members:
				html_content += '<option value="%d">%s</option>' % (mother.get("id"), mother.get("name"))
			
			html_content += '</select><br><input type="submit" name="btn_input" value="Submit" />'
			html_content += '<input type="submit" name="btn_input" value="Reset" />'
			html_content += '<input type="submit" name="btn_input" value="Cancel" /></form></p>'
		
		content = md.convert(html_content)
		return render.layout(content=content)
	
	def POST(self):
		form = web.input(btn_input=None)
		if form.btn_input == "Edit":
			web.seeother("/family_member_edit")
			
		elif form.btn_input == "Family Members":
			web.seeother("/family_members")
			
		elif form.btn_input == "Home":
			web.seeother("/")
			
		else:
			web.seeother("/")
		
class FamilyMemberSubmit(object):
	def POST(self):
		form = web.input(btn_input=None, name=None, age=None, gender=None, job=None, office=None)
		if form.btn_input == "Submit":
			family_member = {"id": session.selected_family_member,
								"name": form.name,
								"age": form.age,
								"gender": form.gender,
								"job": form.job,
								"office": form.office,
								"father": int(form.father),
								"mother": int(form.mother)}
			fmo.update_member(family_member=family_member)
			web.seeother("/family_member")
			
		elif form.btn_input == "Reset":
			web.seeother("/family_member_edit")
		
		elif form.btn_input == "Cancel":
			web.seeother("/family_member")
		
		else:
			web.seeother("/")

class FamilyMemberAdd(object):
	def GET(self):
		html_content = '<h1>Add Family Member</h1>'
		html_content += '<br><p>Add new Family Member</p>'
		html_content += '<br><p><form action="/family_member_create" method="POST">'
		html_content += '<br><p>Name: <input type="text" name="name" value="" /></p>'
		html_content += '<br><p>Age: <input type="text" name="age" value="" /></p>'
		html_content += '<br><p>Gender: <input type="text" name="gender" value="" /></p>'
		html_content += '<br><p>Job: <input type="text" name="job" value="" /></p>'
		html_content += '<br><p>Office: <input type="text" name="office" value="" /></p>'
		
		html_content += '<br><p>Father: <select name="father">'
		html_content += '<option value="0">Select</option>'
		male_members = fmo.get_members(query={"gender": "Male"})
		
		for father in male_members:
			html_content += '<option value="%d">%s</option>' % (father.get("id"), father.get("name"))
			
		html_content += '</select><br><p>Mother: <select name="mother">'
		html_content += '<option value="0">Select</option>'
		female_members = fmo.get_members(query={"gender": "Female"})
		
		for mother in female_members:
			html_content += '<option value="%d">%s</option>' % (mother.get("id"), mother.get("name"))
		
		html_content += '</select><br><input type="submit" name="btn_input" value="Add" />'
		html_content += '<input type="submit" name="btn_input" value="Reset" />'
		html_content += '<input type="submit" name="btn_input" value="Cancel" /></form></p>'
		content = md.convert(html_content)
		return render.layout(content=content)

class FamilyMemberCreate(object):
	def POST(self):
		form = web.input(btn_input=None, name=None, age=None, gender=None, job=None, office=None, father=None, mother=None)
		if form.btn_input == "Add":
			family_member = {"id": 0,
								"name": form.name,
								"age": form.age,
								"gender": form.gender,
								"job": form.job,
								"office": form.office,
								"father": int(form.father),
								"mother": int(form.mother)}
								
			family_member = fmo.add_member(family_member=family_member)
			
			if family_member:
				session.selected_family_member = family_member.get("id")
			else:
				session.selected_family_member = 0
				
			web.seeother("/family_members")
			
		elif form.btn_input == "Reset":
			web.seeother("/family_member_add")
		
		elif form.btn_input == "Cancel":
			web.seeother("/family_members")
		
		else:
			web.seeother("/")	
			
if __name__ == "__main__":
	app.run()
