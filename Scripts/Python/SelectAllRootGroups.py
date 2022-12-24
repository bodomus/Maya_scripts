from maya import cmds

def find_root_groups():
    """Find all root level transforms in scene that have immediate nurbs or polygon children."""

    # Root groups result
    result_transforms = set()

    # Simple function to check if transform has a nurbs or mesh shape
    has_shape= lambda n, t: cmds.listRelatives(n, type=t, shapes=True) or []

    # Start searching!
    for root_transform in cmds.ls(assemblies=True):
        for transform in cmds.listRelatives(root_transform, type="transform", children=True) or []:
            if has_shape(transform, "nurbsSurface") or has_shape(transform, "mesh"):
                result_transforms.add(root_transform)

    return list(result_transforms)

# Find and select
root_groups = find_root_groups()
cmds.select(root_groups, replace=True)

###################################
def find_root_groups():
    """Find all root level transforms in scene that have immediate nurbs or polygon children."""

    scale = cmds.promptDialog(
                title='Scale objects',
                message='Input scale value:',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')
    # Root groups result
    result_transforms = set()

    # Simple function to check if transform has a nurbs or mesh shape
    has_shape= lambda n, t: cmds.listRelatives(n, type=t, shapes=True) or []

    # Start searching!
    for root_transform in cmds.ls(assemblies=True):
        for transform in cmds.listRelatives(root_transform, type="transform", children=True) or []:
            if has_shape(transform, "nurbsSurface") or has_shape(transform, "mesh"):
                result_transforms.add(root_transform)

    return list(result_transforms)

# Find and select
root_groups = find_root_groups()
mySel = cmds.select(root_groups, replace=True)
####### rename group objects
for i, obj in enumerate(root_groups): # Loop over selection, one by one.
    newName = "{}_{}_grp".format(obj, i) # Build the new name.
    cmds.rename(obj, newName) # Finally rename the object.


###################    

