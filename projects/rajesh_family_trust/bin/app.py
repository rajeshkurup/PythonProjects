import web
import markdown
import json
import pymongo
from rajesh_family_trust.family_member import *
from bson import json_util
from pymongo import MongoClient

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

mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db_rft = mongo_client.rajesh_family_trust

class Index(object):
	def GET(self):
		if mongo_db_rft.family_members.count() > 0:
			session.selected_family_member = mongo_db_rft.family_members.find().next().get("id")
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
			for family_member in mongo_db_rft.family_members.find():	
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
		family_member = mongo_db_rft.family_members.find({"id" : session.selected_family_member}).next()
		html_content = '<h1>Family Member</h1>'
		html_content += '<br><p>Details of Family Member</p>'
		html_content += '<br><p><form action="/family_member_edit" method="POST">'
		html_content += '<br><p>Name: %s </p>' % family_member.get("name")
		html_content += '<br><p>Age: %s </p>' % family_member.get("age")
		html_content += '<br><p>Gender: %s </p>' % family_member.get("gender")
		html_content += '<br><p>Job: %s </p>' % family_member.get("job")
		html_content += '<br><p>Office: %s </p>' % family_member.get("office")
		html_content += '<br><input type="submit" name="btn_edit" value="Edit" />'
		html_content += '<input type="submit" name="btn_family_members" value="Family Members" />'
		html_content += '<input type="submit" name="btn_home" value="Home" /></form></p>'
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
			mongo_db_rft.family_members.remove({"id" : session.selected_family_member})
			
			if mongo_db_rft.family_members.count() > 0:
				session.selected_family_member = mongo_db_rft.family_members.find().next().get("id")
			else:
				session.selected_family_member = 0
	
			web.seeother("/family_members")

		elif form.btn_input == "Home":
			web.seeother("/")
			
		else:
			web.seeother("/")
		
class FamilyMemberEdit(object):
	def GET(self):
		family_member = mongo_db_rft.family_members.find({"id" : session.selected_family_member}).next()
		html_content = '<h1>Edit Family Member</h1>'
		html_content += '<br><p>Edit the Details of Family Member</p>'
		html_content += '<br><p><form action="/family_member_submit" method="POST">'
		html_content += '<br><p>Name: <input type="text" name="name" value="%s" /></p>' % family_member.get("name")
		html_content += '<br><p>Age: <input type="text" name="age" value="%s" /></p>' % family_member.get("age")
		html_content += '<br><p>Gender: <input type="text" name="gender" value="%s" /></p>' % family_member.get("gender")
		html_content += '<br><p>Job: <input type="text" name="job" value="%s" /></p>' % family_member.get("job")
		html_content += '<br><p>Office: <input type="text" name="office" value="%s" /></p>' % family_member.get("office")
		html_content += '<br><input type="submit" name="btn_submit" value="Submit" />'
		html_content += '<input type="submit" name="btn_reset" value="Reset" />'
		html_content += '<input type="submit" name="btn_cancel" value="Cancel" /></form></p>'
		content = md.convert(html_content)
		return render.layout(content=content)
	
	def POST(self):
		form = web.input(btn_edit=None, btn_family_members=None, btn_home=None)
		if form.btn_edit:
			web.seeother("/family_member_edit")
			
		elif form.btn_family_members:
			web.seeother("/family_members")
			
		elif form.btn_home:
			web.seeother("/")
			
		else:
			web.seeother("/")
		
class FamilyMemberSubmit(object):
	def POST(self):
		form = web.input(btn_submit=None, btn_reset=None, btn_cancel=None, name=None, age=None, gender=None, job=None, office=None)
		if form.btn_submit:
			mongo_db_rft.family_members.update({"id" : session.selected_family_member}, 
												{"id" : session.selected_family_member, 
												"name" : form.name,
												"age" : form.age,
												"gender" : form.gender,
												"job" : form.job,
												"office" : form.office})

			web.seeother("/family_member")
			
		elif form.btn_reset:
			web.seeother("/family_member_edit")
		
		elif form.btn_cancel:
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
		html_content += '<br><input type="submit" name="btn_add" value="Add" />'
		html_content += '<input type="submit" name="btn_reset" value="Reset" />'
		html_content += '<input type="submit" name="btn_cancel" value="Cancel" /></form></p>'
		content = md.convert(html_content)
		return render.layout(content=content)

class FamilyMemberCreate(object):
	def POST(self):
		form = web.input(btn_add=None, btn_reset=None, btn_cancel=None, name=None, age=None, gender=None, job=None, office=None)
		if form.btn_add:
			new_member_id = mongo_db_rft.family_members.count() + 1
			mongo_db_rft.family_members.insert({"id" : new_member_id, 
												"name" : form.name,
												"age" : form.age,
												"gender" : form.gender,
												"job" : form.job,
												"office" : form.office})
			
			session.selected_family_member = new_member_id
			web.seeother("/family_members")
			
		elif form.btn_reset:
			web.seeother("/family_member_add")
		
		elif form.btn_cancel:
			web.seeother("/family_members")
		
		else:
			web.seeother("/")	
			
if __name__ == "__main__":
	app.run()
