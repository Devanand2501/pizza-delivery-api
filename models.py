from database import Base
from sqlalchemy import Text,String,Boolean,Integer,Column,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

# User Model
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(25),unique=True)
    email = Column(String(50),unique=True)
    password = Column(Text,nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship("Order",back_populates = "user")


    def __repr__(self):
        return f'<User {self.username}>'

# Order Model
class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    quantity=Column(Integer,nullable=False)
    order_statuses = (
        ('pending', 'pending'),
        ('proceed', 'proceed'),
        ('delivered', 'delivered'),
    )
    order_status = Column(ChoiceType(choices=order_statuses),default="pending")

    pizza_sizes = (
        ('small','small'),
        ('medium','medium'),
        ('large','large'),
        ('extra-large','extra-large')
    )
    pizza_size = Column(ChoiceType(choices=pizza_sizes),default="small")
    user = relationship("User",back_populates = "orders")

    def __repr__(self):
        return f'<Order {self.id}>'

