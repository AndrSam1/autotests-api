from pydantic import BaseModel, Field, constr, ConfigDict
from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: constr(min_length=1, max_length=250)
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: constr(min_length=1)
    preview_file: FileSchema = Field(alias="previewFile")  # Вложенная структура файла
    estimated_time: str | None = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")  # Вложенная структура пользователя


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


# Добавили описание структуры запроса на создание курса
class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
