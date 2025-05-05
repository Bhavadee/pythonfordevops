import json

users = '''
{
    "people": [
        {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com",
            "skills": ["Python", "Machine Learning"],
            "is_active": true,
            "subscription": null
        },
        {
            "id": 2,
            "name": "Bob",
            "email": "bob@example.com",
            "skills": ["Java", "Spring Boot"],
            "is_active": false,
            "subscription": "Premium"
        },
        {
            "id": 3,
            "name": "Carol",
            "email": "carol@example.com",
            "skills": ["JavaScript", "React"],
            "is_active": true,
            "subscription": "Basic"
        }
    ]
}
'''

# Parse the JSON string into a Python dictionary
parsed_users = json.loads(users)
print(parsed_users)
# Access the 'people' key
people_list = parsed_users['people']
print("  ")
# Print the type (should be <class 'list'>)
for person in people_list:
        del person['name']
new_string = json.dumps(parsed_users, indent = 2)
print(new_string)

