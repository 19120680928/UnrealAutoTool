import unreal
asset_path = ""
def set_high_detail(static_mesh):
    # 设置LOD组。
    static_mesh.set_editor_property("lod_group", "HighDetail")
    # 保存资源。
    unreal.EditorAssetLibrary.save_loaded_asset(static_mesh)
# 获取路径中所有资源的列表。
all_assets = unreal.EditorAssetLibrary.list_assets(asset_path)
# 将它们都加载到内存中。
all_assets_loaded = [unreal.EditorAssetLibrary.load_asset(a) for a in all_assets]
# 过滤列表以仅包括静态网格体。
static_mesh_assets = unreal.EditorFilterLibrary.by_class(all_assets_loaded, unreal.StaticMesh)
# 对列表中的各个静态网格体运行此函数。
list(map(set_high_detail, static_mesh_assets))