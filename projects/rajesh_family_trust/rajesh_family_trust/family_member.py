import json
import pymongo
from bson import json_util
from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017/')
rajesh_family_trust = mongo_client.rajesh_family_trust

class FamilyMemberOperations(object):
	def __init__(self):
		pass

	def add_member(self, family_member=None):
		new_member_id = rajesh_family_trust.family_members.count() + 1
		
		if family_member:
			family_member["id"] = new_member_id
			rajesh_family_trust.family_members.insert(family_member)
														
		else:
			return None
			
		return self.get_member(id=new_member_id)
											
	def delete_member(self, id=None):
		rajesh_family_trust.family_members.remove({"id": id})
		return self.get_first_member()
	
	def update_member(self, family_member=None):
		if family_member:
			rajesh_family_trust.family_members.update({"id": family_member.get("id")}, family_member)
			return self.get_member(id=family_member.get("id"))
				
		else:
			return None
			
	def get_member(self, id=None):
		try:
			return rajesh_family_trust.family_members.find({"id": id}).next()
			
		except StopIteration:
			return None

	def get_first_member(self):
		try:
			return rajesh_family_trust.family_members.find().next()
			
		except StopIteration:
			return None

	def get_all_members(self):
		family_members = []

		for family_member in rajesh_family_trust.family_members.find():
			family_members.append(family_member)
			
		return family_members

	def get_members(self, query=None):
		family_members = []

		for family_member in rajesh_family_trust.family_members.find(query):
			family_members.append(family_member)
			
		return family_members
		