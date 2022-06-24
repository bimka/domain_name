import unittest

from domain_name import domain_name

class DomainsTestCase(unittest.TestCase):

    def test_domain_is_string(self):
        result = domain_name("http://github.com/carbonfive/raygun")
        self.assertAlmostEqual(result, "github")

    def test_domain_is_not_string(self):
        result = domain_name(123)
        self.assertRaises(TypeError, result)


if __name__ == "__main__":
  unittest.main()