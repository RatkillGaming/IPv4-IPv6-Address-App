"""
Team: PiYuMi
Members:
- Zeth Pineda (UI/Testing)
- John Sydney Yusico (Core Logic)
- Jonwyl Sarmiento (API Integration)
"""

import requests
import logging

def get_geolocation(ip_address):
    """Get geolocation data for IPv4 address - by Jonwyl"""
    try:
        if not ip_address or not isinstance(ip_address, str):
            raise ValueError("Invalid IP address format")
            
        # Using ip-api.com free service
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        
        if data.get('status') == 'success':
            logging.info(f"Geolocation fetched for {ip_address}")
            return {
                'country_name': data.get('country'),
                'region_name': data.get('regionName'),
                'city': data.get('city'),
                'isp': data.get('isp')
            }
        else:
            logging.warning(f"Geolocation failed for {ip_address}")
            return None
            
    except Exception as e:
        logging.error(f"Geolocation error: {str(e)}")
        return None