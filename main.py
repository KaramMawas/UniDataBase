class students:


	def __init__(self, first, last, Mnum, major, fees):

		self.first = first
		self.last = last
		self.Mnum = Mnum # Matrikulation_Number
		self.major = major
		self.fees = fees

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def email(self):
		return list(self.first.upper())[0]+'.'+list(self.last.upper())[0]+'_'+str(self.Mnum)+'@University.info'


#-----------------------------------------------------
class Professors(students):
	
	def __init__(self, first, last, Mnum, salary, modules):
		# super().__init__(first , last)
		# students.__init__(self, first ,last)
		self.first = first
		self.last = last
		self.Mnum = Mnum
		self.salary = salary
		self.modules = modules

#-----------------------------------------------------
class Manager(Professors):

	def __init__(self, first, last, salary, student=None):
		super().__init__(first , last, salary)

	def add_student(self, std):
		if std not in self.student:
			self.student.append(std)

	def remove_student(self, std):
		if std  in self.student:
			self.student.remove(std)

	def print_emps(self):
		for std in self.student:
			print('-->', std.fullname())

########### Examples ###########

stud_1 = students('Karam','Mawas', '0000001', 'Geomatics', '100$')
prof_1 = Professors('Fahid','Al Hussain','11111', '50k$', 'Math, Python')



print(stud_1.email())
print(stud_1.fullname())


print(prof_1.email())