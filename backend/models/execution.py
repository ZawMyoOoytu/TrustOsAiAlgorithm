from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

from backend.db.database import Base

class Execution(Base):

    __tablename__ = "executions"

    id = Column(Integer, primary_key=True)

    execution_id = Column(String)

    task = Column(String)

    trust_score = Column(Integer)

    status = Column(String)

    result = Column(String)