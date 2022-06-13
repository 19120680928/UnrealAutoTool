from unreal import EditorUtilityLibrary,TextureMipGenSettings,log

select_asset=EditorUtilityLibrary.get_selected_assets()
asset_num=len(select_asset)
replaced=0
pattern="T_"

for asset in select_asset:
    asset_name = asset.get_fname()
    if asset_name.contains(asset,pattern):
        asset_obj=EditorUtilityLibrary.load_aseet(asset)
        asset_obj.set_editor_property("Mip Gen Settings",TextureMipGenSettings.TMGS_NO_MIPMAPS)
        

        log("设置了{}".format(asset))
        replaced+=1
        break
log("设置了{}个纹理".format(replaced))
        
        
