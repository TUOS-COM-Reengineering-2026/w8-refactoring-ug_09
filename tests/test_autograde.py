import os
import unittest

class TestMiniReport(unittest.TestCase):
    def test_mini_report_exists_and_size(self):
        self.assertTrue(os.path.exists("mini-report.pdf"), 'Cannot find mini-report.pdf')
        self.assertGreater(os.path.getsize("mini-report.pdf"), 10000, 'Your mini report is too short.')

if __name__ == "__main__":
    unittest.main()