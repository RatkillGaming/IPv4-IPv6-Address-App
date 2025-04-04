"""
Team: PiYuMi
Members:
- Zeth Pineda (UI/Testing)
- John Sydney Yusico (Core Logic)
- Jonwyl Sarmiento (API Integration)
"""

from converter import ip_to_binary, validate_ip
from geo_api import get_geolocation
import logging

def main():
    """Main application interface - by Zeth"""
    print("IPv4/IPv6 Address Application")
    print("=============================\n")
    
    while True:
        ip = input("Enter IP address (or 'quit' to exit): ")
        
        if ip.lower() == 'quit':
            break
        
        if not validate_ip(ip):
            print("Invalid IP address format\n")
            continue
        
        binary = ip_to_binary(ip)
        print(f"\nBinary representation: {binary}")
        
        # Jonwyl's geolocation feature
        if '.' in ip:  # IPv4 only for geolocation
            geo = get_geolocation(ip)
            if geo:
                print(f"\nGeolocation Data:")
                print(f"Country: {geo.get('country_name', 'N/A')}")
                print(f"Region: {geo.get('region_name', 'N/A')}")
                print(f"City: {geo.get('city', 'N/A')}")
            else:
                print("Geolocation data unavailable")
        
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.INFO)  # Jonwyl's logging
    main()