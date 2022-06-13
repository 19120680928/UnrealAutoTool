from unreal import EditorLevelLibrary,EditorFilterLibrary, SkeletalMesh, StaticMesh, StaticMeshActor
import unreal

#get all actors of level in a arry


def getactorName():
    all_actor=EditorLevelLibrary.get_all_level_actors()

    allstaticmesh=EditorFilterLibrary.by_class(all_actor,StaticMeshActor)

    deleted=0

    for actor in allstaticmesh:
        actor_name=actor.get_fname()
        # unreal.log("关卡存在{}的actor".format(actor_name))
        actor_meshcomp=actor.static_mesh_component
        actor_mesh=actor_meshcomp.static_mesh
        # unreal.log(actor_mesh) 
        #有效的actor存在一个变量      
        isValid_actor=actor_mesh!=None
        #如果遍历过程存在空actor,如果存在假isValid
        if not isValid_actor:
            actor.destroy_actor()
            deleted +=1
            unreal.log("存在无效{}acotr,且被删除".format(actor_mesh))
    unreal.log("删除数量为{}".format(deleted))
getactorName()