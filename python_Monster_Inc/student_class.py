from monster_main import *


class Students(Monster):

    def __init__(self, f_name, l_name, student_id, skills=[]):
        super().__init__(f_name, l_name)
        self.student_id = student_id
        self.skills = [skills]
