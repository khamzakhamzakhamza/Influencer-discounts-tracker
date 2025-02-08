from idt_api.domain.entities.user import User

class UserService:
    def retrive_or_create_user(self, username: str) -> User:
        # search for user in the database
        user = User(username)
        # save user if doesnt exist
        return user
