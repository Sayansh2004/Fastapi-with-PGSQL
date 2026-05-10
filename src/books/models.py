from sqlalchemy.orm import Mapped, mapped_column
from src.db.main import Base
from datetime import datetime
import  uuid


class Book(Base):
    __tablename__="books"

    uid: Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    title:Mapped[str]
    author:Mapped[str]
    publisher:Mapped[str]
    published_date:Mapped[str]
    page_count:Mapped[int]
    language:Mapped[str]
    created_at:Mapped[datetime]
    updated_at:Mapped[datetime] 

