from database import Base
from sqlalchemy import Text,String,Boolean,Integer,Column,ForeignKey
from sqlalchemy_utils import ChoiceType,relationships

# User Model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(25),unique=True)
    email = Column(String(50),unique=True)
    password = Column(Text,nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationships("Order",back_populates = "users")


    def __repr__(self):
        return f'<User {self.username}>'

# Order Model
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    order_statuses = (
        ('pending', 'pending'),
        ('proceed', 'proceed'),
        ('delivered', 'delivered'),
    )
    order_status = Column(ChoiceType(choices=order_statuses),default="pending")

    pizza_sizes = (
        ('small','small')
        ('medium','medium')
        ('large','large')
        ('extra-large','extra-large')
    )
    pizza_size = Column(ChoiceType(choices=pizza_sizes),default="small")
    user = relationships("User",back_populates = "orders")

    def __repr__(self):
        return f'<Order {self.id}>'

