import allure

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal
from tools.logger import get_logger  # Импортируем функцию для создания логгера

logger = get_logger("USERS_ASSERTIONS")  # Создаем логгер с именем "USERS_ASSERTIONS"


@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    # Логируем факт начала проверки
    logger.info("Check create user response")

    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


@allure.step("Check user")
def assert_user(request: UserSchema, response: UserSchema):
    """
    Проверяет, что ответ на получение данных пользователя соответствует данным.

    :param request: Ответ API при создании пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    # Логируем факт начала проверки
    logger.info("Check user")

    assert_equal(response.email, request.email, "id")
    assert_equal(response.email, request.email, "email")
    assert_equal(response.last_name, request.last_name, "last_name")
    assert_equal(response.first_name, request.first_name, "first_name")
    assert_equal(response.middle_name, request.middle_name, "middle_name")


@allure.step("Check get user response")
def assert_get_user_response(
        create_user_response: CreateUserResponseSchema,
        get_user_response: GetUserResponseSchema
):
    """
    Проверяет что данные пользователя при создании и при запросе совпадают.

    :param create_user_response: Ответ API при создании пользователя.
    :param get_user_response: Ответ API при запросе пользователя.
    :raises AssertionError: Если объекты не совпадают.
    """
    # Логируем факт начала проверки
    logger.info("Check get user response")

    assert_user(create_user_response.user, get_user_response.user)
