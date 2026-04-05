from typing import Any
from models import User
from exceptions import APIContractError


def parse_users(payload: list[dict[str, Any]]) -> list[User]:


    res = []

    for data in payload:
        try:

            id = data["id"]
            username = data["username"] # we use [] instead of .get() so we dont fail silently, .get() returns None 
            email = data["email"]
            is_active = data["is_active"]


            user = User(id, username, email, is_active)
            res.append(user)


        except KeyError:
            raise APIContractError("Missing Required Key", data, {
                "id": "int",
                "username": "str",
                "email": "str",
                "is_active": "bool"

            })


    return res

