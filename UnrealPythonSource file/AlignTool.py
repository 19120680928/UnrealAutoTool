from unreal import EditorLevelLibrary

actors = EditorLevelLibrary().get_selected_level_actors()
index=0
def align_location_to_x(actors,a_index):
#获得第一个和下一个actor的实例
    first_actor = actors[a_index]
    next_actor = actors[a_index+1] 
# 获得世界位置
    first_vector = first_actor.get_actor_location()
#获得边界向量，返回一个列表
    first_bonunds = first_actor.get_actor_bounds(False,False)
# 获得x轴对齐新位置
    next_x = first_bonunds[1].x*2+first_vector.x
#设置新位置
    set_local = (next_x,first_vector.y,first_vector.z)
    next_actor.set_actor_location(set_local,False,False)
    a_index = a_index+1
#递归条件   
    if len(actors)-1>a_index:
        align_location_to_x(actors,a_index)
    print('成功对齐了{}个actor'.format(a_index))
align_location_to_x(actors,index)


    
