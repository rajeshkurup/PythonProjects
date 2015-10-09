import json
import pymongo
from bson import json_util
from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017/')
rajesh_family_trust = mongo_client.rajesh_family_trust

class FamilyMember(object):
	def __init__(self):
		self.id = 0
		self.name = ""
		self.age = ""
		self.gender = ""
		self.job = ""
		self.office = ""

class FamilyMemberOperator(object):
	def __init__(self):
		pass

	def add_member(self, family_member=FamilyMember()):
		family_member.id = rajesh_family_trust.family_members.count() + 1
		rajesh_family_trust.family_members.insert({"id" : family_member.id, 
											"name" : family_member.name,
											"age" : family_member.age,
											"gender" : family_member.gender,
											"job" : family_member.job,
											"office" : family_member.office})
		return family_member
											
	def delete_member(self, id=None):
		try:
			col_cursor = rajesh_family_trust.family_members.find({"id" : id})
			db_family_member = col_cursor.next()
			rajesh_family_trust.family_members.remove({"id" : id})
			return self.get_first_member()

		except StopIteration:
			return None
			
	def update_member(self, family_member=FamilyMember()):
		try:
			col_cursor = rajesh_family_trust.family_members.find({"id" : family_member.id})
			db_family_member = col_cursor.next()
			rajesh_family_trust.family_members.update({"id" : family_member.id}, {"id" : family_member.id, 
																					"name" : family_member.name,
																					"age" : family_member.age,
																					"gender" : family_member.gender,
																					"job" : family_member.job,
																					"office" : family_member.office})
			return True
			
		except StopIteration:
			return False
			
	def get_member(self, id=None):
		try:
			col_cursor = rajesh_family_trust.family_members.find({"id" : id})
			db_family_member = col_cursor.next()
			family_member = FamilyMember()
			family_member.name = db_family_member.get("name")
			family_member.age = db_family_member.get("age")
			family_member.gender = db_family_member.get("gender")
			family_member.job = db_family_member.get("job")
			family_member.office = db_family_member.get("office")
			return family_member
			
		except StopIteration:
			return None

	def get_first_member(self):
		try:
			col_cursor = rajesh_family_trust.family_members.find()
			db_family_member = col_cursor.next()
			first_family_member = FamilyMember()
			first_family_member.id = db_family_member.get("id")
			first_family_member.name = db_family_member.get("name")
			first_family_member.age = db_family_member.get("age")
			first_family_member.gender = db_family_member.get("gender")
			first_family_member.job = db_family_member.get("job")
			first_family_member.office = db_family_member.get("office")
			return first_family_member
			
		except StopIteration:
			return None

	def get_all_members(self):
		family_members = []
		for family_member in rajesh_family_trust.family_members.find():
			if family_member:
				temp_family_member = FamilyMember()
				temp_family_member.id = family_member.get("id")
				temp_family_member.name = family_member.get("name")
				temp_family_member.age = family_member.get("age")
				temp_family_member.gender = family_member.get("gender")
				temp_family_member.job = family_member.get("job")
				temp_family_member.office = family_member.get("office")
				family_members.append(temp_family_member)
			
		return family_members
