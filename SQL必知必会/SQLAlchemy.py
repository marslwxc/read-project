from sqlalchemy import create_engine, Column, String, Integer, Float


engine = create_engine('mysql+mysqlconnector://root:1205014235zhe@localhost:3306/sql learning')

class Players(Base):
    # 表的名字
    __tablename__ = 'player'

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
new_player = Player(team_id=1003, player_name=" 约翰 - 科林斯 ", height= 2.08)
# 添加到 session
session.add(new_player)
# 提交即保存到数据库
session.commit()
# 关闭 session
session.close()