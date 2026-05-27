Advanced IP Logger
This advanced IP logger collects more than 70 information about the user, including their IP address, user agent, referer, language, browser details, system information, and network data.

Installation
Replace YOUR_DISCORD_WEBHOOK_URL with your actual Discord Webhook URL in the logger.py file.
Save the file as logger.py.
Create a new repository on GitHub and add the logger.py file to it.
Provide instructions on how to run the script using Python (e.g., python logger.py).
Features
Collects the user's IP address.
Extracts information from the user agent string, including browser name brands, version numbers, device type, adblock status, mobile or PC status, operating system name and version.
Retrieves system information, such as platform name, version, architecture, processor, node, release, and machine.
Sends a request to ip-api.com to gather network data, including country, country code, region, region name, city, zip code, ISP, organization, latitude, longitude, timezone, AS number, and AS name.
All collected data is sent to the provided Discord Webhook URL.
