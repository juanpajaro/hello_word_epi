#!/usr/bin/env python3

import unittest
from taller_1_intro import function_saludo

class TestTaller1(unittest.TestCase):
    def test_function_saludo(self):
        self.assertEqual(function_saludo("Juan"), "Hola Juan")

if __name__ == '__main__':
    unittest.main()


