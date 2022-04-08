from pydantic import BaseModel, AnyUrl


class Url(BaseModel):
    url: AnyUrl
