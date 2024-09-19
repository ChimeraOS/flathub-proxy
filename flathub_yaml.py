import requests

URL='https://flathub.org/api/v2/appstream'

apps = []
api_response = requests.get(URL)
if api_response.status_code == requests.codes.ok:
    for entry in api_response.json():
        flatpak_id = entry
        api_item_response = requests.get(URL + '/' + flatpak_id)
        if api_item_response.status_code != requests.codes.ok:
            continue
        data = api_item_response.json()
        if 'name' not in data or 'summary' not in data or 'releases' not in data or len(data['releases']) < 1 or 'version' not in data['releases'][0]:
            continue

        summary = data['summary'].replace('"', r'\"')
        print(f"- id: \"{flatpak_id}\"")
        print(f"  name: \"{data['name']}\"")
        print(f"  summary: \"{summary}\"")
        print(f"  version: \"{data['releases'][0]['version']}\"")
