import unittest
from unittest.mock import patch
from stud import student as Student

class Test_student (unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Set Up!')
    
    @classmethod
    def tearDownClass(cls):
        print('tearDown')
    
    def setUp(self):
        print('setting up...')
        self.s_1 = Student('Jeff','Sun', '0110', 88)
        self.s_2 = Student('Yanness','Huang', '0918', 98)
    
    def tearDown(self):
        print('tear down\n')
    
    def test_full_name(self):
        print('testing full_name functionality:')
        self.assertEqual(self.s_1.full_name, 'Jeff Sun')
        self.assertEqual(self.s_2.full_name, 'Yanness Huang')
        
        self.s_1.first = 'Zhu'
        
        self.assertEqual(self.s_1.full_name, 'Zhu Sun')
        
    def test_student_id(self):
        print('testing student_id functionality:')
        self.assertEqual(self.s_1.student_id, 'JeffSun.0110')
        self.assertEqual(self.s_2.student_id, 'YannessHuang.0918')
        
        self.s_2.last = "Cho"
        self.assertEqual(self.s_2.student_id, 'YannessCho.0918')
        
    def test_mark_boost(self):
        print('testing mark_boost functionality:')
        self.assertEqual(self.s_1.apply_mark_boost(), 93)
        self.assertEqual(self.s_2.apply_mark_boost(), 100)
        
    def test_student_schedule(self):
        print('testing student_schedule functionality:')
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.text = 'Success'
            
            self.assertEqual(self.s_1.student_schedule(), 'Success')
            mocked_get.assert_called_with('http://localhost:0110/Jeff Sun')
            
            mocked_get.return_value.status_code = 404
            with self.assertRaises(ValueError):
                self.s_2.student_schedule()
            
    
        
if __name__ == '__main__':
    unittest.main()
        