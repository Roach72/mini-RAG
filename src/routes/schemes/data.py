from pydantic import BaseModel
from typing import Optional

class processRequest(BaseModel):
    file_id: str
    chunk_size: Optional[int] = 100
    overlap_size: Optional[int] = 20
    reset: Optional[int] = 0
    do_reset: int