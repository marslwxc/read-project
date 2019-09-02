from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func


# engine = create_engine('mysql+mysqlconnector://root:1205014235zhe@localhost:3306/sql learning')
engine = create_engine('mysql+mysqlconnector://root:1@localhost:3306/learning')

# 创建对象的基类:
Base = declarative_base()

# 定义players对象
class Players(Base):
    # 表的名字
    __tablename__ = 'playerss'

    # 表的结构
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer)
    player_name = Column(String(255))
    height = Column(Float(3, 2))

# 创建 DBSession 类型
DBSession = sessionmaker(bind=engine)
# 创建 session 对象
session = DBSession()

# 创建 Player 对象
new_player = Players(team_id=1003, player_name=" 约翰 - 科林斯 ", height= 2.08)
# 添加到 session
session.add(new_player)

# 增加 to_dict() 方法到 Base 类中
def to_dict(self):
    return {
        c.name:getattr(self, c.name, None) for c in self.__table__.columns
    }
# 将对象可以转化为 dict 类型
Base.to_dict = to_dict
# 查询身高 >=2.08 的球员
rows = session.query(Players).filter(Player.height >= 2.08).all()
#rows = session.query(Players.team_id, func.count(Players.player_id))\
# .group_by(Players.team_id).having(func.count(Players.player_id)>5)\
# .order_by(func.count(Players.player_id).asc()).all()
print([row.to_dict() for row in rows])

row = session.query(Players).filter(Players.player_name==' 约翰 - 科林斯 ').first()
# 修改表数据
row.height = 2.17
# 删除行数据
session.delete(row)

# 提交即保存到数据库
session.commit()
# 关闭 session
session.close()