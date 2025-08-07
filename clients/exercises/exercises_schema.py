from pydantic import BaseModel, Field, constr, ConfigDict


class Exercise(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: constr(min_length=1, max_length=250)
    course_id: str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: constr(min_length=1)
    estimated_time: constr(min_length=1, max_length=50) | None = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка упражнений.
    """
    exercises: list[Exercise]


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение упражнения.
    """
    exercise: Exercise


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
