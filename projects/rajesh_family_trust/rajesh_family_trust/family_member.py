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
		if family_member:
			new_member_id = rajesh_family_trust.family_members.count() + 1
			rajesh_family_trust.family_members.insert({"id": new_member_id, 
														"name": family_member.get("name"),
														"age": family_member.get("age"),
														"gender": family_member.get("gender"),
														"job": family_member.get("job"),
														"office": family_member.get("office")})
														
		else:
			return None
			
		return self.get_member(id=new_member_id)
											
	def delete_member(self, id=None):
		rajesh_family_trust.family_members.remove({"id": id})
		return self.get_first_member()
	
	def update_member(self, family_member=None):
		if family_member:
			rajesh_family_trust.family_members.update({"id": family_member.get("id")}, {"id": family_member.get("id"), 
																						"name": family_member.get("name"),
																						"age": family_member.get("age"),
																						"gender": family_member.get("gender"),
																						"job": family_member.get("job"),
																						"office": family_member.get("office")})
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
			if family_member:
				family_members.append({"id": family_member.get("id"),
										"name": family_member.get("name"),
										"age": family_member.get("age"),
										"gender": family_member.get("gender"),
										"job": family_member.get("job"),
										"office": family_member.get("office")})
										
			else:
				continue
			
		return family_members
