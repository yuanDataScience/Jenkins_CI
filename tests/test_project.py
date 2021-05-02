import unittest   # The test framework
import quicksort as st
import random

class Project_Test(unittest.TestCase):
     def test_simple(self):
         testList = [4,3,2,1]
         expectedList = [1,2,3,4]
         st.quickSort(testList)
         self.assertEqual(testList, expectedList)
         
     def test_dec(self):
         testList = [5, 4, 3, 2, 1]
         expectedList=[1, 2, 3, 4, 5]
         st.quickSort(testList)
         self.assertEqual(testList, expectedList)


     def test_empty(self):
         testList = []
         expectedList = testList.copy()
         expectedList.sort()
         st.quickSort(testList)
         self.assertEqual(testList, expectedList)

     def test_alpha(self):
         testList = ['Judy','Dave','Holly','Jeff']
         expectedList = testList.copy()
         expectedList.sort()
         st.quickSort(testList)
         self.assertEqual(testList, expectedList)

     def test_negative(self):
         testList = [-4,-3,-2,-1]
         expectedList = testList.copy()
         expectedList.sort()
         st.quickSort(testList)
         self.assertEqual(testList, expectedList)
         
     def test_random(self):
         testList = [random.randint(0, 20),random.randint(0, 20),random.randint(0, 20),random.randint(0, 20)]
         expectedList = testList.copy()
         expectedList.sort()
         st.quickSort(testList)
         self.assertEqual(testList, expectedList)

if __name__ == '__main__':
    import xmlrunner
    print ('running main')
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
