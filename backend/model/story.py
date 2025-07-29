'''
story name
story theme

first option: 
childres = [go_left , go_right]

text:
more options

basically binary tree like structure
'''

from sqlalchemy import Column,Integer, String, Text, ForeignKey, Boolean, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import base

class Story(base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key = True, index =True)
    title = Column(String,index=True)
    session_id = Column(String, index=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now())

    node = relationship(argument='StoryNode', back_populates = "story")

class StoryNode(base):
    __tablename__= 'story_node'

    id = Column(Integer, primary_key=True, index = True)
    story_id = Column(Integer, ForeignKey("stories.id"), index= True)
    content = Column(String)
    is_root = Column(Boolean, default=False)
    is_ending = Column(Boolean, default=False)
    is_winning_ending = Column(Boolean, default=False)
    options = Column(JSON, default=[])

    story = relationship(argument= 'Stories', back_populates="node")