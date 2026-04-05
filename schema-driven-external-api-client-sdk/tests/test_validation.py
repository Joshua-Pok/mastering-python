from validation import parse_users

def test_happy_path():

    users = [
        {
            "id": 1,
            "username": "john",
            "email": "john@yahoo.com",
            "is_active": True
        },
        {
            "id": 2,
            "username": "jane",
            "email": "jane@gmail.com",
            "is_active": False,
        }
    ]


    created_users = parse_users(users)

    assert len(created_users) == 2# Check first user

    assert created_users[0].id == 1
    assert created_users[0].username == "john"
    assert created_users[0].email == "john@yahoo.com"
    assert created_users[0].is_active == True

    # Check second user
    assert created_users[1].id == 2
    assert created_users[1].username == "jane"
    assert created_users[1].email == "jane@gmail.com"
    assert created_users[1].is_active == False



