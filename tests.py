from based_way import integrate
from streams import integrate_threaded
from processes import integrate_proc
from Cython import integrate as integrate_cython
import unittest

def square(x):
    return x**2

class TestMySolution(unittest.TestCase):

  def test_based(self):
    self.assertAlmostEqual(integrate(square, 0, 100, n_iter=1000), 332833.5, delta= 0.001)
    self.assertAlmostEqual(integrate(square, 0, 100, n_iter=1000000), 333332.8333334973, delta=0.000001)

  def test_streams(self):
    self.assertAlmostEqual(integrate_threaded(square, 0, 100, n_iter=1000), 332833.5, delta= 0.001)
    self.assertAlmostEqual(integrate_threaded(square, 0, 100, n_iter=1000000), 333332.8333334973, delta=0.000001)

  def test_proc(self):
    self.assertAlmostEqual(integrate_proc(square, 0, 100, n_iter=1000), 332833.5, delta= 0.001)
    self.assertAlmostEqual(integrate_proc(square, 0, 100, n_iter=1000000), 333332.8333334973, delta=0.000001)

  def test_cython(self):
    self.assertAlmostEqual(integrate_cython(square, 0, 100, n_iter=1000), 332833.5, delta= 0.001)
    self.assertAlmostEqual(integrate_cython(square, 0, 100, n_iter=1000000), 333332.8333334973, delta=0.000001)

if __name__ == '__main__':
  unittest.main()