import yaml

print('========== validate.py:')
with open('apps.yaml', 'r') as file:
    data = yaml.safe_load(file)

if len(data) > 2700:
    print('data found')
    exit(0)
else:
    print('data not found')
    exit(1)
