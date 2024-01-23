import requests
from bs4 import BeautifulSoup
import re

def get_carrier(tracking_number):
    # Define regular expressions for USPS, UPS, and FedEx tracking numbers
    usps_pattern = re.compile(r'^\d{22}$')
    ups_pattern = re.compile(r'^1Z[0-9A-Z]{16}$')
    fedex_pattern = re.compile(r'^\d{12}$')

    if usps_pattern.match(tracking_number):
        return 'usps'
    elif ups_pattern.match(tracking_number):
        return 'ups'
    elif fedex_pattern.match(tracking_number):
        return 'fedex'
    else:
        return None

def track_usps(tracking_number):
    url = f'https://tools.usps.com/go/TrackConfirmAction?tLabels={tracking_number}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    status = soup.find('div', class_='status').text.strip()
    estimated_delivery_date = soup.find('div', class_='date-bold').text.strip()

    return status, estimated_delivery_date

def track_ups(tracking_number):
    url = f'https://www.ups.com/track?tracknum={tracking_number}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    status = soup.find('div', class_='tt_shipped_on').text.strip()
    estimated_delivery_date = soup.find('div', class_='tt_delivered_on').text.strip()

    return status, estimated_delivery_date

def track_fedex(tracking_number):
    url = f'https://www.fedex.com/apps/fedextrack/?tracknumbers={tracking_number}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    status = soup.find('div', class_='fx-accordion-pane-status').text.strip()
    estimated_delivery_date = soup.find('div', class_='fx-accordion-pane-est-delivery').text.strip()

    return status, estimated_delivery_date

def main():
    tracking_number = input("Enter your tracking number: ")
    carrier = get_carrier(tracking_number)

    if carrier == 'usps':
        status, estimated_delivery_date = track_usps(tracking_number)
    elif carrier == 'ups':
        status, estimated_delivery_date = track_ups(tracking_number)
    elif carrier == 'fedex':
        status, estimated_delivery_date = track_fedex(tracking_number)
    else:
        print("Invalid tracking number or carrier.")
        return

    print(f"Status: {status}")
    print(f"Estimated Delivery Date: {estimated_delivery_date}")

if __name__ == "__main__":
    main()
