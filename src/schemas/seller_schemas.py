from pydantic import BaseModel


class Seller(BaseModel):
    username: str
    password: str
    email: str

class DisplaySeller(BaseModel):
    username: str
    email: str