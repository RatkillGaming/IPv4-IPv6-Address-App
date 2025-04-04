"""
Team: PiYuMi
Members:
- Zeth Pineda (UI/Testing)
- John Sydney Yusico (Core Logic)
- Jonwyl Sarmiento (API Integration)
"""

import unittest
from converter import validate_ip, ip_to_binary, expand_ipv6

class TestIPFunctions(unittest.TestCase):
    """Test cases by Zeth"""
    
    def test_validate_ip(self):
        self.assertTrue(validate_ip("192.168.1.1"))
        self.assertTrue(validate_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
        self.assertFalse(validate_ip("300.400.500.600"))
        self.assertFalse(validate_ip("not_an_ip"))
    
    def test_ip_to_binary(self):
        self.assertEqual(ip_to_binary("192.168.1.1"), "11000000.10101000.00000001.00000001")
        self.assertTrue("0010000000000001" in ip_to_binary("2001:db8::1"))
    
    def test_expand_ipv6(self):
        self.assertEqual(expand_ipv6("2001:db8::1"), 
                        "2001:0db8:0000:0000:0000:0000:0000:0001")
        self.assertEqual(expand_ipv6("::1"), 
                        "0000:0000:0000:0000:0000:0000:0000:0001")

if __name__ == "__main__":
    unittest.main()