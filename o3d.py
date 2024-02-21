import open3d as o3d
import numpy as np

# kota = "kota_circuit2.ply"

# pcd = o3d.io.read_point_cloud(kota)

# o3d.visualization.draw_geometries_with_editing([pcd])

crop = "cropped_1.ply"
pcd_crop = o3d.io.read_point_cloud(crop)
# o3d.visualization.draw_geometries([pcd_crop])

pcd_crop.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.5, max_nn=100))
# o3d.visualization.draw_geometries([pcd_crop])
# o3d.io.write_point_cloud("cropped_1_ascii.ply",pcd_crop,write_ascii=True)


# normal = np.array(pcd_crop.normals)
colors = np.array(pcd_crop.colors)


# for i in range(len(normal)):
#     if(normal[i][2] >= 0.99):
#         colors[i][0] = 1
#         colors[i][1] = 0
#         colors[i][2] = 0
# pcd_crop.colors = o3d.utility.Vector3dVector(colors)
# o3d.visualization.draw_geometries([pcd_crop])

for i in range(len(colors)):
     if(colors[i][1] > 0.52 and colors[i][2]>0.59):
         colors[i][0] = 1
         colors[i][1] = 0
         colors[i][2] = 0

pcd_crop.colors = o3d.utility.Vector3dVector(colors)
o3d.visualization.draw_geometries([pcd_crop])

o3d.io.write_point_cloud("cropped_1_color.ply",pcd_crop,write_ascii=True)



