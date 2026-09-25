from pydantic import BaseModel, field_validator, Field

class createUser(BaseModel):
    user: str = Field(min_length=3, max_length=18)
    email: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, password):
        if len(password) < 8:
            raise ValueError("Password needs to be atleast 8 characters")

        if not any((c.upper()) for c in password):
            raise ValueError("Password needs to contain atleast one uppercase letter")

        if not any((c.lower()) for c in password):
            raise ValueError("Password needs to contain atleast one lowercase letter")

        if not any(c.isdigit() for c in password):
            raise ValueError("Password needs to contain atleast one digit")

        if all(c.alnum() for c in password):
            raise ValueError("Password needs to contain atleast one specialized charcter")
        
        return password

    @field_validator("email")
    @classmethod
    def check_email(cls, email):
        if not any(c == "@" for c in email):
            raise ValueError("Email is not appropriate")

        #TODO
        #More validations

        return email