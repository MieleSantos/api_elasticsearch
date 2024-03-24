from pydantic import BaseModel, Field


class SearchModel(BaseModel):
    text: str = Field(default=None)
