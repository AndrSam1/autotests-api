from pydantic import BaseModel, Field, EmailStr, UUID4, constr

from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Модель данных пользователя
    """
    id: UUID4
    email: EmailStr = Field(min_length=1, max_length=250)
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Запрос на создание пользователя
    """
    email: EmailStr = Field(min_length=1, max_length=250, default_factory=lambda: get_random_email())
    password: constr(min_length=1, max_length=250) = Field(default="string")
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName", default="string")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName", default="string")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName", default="string")


class CreateUserResponseSchema(BaseModel):
    """
    Ответ с данными созданного пользователя
    """
    user: UserSchema
