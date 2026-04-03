import unittest
import pycalc.pycalc as calculator

class PyCalcUnitTests(unittest.TestCase):
  def test_add(self):
    left = [5,10,7,365,0,0,0,-50,-12,-4,32,4,-16,-7]
    right = [9,5,0,-2,445,0,-54,100,0,-49,-32,-6,16,5]
    expected = [14,15,7,363,445,0,-54,50,-12,-53,0,-2,0,-2]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.add(l, r)
        self.assertEqual(got, e)

if __name__ == '__main__':
  unittest.main()
