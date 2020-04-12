import re
m = '"raw_title":"【新品享6期免息】红米k30 索尼6400万大电量120Hz智能游戏学生手机K20升级redmi小米官方旗舰店网正品xiaomi","raw_title":"【新品享6期免息】红米k30 索尼6400万大电量120Hz智能游戏学生手机K20升级redmi小米官方旗舰店网正品xiaomi",'
print('m:',m)
print(re.findall('"raw_title":(.*?),',m))