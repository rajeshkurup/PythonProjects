class FamilyMember(object):
	
	def __init__(self, name, age, gender, job, office):
		self.name = name
		self.age = age
		self.gender = gender
		self.job = job
		self.office = office

family_members = {
	"1": FamilyMember("Rajesh", "38", "Male", "Software Engineer", "PayPal"),
	"2": FamilyMember("Bindhu", "37", "Female", "Medical Coder", "Kiwi Tech"),
	"3": FamilyMember("Athul", "14", "Male", "Student", "Granada High"),
	"4": FamilyMember("Ahalya", "10", "Female", "Student", "East Avenue Middle")
}
