import gvxrPython3 as gvxr

# This script uses GVirtualXRay created by Dr Franck P. Vidal
# Copyright (c) 2019, Dr Franck P. Vidal (franck.p.vidal@fpvidal.net), http://www.fpvidal.net/
# All rights reserved.

# This script is created by Jones Jernfors

# This script is for loading the 3D data into the program


# Without this, the program doesn't work
gvxr.createOpenGLContext()

# Skeleton
gvxr.loadMeshFile("skeleton", "3D_models/Bone.stl", "mm")
gvxr.scaleNode("skeleton", 0.72, 0.72, 0.72, "mm")
gvxr.rotateNode("skeleton", 90, 0, 0, -90)
gvxr.translateNode("skeleton", 0, 0, 0, "cm")
gvxr.setColor("skeleton", 0.5, 0, 0, 0.01)
gvxr.setHU("skeleton", 1500)

# Lungs
gvxr.loadMeshFile("lungs", "3D_models/Lungs.stl", "mm")
gvxr.scaleNode("lungs", 0.72, 0.72, 0.72, "mm")
gvxr.rotateNode("lungs", 90, 0, 0, -90)
gvxr.translateNode("lungs", 0, 0, 0, "cm")
gvxr.setColor("lungs", 0, 0.5, 0, 0.01)
gvxr.setHU("lungs", -1000)

# Lung Vessels
gvxr.loadMeshFile("lung vessels", "3D_models/Lung_Vessels.stl", "mm")
gvxr.scaleNode("lung vessels", 0.72, 0.72, 0.72, "mm")
gvxr.rotateNode("lung vessels", 90, 0, 0, -90)
gvxr.translateNode("lung vessels", 0, 0, 0, "cm")
gvxr.setColor("lung vessels", 0, 0.5, 0, 0.01)
gvxr.setHU("lung vessels", 300)

# Kidneys
gvxr.loadMeshFile("kidneys", "3D_models/Kidneys.stl", "mm")
gvxr.scaleNode("kidneys", 0.72, 0.72, 0.72, "mm")
gvxr.rotateNode("kidneys", 90, 0, 0, -90)
gvxr.translateNode("kidneys", 0, 0, 0, "cm")
gvxr.setColor("kidneys", 0, 0.5, 0, 0.01)
gvxr.setHU("kidneys", 300)

# Liver
gvxr.loadMeshFile("liver", "3D_models/Liver.stl", "mm")
gvxr.scaleNode("liver", 0.72, 0.72, 0.72, "mm")
gvxr.rotateNode("liver", 90, 0, 0, -90)
gvxr.translateNode("liver", 0, 0, 0, "cm")
gvxr.setColor("liver", 0, 0.5, 0, 0.01)
gvxr.setHU("liver", 300)

# Stomach Tissue Area
gvxr.loadMeshFile("stomach", "3D_models/Stomach_Tissue_area.stl", "mm")
gvxr.scaleNode("stomach", 0.72, 0.72, 0.72, "mm")
gvxr.rotateNode("stomach", 90, 0, 0, -90)
gvxr.translateNode("stomach", 0, 0, 0, "cm")
gvxr.setColor("stomach", 0, 0, 0.5, 0.01)
gvxr.setHU("stomach", 300)

# Thorax Tissue Area
gvxr.loadMeshFile("thorax", "3D_models/Thorax_Tissue_area.stl", "mm")
gvxr.scaleNode("thorax", 0.72, 0.72, 0.72, "mm")
gvxr.rotateNode("thorax", 90, 0, 0, -90)
gvxr.translateNode("thorax", 0, 0, 0, "cm")
gvxr.setColor("thorax", 0, 0, 0.5, 0.01)
gvxr.setHU("thorax", 300)

# Head Tissue Area
gvxr.loadMeshFile("head", "3D_models/Head_Tissue.stl", "mm")
gvxr.scaleNode("head", 0.72, 0.72, 0.72, "mm")
gvxr.rotateNode("head", 90, 0, 0, -90)
gvxr.translateNode("head", 0, 0, 0, "cm")
gvxr.setColor("head", 0, 0, 0.5, 0.01)
gvxr.setHU("head", 300)
