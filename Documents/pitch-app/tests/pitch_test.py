import unittest
from app.models import Pitch
# from app import create_app

class NewsTest(unittest.TestCase):
        '''
        Test class to test the behavior of the news source class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_pitch = Pitch(1, 1,'my pitch', 'pitch',
                                        'product', 'great to use', 0, 0)

        def test_instance(self):
            '''
            '''
            self.assertTrue(isinstance(self.new_pitch, Pitch))

        def test_to_check_instance_variables(self):
            '''
            '''
            self.assertEquals(self.new_pitch.id, 1)
            self.assertEquals(self.new_pitch.user_id, 1)
            self.assertEquals(self.new_pitch.post, 'my pitch')
            self.assertEquals(self.new_pitch.title, 'pitch')
            self.assertEquals(self.new_pitch.category, 'product')
            self.assertEquals(self.new_pitch.comment, 'great to use')
            self.assertEquals(self.new_pitch.upvote, 0)
            self.assertEquals(self.new_pitch.downvote, 0)




if __name__ == '__main__':
    unittest.main()