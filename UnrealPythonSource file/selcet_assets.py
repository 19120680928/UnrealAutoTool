import unreal

def select_assetNum():
    #实例化UE引擎的类
    System_lib=unreal.SystemLibrary
    editor_util=unreal.EditorUtilityLibrary
    string_lib=unreal.StringLibrary

    #选择资产
    select_asset=editor_util.get_selected_assets()
    num_assets=len(select_asset)
    replaced= 0

    print("选额",num_assets,"资产")
    unreal.log("Selected {} asset/s".format(num_assets))
    
select_assetNum()