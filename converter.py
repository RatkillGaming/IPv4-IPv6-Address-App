"""
Team: PiYuMi
Members:
- Zeth Pineda (UI/Testing)
- John Sydney Yusico (Core Logic)
- Jonwyl Sarmiento (API Integration)
"""

import re
import ipaddress

def validate_ip(ip_str):
    """Validate IPv4 or IPv6 address - by Johnasd"""
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def ip_to_binary(ip_str):
    """Convert IP to binary representation - by John"""
    try:
        ip_obj = ipaddress.ip_address(ip_str)
        binary_str = ''.join(f'{byte:08b}' for byte in ip_obj.packed)
        
        # Formatting for better readability
        if ip_obj.version == 4:
            return '.'.join([binary_str[i:i+8] for i in range(0, 32, 8)])
        else:  # IPv6
            return ':'.join([binary_str[i:i+16] for i in range(0, 128, 16)])
    except ValueError:
        return "Invalid IP address"

def expand_ipv6(ipv6_str):
    """Expand shortened IPv6 address - by John"""
    try:
        return ipaddress.IPv6Address(ipv6_str).exploded
    except ipaddress.AddressValueError:
        return "Invalid IPv6 address"