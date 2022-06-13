from unreal import EditorLevelLibrary,EditorFilterLibrary,StaticMeshActor
import unreal
all_actors = EditorLevelLibrary.get_all_level_actors()
static_meshesactor = EditorFilterLibrary.by_class(all_actors,StaticMeshActor)
deleted = 0
isnotvalid_mesh = None
for actors in static_meshesactor:    # print(static_meshes)
    mesh_comp = actors.static_mesh_component
# unreal.log(mesh_comp)
    mesh=mesh_comp.static_mesh
    if mesh is  isnotvalid_mesh:
        # print("组件存在空Mesh")
        actors.destroy_actor()

        deleted += 1
print("删除了{}个空静态网格体组件".format(deleted))