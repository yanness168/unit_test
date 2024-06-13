import requests

class student:
    
    mark_boost = 5
    
    def __init__ (self, first, last, birth_date, mark):
        self.first = first
        self.last = last
        self.birth_date = birth_date
        self.mark = mark
        
    @property # AKA getFullName
    def full_name (self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def student_id (self):
        return '{}{}.{}'.format(self.first, self.last, self.birth_date)
    
    def apply_mark_boost(self):
        
        if (self.mark+self.mark_boost) <= 100:
            return (self.mark+self.mark_boost)
        else:
            return 100
    
    def student_schedule (self):
        res = requests.get(f'http://localhost:{self.birth_date}/{self.full_name}')
        if res.status_code == 200:
            return res.text
        else:
            raise ValueError(f'Request failed...')
    