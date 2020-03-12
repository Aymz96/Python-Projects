from monster_main import *


class teachers(Monster):

    def __init__(self, f_name, l_name, staff_id, skills=[]):
        super().__init__(f_name, l_name)
        self.staff_id = staff_id
        self.skills = [skills]

