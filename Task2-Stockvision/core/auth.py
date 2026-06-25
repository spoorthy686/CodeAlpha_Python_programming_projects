
import os
import json
import hashlib


class AuthManager:

    def __init__(self):

        self.users_file = os.path.join(
            "data",
            "users",
            "users.json"
        )

        self.create_storage()

    # =================================
    # Create folders/files if missing
    # =================================

    def create_storage(self):

        os.makedirs(
            os.path.dirname(
                self.users_file
            ),
            exist_ok=True
        )

        if not os.path.exists(
            self.users_file
        ):

            with open(
                self.users_file,
                "w"
            ) as file:

                json.dump(
                    {},
                    file,
                    indent=4
                )

    # =================================
    # Load Users
    # =================================

    def load_users(self):

        try:

            with open(
                self.users_file,
                "r"
            ) as file:

                return json.load(
                    file
                )

        except:

            return {}

    # =================================
    # Save Users
    # =================================

    def save_users(
        self,
        users
    ):

        with open(
            self.users_file,
            "w"
        ) as file:

            json.dump(
                users,
                file,
                indent=4
            )

    # =================================
    # Hash Password
    # =================================

    def hash_password(
        self,
        password
    ):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    # =================================
    # Register User
    # =================================

    def register_user(
        self,
        username,
        password,
        email
    ):

        users = self.load_users()

        username = username.strip()
        email = email.strip()

        if username in users:

            return (
                False,
                "Username already exists."
            )

        if len(password) < 6:

            return (
                False,
                "Password must contain at least 6 characters."
            )

        users[username] = {

            "email": email,

            "password":
            self.hash_password(
                password
            ),

            "portfolio": [],

            "watchlist": []
        }

        self.save_users(
            users
        )

        return (
            True,
            "Registration successful"
        )

    # =================================
    # Login User
    # =================================

    def login_user(
        self,
        username,
        password
    ):

        users = self.load_users()

        username = username.strip()

        if username not in users:

            return (
                False,
                "User not found."
            )

        hashed_password = (
            self.hash_password(
                password
            )
        )

        if users[
            username
        ][
            "password"
        ] != hashed_password:

            return (
                False,
                "Incorrect password."
            )

        return (
            True,
            "Login successful"
        )

    # =================================
    # Get User Data
    # =================================

    def get_user_data(
        self,
        username
    ):

        users = self.load_users()

        return users.get(
            username,
            None
        )

    # =================================
    # Update User Data
    # =================================

    def update_user_data(
        self,
        username,
        data
    ):

        users = self.load_users()

        if username in users:

            users[
                username
            ] = data

            self.save_users(
                users
            )

            return True

        return False
