bl_info = {
    'name': 'Custom Objects',
    'category': 'Object',
    'author': 'Spectral Vectors',
    'version': (0, 1, 0),
    'blender': (2, 80, 0),
    'location': 'Toolbar & Add Menu',
    'description': 'Adds Meshes, Lights and Probes Scaled to 0.01 Unit Scale'
}

import bpy
from bpy.props import (
    StringProperty,
    FloatProperty,
    FloatVectorProperty,
    IntProperty,
)
from bpy.types import (
    Operator,
    Panel
)

###################
# Addon Preferences
###################

class CustomObjectsPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    #########
    # Display
    #########

    ShowInViewport: bpy.props.BoolProperty(
        name='Show in 3D Viewport',
        default=True
    )

    ################
    # Empty & Camera
    ################

    EmptyRadiusPreference: bpy.props.FloatProperty(
        name="Empty Radius",
        description="What size should the Empty be?",
        default=20,
        min=1,
        max=200
    )

    CameraScalePreference: bpy.props.FloatProperty(
        name="Camera Scale",
        description="How large the camera appears in the Viewport",
        default=50,
        min=5,
        max=200
    )

    ########
    # Meshes
    ########

    CubeSizePreference: bpy.props.FloatProperty(
        name="Cube Size",
        description="What size should the Cube be?",
        default=50,
        min=5,
        max=200
    )

    UVSphereRadiusPreference: bpy.props.FloatProperty(
        name="UV Sphere Radius",
        description="What size should the UV Sphere be?",
        default=30,
        min=5,
        max=200
    )

    IcoSphereRadiusPreference: bpy.props.FloatProperty(
        name="Ico Sphere Radius",
        description="What size should the Ico Sphere be?",
        default=30,
        min=5,
        max=200
    )

    CylinderRadiusPreference: bpy.props.FloatProperty(
        name="Cylinder Radius",
        description="What size should the Ico Sphere be?",
        default=20,
        min=5,
        max=200
    )

    ConeRadiusPreference: bpy.props.FloatProperty(
        name="Cone Radius",
        description="What size should the Cone be?",
        default=30,
        min=5,
        max=200
    )

    TorusRadiusPreference: bpy.props.FloatProperty(
        name="Torus Radius",
        description="What size should the Torus be?",
        default=20,
        min=5,
        max=200
    )

    MonkeySizePreference: bpy.props.FloatProperty(
        name="Monkey Size",
        description="What size should Suzanne be?",
        default=50,
        min=5,
        max=200
    )

    PlaneSizePreference: bpy.props.FloatProperty(
        name="Plane Size",
        description="What size should the Plane be?",
        default=100,
        min=20,
        max=1000
    )

    FloorPlaneSizePreference: bpy.props.FloatProperty(
        name="Floor Plane Size",
        description="What size should the Floor Plane be?",
        default=10000,
        min=2000,
        max=100000
    )

    CircleRadiusPreference: bpy.props.FloatProperty(
        name='Circle Size',
        description="What size should the Circle be?",
        default=50,
        min=5,
        max=200
    )

    ########
    # Lights
    ########

    PointLightEnergyPreference: bpy.props.FloatProperty(
        name='Point Light Energy',
        description="How bright should the Point Light be?",
        default=1000000,
        min=10000,
        max=100000000
    )

    DirectionalLightEnergyPreference: bpy.props.FloatProperty(
        name='Directional Light Energy',
        description="How bright should the Directional Light be?",
        default=1000000,
        min=10000,
        max=100000000
    )

    SpotLightEnergyPreference: bpy.props.FloatProperty(
        name='Spot Light Energy',
        description="How bright should the Spot Light be?",
        default=1000000,
        min=10000,
        max=100000000
    )

    SunLightEnergyPreference: bpy.props.FloatProperty(
        name='Sun Light Energy',
        description="How bright should the Sun Light be?",
        default=5,
        min=10,
        max=1
    )

    ##############
    # Light Probes
    ##############

    CubemapRadiusPreference: bpy.props.FloatProperty(
        name="Cubemap Radius",
        description="What size should the Cubemap be?",
        default=100,
        min=5,
        max=2000
    )

    PlanarRadiusPreference: bpy.props.FloatProperty(
        name="Planar Reflection Capture Radius",
        description="What size should the Planar be?",
        default=100,
        min=5,
        max=2000
    )

    GridRadiusPreference: bpy.props.FloatProperty(
        name="Grid Reflection Capture Radius",
        description="What size should the Grid be?",
        default=100,
        min=5,
        max=2000
    )

    ########
    # Extras
    ########

    MirrorCubeSizePreference: bpy.props.FloatProperty(
        name="Mirror Cube Size",
        description="What size should the Mirrored Cube be?",
        default=50,
        min=5,
        max=200
    )

    MirrorSphereRadiusPreference: bpy.props.FloatProperty(
        name="Mirror Sphere Radius",
        description="What size should the Mirrored Sphere be?",
        default=30,
        min=5,
        max=200
    )

    HardSurfacePlaneSizePreference: bpy.props.FloatProperty(
        name="Hard Surface Plane Size",
        description="What size should the Hard Surface Plane be?",
        default=100,
        min=20,
        max=1000
    )

    HardSurfaceCubeSizePreference: bpy.props.FloatProperty(
        name="Hard Surface Cube Size",
        description="What size should the Hard Surface Cube be?",
        default=50,
        min=20,
        max=1000
    )

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        column = box.column()
        row = column.row()
        row.label(text='Display', icon='WORKSPACE')
        row = column.row()
        row.prop(self, 'ShowInViewport')

        box = layout.box()
        column = box.column()
        row = column.row()
        row.label(text='Empty & Camera', icon='EMPTY_DATA')
        row = column.row()
        row.prop(self, 'EmptyRadiusPreference')
        row = column.row()
        row.prop(self, 'CameraScalePreference')
        
        box = layout.box()
        column = box.column()
        row = column.row()
        row.label(text='Meshes', icon='MESH_CUBE')
        row = column.row()
        row.prop(self, 'CubeSizePreference')
        row = column.row()
        row.prop(self, 'UVSphereRadiusPreference')
        row = column.row()
        row.prop(self, 'IcoSphereRadiusPreference')
        row = column.row()
        row.prop(self, 'CylinderRadiusPreference')
        row = column.row()
        row.prop(self, 'ConeRadiusPreference')
        row = column.row()
        row.prop(self, 'TorusRadiusPreference')
        row = column.row()
        row.prop(self, 'MonkeySizePreference')
        row = column.row()
        row.prop(self, 'PlaneSizePreference')
        row = column.row()
        row.prop(self, 'FloorPlaneSizePreference')
        row = column.row()
        row.prop(self, 'CircleRadiusPreference')

        box = layout.box()
        column = box.column()
        row = column.row()
        row.label(text='Lights', icon='LIGHT_POINT')
        row = column.row()
        row.prop(self, 'PointLightEnergyPreference')
        row = column.row()
        row.prop(self, 'DirectionalLightEnergyPreference')
        row = column.row()
        row.prop(self, 'SpotLightEnergyPreference')
        row = column.row()
        row.prop(self, 'SunLightEnergyPreference')

        box = layout.box()
        column = box.column()
        row = column.row()
        row.label(text='Light Probes', icon='LIGHTPROBE_CUBEMAP')
        row = column.row()
        row.prop(self, 'CubemapRadiusPreference')
        row = column.row()
        row.prop(self, 'PlanarRadiusPreference')
        row = column.row()
        row.prop(self, 'GridRadiusPreference')

        box = layout.box()
        column = box.column()
        row = column.row()
        row.label(text='Extras', icon='OUTLINER_OB_ARMATURE')
        row = column.row()
        row.prop(self, 'MirrorCubeSizePreference')
        row = column.row()
        row.prop(self, 'MirrorSphereRadiusPreference')
        row = column.row()
        row.prop(self, 'HardSurfacePlaneSizePreference')
        row = column.row()
        row.prop(self, 'HardSurfaceCubeSizePreference')

######################
# Add Object Operators
######################

##################
# Empty and Camera
##################

# Add Empty #
class BLUI_OT_add_empty(Operator):
    bl_idname = "blui.add_empty"
    bl_label = "Add Empty"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.object.empty_add(radius=addon_prefs.EmptyRadiusPreference)
        return {'FINISHED'}


# Add Camera w Distant Clip End #
class BLUI_OT_add_long_camera(Operator):
    bl_idname = "blui.add_long_camera"
    bl_label = "Camera - Far Clip End"
    bl_description = "Adds a Camera with the Clip End set to 100000"
    bl_options = {'REGISTER', 'UNDO'}
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.object.camera_add(location=(00, -200, 100), rotation=(1, 0, 0))
        bpy.context.object.data.clip_end = 10000000
        bpy.context.object.scale[0] = addon_prefs.CameraScalePreference
        bpy.context.object.scale[1] = addon_prefs.CameraScalePreference
        bpy.context.object.scale[2] = addon_prefs.CameraScalePreference
        return {'FINISHED'}

########
# Meshes
########

# Add Cube #
class BLUI_OT_add_cube(Operator):
    bl_idname = "blui.add_cube"
    bl_label = "Add Cube"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_cube_add(size=addon_prefs.CubeSizePreference, location=(0,0,addon_prefs.CubeSizePreference/2))
        return {'FINISHED'}


# Add UV Sphere #
class BLUI_OT_add_uv_sphere(Operator):
    bl_idname = "blui.add_uv_sphere"
    bl_label = "Add UV Sphere"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_uv_sphere_add(radius=addon_prefs.UVSphereRadiusPreference, location=(0,0,addon_prefs.UVSphereRadiusPreference))
        return {'FINISHED'}


# Add Ico Sphere #
class BLUI_OT_add_ico_sphere(Operator):
    bl_idname = "blui.add_ico_sphere"
    bl_label = "Add Ico Sphere"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_ico_sphere_add(radius=addon_prefs.IcoSphereRadiusPreference, location=(0,0,addon_prefs.IcoSphereRadiusPreference))
        return {'FINISHED'}


# Add UV Cylinder #
class BLUI_OT_add_cylinder(Operator):
    bl_idname = "blui.add_cylinder"
    bl_label = "Add Cylinder"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_cylinder_add(radius=addon_prefs.CylinderRadiusPreference, depth=addon_prefs.CylinderRadiusPreference*2.5, location=(0,0,addon_prefs.CylinderRadiusPreference*2.5/2))
        return {'FINISHED'}


# Add Cone #
class BLUI_OT_add_cone(Operator):
    bl_idname = "blui.add_cone"
    bl_label = "Add Cone"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_cone_add(radius1=addon_prefs.ConeRadiusPreference, radius2=0, depth=addon_prefs.ConeRadiusPreference*2, location=(0,0,addon_prefs.ConeRadiusPreference))
        return {'FINISHED'}


# Add Torus #
class BLUI_OT_add_torus(Operator):
    bl_idname = "blui.add_torus"
    bl_label = "Add Torus"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_torus_add(major_radius=addon_prefs.TorusRadiusPreference*2.5, minor_radius=addon_prefs.TorusRadiusPreference, location=(0,0,addon_prefs.TorusRadiusPreference))
        return {'FINISHED'}


# Add Monkey #
class BLUI_OT_add_monkey(Operator):
    bl_idname = "blui.add_monkey"
    bl_label = "Add Monkey"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_monkey_add(size=addon_prefs.MonkeySizePreference, location=(0,0,addon_prefs.MonkeySizePreference/2))
        return {'FINISHED'}


# Add Plane #
class BLUI_OT_add_plane(Operator):
    bl_idname = "blui.add_plane"
    bl_label = "Add Plane"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_plane_add(size=addon_prefs.PlaneSizePreference)
        return {'FINISHED'}

# Add Floor Plane #
class BLUI_OT_add_floor_plane(Operator):
    bl_idname = "blui.add_floor_plane"
    bl_label = "Add Floor Plane"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_plane_add(size=addon_prefs.FloorPlaneSizePreference)
        return {'FINISHED'}


# Add Circle #
class BLUI_OT_add_circle(Operator):
    bl_idname = "blui.add_circle"
    bl_label = "Add Circle"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_circle_add(radius=addon_prefs.CircleRadiusPreference)
        return {'FINISHED'}

########
# Lights
########

# Add a Point Light #
class BLUI_OT_add_point_light(Operator):
    bl_idname = "blui.add_point_light"
    bl_label = "Add Point Light"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.object.light_add(type='POINT', location=(0, 0, 300))
        bpy.context.object.data.energy = addon_prefs.PointLightEnergyPreference
        return {'FINISHED'}


# Add a Directional Light #
class BLUI_OT_add_directional_light(Operator):
    bl_idname = "blui.add_directional_light"
    bl_label = "Add Directional Light"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.object.light_add(type='AREA', location=(0, 0, 300))
        bpy.context.object.data.energy = addon_prefs.DirectionalLightEnergyPreference
        bpy.context.object.scale[0] = 200
        bpy.context.object.scale[1] = 200
        bpy.context.object.scale[2] = 200
        return {'FINISHED'}


# Add a Spot Light #
class BLUI_OT_add_spot_light(Operator):
    bl_idname = "blui.add_spot_light"
    bl_label = "Add Spot Light"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.object.light_add(type='SPOT', location=(0, 0, 300))
        bpy.context.object.data.energy = addon_prefs.SpotLightEnergyPreference
        bpy.context.object.scale[0] = 50
        bpy.context.object.scale[1] = 50
        bpy.context.object.scale[2] = 50
        return {'FINISHED'}


# Add a Sun Light #
class BLUI_OT_add_sun_light(Operator):
    bl_idname = "blui.add_sun_light"
    bl_label = "Add Sun Light"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.object.light_add(type='SUN', location=(0, 0, 300))
        bpy.context.object.data.energy = addon_prefs.SunLightEnergyPreference
        bpy.context.object.scale[0] = 50
        bpy.context.object.scale[1] = 50
        bpy.context.object.scale[2] = 50
        return {'FINISHED'}

###################################
# Lightprobes / Reflection Captures
###################################

# Add a Cubemap #
class BLUI_OT_add_cubemap(Operator):
    bl_idname = "blui.add_cubemap"
    bl_label = "Add Cubemap"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.object.lightprobe_add(type='CUBEMAP', radius=addon_prefs.CubemapRadiusPreference)
        return {'FINISHED'}


# Add a Planar Reflection Capture #
class BLUI_OT_add_planar(Operator):
    bl_idname = "blui.add_planar"
    bl_label = "Add Planar"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.object.lightprobe_add(type='PLANAR', radius=addon_prefs.PlanarRadiusPreference)
        return {'FINISHED'}


# Add a Grid Reflection Capture #
class BLUI_OT_add_grid(Operator):
    bl_idname = "blui.add_grid"
    bl_label = "Add Grid"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.object.lightprobe_add(type='GRID', radius=addon_prefs.GridRadiusPreference)
        return {'FINISHED'}

########
# Extras
########

# Add an Unreal Mannequin Skeleton #
class BLUI_OT_add_skeleton(Operator):
    bl_idname = "blui.add_skeleton"
    bl_label = "Add Unreal compatible skeleton"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        # Add a small cylinder, name it 'boneshape', rotate, then apply the rotation
        # This is the mesh that will stand in for the actual bones

        bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=0.7)
        boneshape = bpy.context.object
        boneshape.name = "boneshape"
        boneshape.delta_rotation_euler = (0,1.5708,0)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        # Add an armature, then begin adding bones

        bpy.ops.object.armature_add(radius=20, enter_editmode=True)
        root = bpy.context.object
        root.name = "root"
        edit_bones = root.data.edit_bones

        # Spine - parent
        pelvis = edit_bones.new('pelvis')
        pelvis.head = (0, 1.0562, 96.7506)
        pelvis.tail = (0, 10.7616, 96.7861)
        pelvis.roll = -1.5708

        spine_01 = edit_bones.new('spine_01')
        spine_01.head = (0, 0.1652, 107.556)
        spine_01.tail = (0, 19.2608, 110.024)
        spine_01.roll = -1.5708
        spine_01.parent = pelvis

        spine_02 = edit_bones.new('spine_02')
        spine_02.head = (0, 1.516, 126.763)
        spine_02.tail = (0, 14.8383, 125.198)
        spine_02.roll = -1.5708
        spine_02.parent = spine_01

        spine_03 = edit_bones.new('spine_03')
        spine_03.head = (0, 3.4979, 140.03)
        spine_03.tail = (0, 17.3384, 137.719)
        spine_03.roll = -1.5708
        spine_03.parent = spine_02

        # Left Arm - child of 'spine_03'
        clavicle_l = edit_bones.new('clavicle_l')
        clavicle_l.head = (3.782, 2.7604, 152.201)
        clavicle_l.tail = (-3.2703, 16.8823, 152.201)
        clavicle_l.roll = 0.169297
        clavicle_l.parent = spine_03

        upperarm_l = edit_bones.new('upperarm_l')
        upperarm_l.head = (17.7002, 9.711, 149.53)
        upperarm_l.tail = (16.6509, 25.0845, 150.106)
        upperarm_l.roll = 0.872665
        upperarm_l.parent = clavicle_l

        lowerarm_l = edit_bones.new('lowerarm_l')
        lowerarm_l.head = (37.2646, 11.9106, 126.445)
        lowerarm_l.tail = (41.8992, 30.1114, 118.26)
        lowerarm_l.roll = 0.698132
        lowerarm_l.parent = upperarm_l

        # Left Hand - child of 'lowerarm_l'
        hand_l = edit_bones.new('hand_l')
        hand_l.head = (56.646, 0.3352, 111.68)
        hand_l.tail = (50.0167, 1.0778, 103.198)
        hand_l.roll = 1.11701
        hand_l.parent = lowerarm_l

        # Left Index - child of 'hand_l'
        index_01_l = edit_bones.new('index_01_l')
        index_01_l.head = (63.0423, -6.7664, 103.815)
        index_01_l.tail = (59.9164, -4.7108, 101.721)
        index_01_l.roll = 1.3439
        index_01_l.parent = hand_l

        index_02_l = edit_bones.new('index_02_l')
        index_02_l.head = (64.6721, -8.0948, 100.078)
        index_02_l.tail = (62.0295, -6.2201, 99.0685)
        index_02_l.roll = 1.44862
        index_02_l.parent = index_01_l

        index_03_l = edit_bones.new('index_03_l')
        index_03_l.head = (65.4362 , -8.7624, 96.8398)
        index_03_l.tail = (62.9962 , -6.9696, 95.3068)
        index_03_l.roll = 1.36136
        index_03_l.parent = index_02_l

        # Left Middle - child of 'hand_l'
        middle_01_l = edit_bones.new('middle_01_l')
        middle_01_l.head = (64.49, -4.4795, 103.481)
        middle_01_l.tail = (60.6792, -3.2446, 101.139)
        middle_01_l.roll = 1.309
        middle_01_l.parent = hand_l

        middle_02_l = edit_bones.new('middle_02_l')
        middle_02_l.head = (66.5308, -5.7249, 99.5043)
        middle_02_l.tail = (63.2161, -4.6874, 98.3863)
        middle_02_l.roll = 1.48353
        middle_02_l.parent = middle_01_l

        middle_03_l = edit_bones.new('middle_03_l')
        middle_03_l.head = (67.435, -6.5422, 96.065)
        middle_03_l.tail = (64.4945, -5.7117, 94.0706)
        middle_03_l.roll = 1.20428
        middle_03_l.parent = middle_02_l

        # Left Ring - child of 'hand_l'
        ring_01_l = edit_bones.new('ring_01_l')
        ring_01_l.head = (64.5756, -2.0826, 103.039)
        ring_01_l.tail = (60.6571, -2.0405, 100.973)
        ring_01_l.roll = 1.29154
        ring_01_l.parent = hand_l

        ring_02_l = edit_bones.new('ring_02_l')
        ring_02_l.head = (66.5923, -2.9755, 99.197)
        ring_02_l.tail = (63.2372, -2.7639, 98.3107)
        ring_02_l.roll = 1.48353
        ring_02_l.parent = ring_01_l

        ring_03_l = edit_bones.new('ring_03_l')
        ring_03_l.head = (67.4341, -3.5502, 95.8732)
        ring_03_l.tail = (64.349, -3.4936, 94.2714)
        ring_03_l.roll = 1.32645
        ring_03_l.parent = ring_02_l

        # Left Pinky - child of 'hand_l'
        pinky_01_l = edit_bones.new('pinky_01_l')
        pinky_01_l.head = (64.025, 0.1589, 103.017)
        pinky_01_l.tail = (61.0139, -0.2218, 101.136)
        pinky_01_l.roll = 1.09956
        pinky_01_l.parent = hand_l

        pinky_02_l = edit_bones.new('pinky_02_l')
        pinky_02_l.head = (65.9371, -0.1266, 100.015)
        pinky_02_l.tail = (63.1542, -0.3373, 98.9544)
        pinky_02_l.roll = 1.29154
        pinky_02_l.parent = pinky_01_l

        pinky_03_l = edit_bones.new('pinky_03_l')
        pinky_03_l.head = (67.0124 , -0.3546 , 97.2392 )
        pinky_03_l.tail = (64.2102 , -0.5383 , 96.2253 )
        pinky_03_l.roll = 1.36136
        pinky_03_l.parent = pinky_02_l

        # Left Thumb - child of 'hand_l'
        thumb_01_l = edit_bones.new('thumb_01_l')
        thumb_01_l.head = (57.478 , -3.8766 , 107.639 )
        thumb_01_l.tail = (59.7358 , -2.0499 , 105.082 )
        thumb_01_l.roll = 1.20428
        thumb_01_l.parent = hand_l

        thumb_02_l = edit_bones.new('thumb_02_l')
        thumb_02_l.head = (57.6075 , -7.0769 , 105.467 )
        thumb_02_l.tail = (59.9538 , -4.3965 , 103.515 )
        thumb_02_l.roll = 1.309
        thumb_02_l.parent = thumb_01_l

        thumb_03_l = edit_bones.new('thumb_03_l')
        thumb_03_l.head = (57.7842 , -9.5661 , 102.262 )
        thumb_03_l.tail = (60.2511 , -7.5595 , 99.7346 )
        thumb_03_l.roll = 1.36136
        thumb_03_l.parent = thumb_02_l

        # Right Arm - child of 'spine_03'
        clavicle_r = edit_bones.new('clavicle_r')
        clavicle_r.head = (-3.782, 2.7604, 152.201)
        clavicle_r.tail = (-10.8342, -11.3614, 152.201)
        clavicle_r.roll = -2.96706
        clavicle_r.parent = spine_03

        upperarm_r = edit_bones.new('upperarm_r')
        upperarm_r.head = (-17.7002, 9.711, 149.53)
        upperarm_r.tail = (-18.7495, -5.6625, 148.955)
        upperarm_r.roll = 3.00197
        upperarm_r.parent = clavicle_r

        lowerarm_r = edit_bones.new('lowerarm_r')
        lowerarm_r.head = (-37.2646, 11.9106, 126.445)
        lowerarm_r.tail = (-32.6301, -6.2902, 134.631)
        lowerarm_r.roll = 1.72788
        lowerarm_r.parent = upperarm_r

        # Right Hand - child of 'lowerarm_r'
        hand_r = edit_bones.new('hand_r')
        hand_r.head = (-56.646, 0.3352, 111.68)
        hand_r.tail = (-63.2754, -0.4075, 120.161)
        hand_r.roll = -0.20944
        hand_r.parent = lowerarm_r

        # Right Index - child of 'hand_r'
        index_01_r = edit_bones.new('index_01_r')
        index_01_r.head = (-63.0421, -6.76643, 103.815)
        index_01_r.tail = (-66.1682, -8.82212, 105.909)
        index_01_r.roll = -0.619672
        index_01_r.parent = hand_r

        index_02_r = edit_bones.new('index_02_r')
        index_02_r.head = (-64.6721, -8.09492, 100.078)
        index_02_r.tail = (-67.3147, -9.96964, 101.088)
        index_02_r.roll = -0.967554
        index_02_r.parent = index_01_r

        index_03_r = edit_bones.new('index_03_r')
        index_03_r.head = (-65.4362, -8.76252, 96.8397)
        index_03_r.tail = (-67.8762, -10.5553, 98.3727)
        index_03_r.roll = -0.649723
        index_03_r.parent = index_02_r

        # Right Middle - child of 'hand_r'
        middle_01_r = edit_bones.new('middle_01_r')
        middle_01_r.head = (-64.49, -4.47954, 103.481)
        middle_01_r.tail = (-68.3009, -5.71443, 105.824)
        middle_01_r.roll = -0.737538
        middle_01_r.parent = hand_r

        middle_02_r = edit_bones.new('middle_02_r')
        middle_02_r.head = (-66.5307, -5.72502, 99.5041)
        middle_02_r.tail = (-69.8456, -6.76257, 100.622)
        middle_02_r.roll = -1.00971
        middle_02_r.parent = middle_01_r

        middle_03_r = edit_bones.new('middle_03_r')
        middle_03_r.head = (-67.4349, -6.5423, 96.0648)
        middle_03_r.tail = (-70.3755, -7.37286, 98.0592)
        middle_03_r.roll = -0.747729
        middle_03_r.parent = middle_02_r

        # Right Ring - child of 'hand_r'
        ring_01_r = edit_bones.new('ring_01_r')
        ring_01_r.head = (-64.5756, -2.08277, 103.039)
        ring_01_r.tail = (-68.4938, -2.12491, 105.105)
        ring_01_r.roll = -0.882559
        ring_01_r.parent = hand_r

        ring_02_r = edit_bones.new('ring_02_r')
        ring_02_r.head = (-66.5922, -2.97553, 99.1971)
        ring_02_r.tail = (-69.9473, -3.18709, 100.083)
        ring_02_r.roll = -1.14615
        ring_02_r.parent = ring_01_r

        ring_03_r = edit_bones.new('ring_03_r')
        ring_03_r.head = (-67.4341, -3.55024, 95.8733)
        ring_03_r.tail = (-70.5193, -3.60684, 97.4751)
        ring_03_r.roll = -0.86413
        ring_03_r.parent = ring_02_r

        # Right Pinky - child of 'hand_r'
        pinky_01_r = edit_bones.new('pinky_01_r')
        pinky_01_r.head = (-64.0249, 0.158811, 103.017)
        pinky_01_r.tail = (-67.0361, 0.539548, 104.899)
        pinky_01_r.roll = -0.931809
        pinky_01_r.parent = hand_r

        pinky_02_r = edit_bones.new('pinky_02_r')
        pinky_02_r.head = (-65.937, -0.126716, 100.015)
        pinky_02_r.tail = (-68.7197, 0.084021, 101.076)
        pinky_02_r.roll = -1.13001
        pinky_02_r.parent = pinky_01_r

        pinky_03_r = edit_bones.new('pinky_03_r')
        pinky_03_r.head = (-67.0125, -0.354654, 97.2393)
        pinky_03_r.tail = (-69.8145, -0.171015, 98.2531)
        pinky_03_r.roll = -1.07827
        pinky_03_r.parent = pinky_02_r

        # Right Thumb - child of 'hand_r'
        thumb_01_r = edit_bones.new('thumb_01_r')
        thumb_01_r.head = (-57.4781, -3.87677, 107.639)
        thumb_01_r.tail = (-55.2203, -5.70348, 110.196)
        thumb_01_r.roll = 2.64777
        thumb_01_r.parent = hand_r

        thumb_02_r = edit_bones.new('thumb_02_r')
        thumb_02_r.head = (-57.6074, -7.07692, 105.467)
        thumb_02_r.tail = (-55.2611, -9.75726, 107.42)
        thumb_02_r.roll = 3.06475
        thumb_02_r.parent = thumb_01_r

        thumb_03_r = edit_bones.new('thumb_03_r')
        thumb_03_r.head = (-57.7841, -9.56623, 102.262)
        thumb_03_r.tail = (-55.3172, -11.5729, 104.79)
        thumb_03_r.roll = 2.90462
        thumb_03_r.parent = thumb_02_r

        # Neck - child of spine_03
        neck_01 = edit_bones.new('neck_01')
        neck_01.head = (0.000007, 5.87469, 156.421)
        neck_01.tail = (0.000007, 14.8884, 158.673)
        neck_01.roll = -1.5708
        neck_01.parent = spine_03

        head = edit_bones.new('head')
        head.head = (0.000008, 3.97763, 165.516)
        head.tail = (0.000008, 13.2659, 165.302)
        head.roll = -1.5708
        head.parent = neck_01

        # Left Leg - child of pelvis
        thigh_l = edit_bones.new('thigh_l')
        thigh_l.head = (9.00581, 0.530028, 95.2999)
        thigh_l.tail = (4.22747, 32.506, 95.673)
        thigh_l.roll = -1.69577
        thigh_l.parent = pelvis

        calf_l = edit_bones.new('calf_l')
        calf_l.head = (14.2178, 1.80179, 53.0672)
        calf_l.tail = (12.2905, 31.7257, 57.6673)
        calf_l.roll = -1.64697
        calf_l.parent = thigh_l

        foot_l = edit_bones.new('foot_l')
        foot_l.head = (17.0763, 8.07371, 13.4659)
        foot_l.tail = (16.1807, 27.6506, 13.7035)
        foot_l.roll = -1.58592
        foot_l.parent = calf_l

        ball_l = edit_bones.new('ball_l')
        ball_l.head = (17.9087, -8.35531, 2.81181)
        ball_l.tail = (17.6464, -9.24983, 22.3885)
        ball_l.roll = -1.53847
        ball_l.parent = foot_l

        # Right Leg - child of pelvis
        thigh_r = edit_bones.new('thigh_r')
        thigh_r.head = (-9.0058, 0.530023, 95.3)
        thigh_r.tail = (-13.7842, -31.446, 94.9268)
        thigh_r.roll = 1.28994
        thigh_r.parent = pelvis

        calf_r = edit_bones.new('calf_r')
        calf_r.head = (-14.2179, 1.80179, 53.0672)
        calf_r.tail = (-16.1452, -28.1223, 48.467)
        calf_r.roll = -0.853457
        calf_r.parent = thigh_r

        foot_r = edit_bones.new('foot_r')
        foot_r.head = (-17.0763, 8.07373, 13.4657)
        foot_r.tail = (-17.9718, -11.5031, 13.2281)
        foot_r.roll = 1.03695
        foot_r.parent = calf_r

        ball_r = edit_bones.new('ball_r')
        ball_r.head = (-17.9087, -8.35523, 2.81168)
        ball_r.tail = (-18.1711, -7.46071, -16.7649)
        ball_r.roll = -1.51168
        ball_r.parent = foot_r

        # Cleanup

        # This removes the bone automatically added with the armature, named 'Bone'

        for bone in edit_bones:
            if bone.name == "Bone": 
                edit_bones.remove(bone)

        # Now we switch to Object mode to assign a custom mesh to our bones

        bpy.ops.object.mode_set(mode='OBJECT')

        # Looping through all the bones, and setting them all to use our 'boneshape' mesh

        for bone in root.pose.bones:
            bone.custom_shape = boneshape

        # Finally, we select the original 'boneshape' mesh and delete it, leaving only the skeleton

        ob = bpy.context.scene.objects["boneshape"]
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = ob
        ob.select_set(True)
        bpy.ops.object.delete()
        return {'FINISHED'}

# Add Mirror Cube #
class BLUI_OT_add_mirror_cube(Operator):
    bl_idname = "blui.add_mirror_cube"
    bl_label = "Add Cube w Mirror Modifier"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_cube_add(size=addon_prefs.MirrorCubeSizePreference, location=(0, 0, addon_prefs.MirrorCubeSizePreference/2))
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(0, 0, 0), plane_no=(1, 0, 0), xstart=0, xend=100, ystart=0, yend=100, clear_outer=False, clear_inner=True)
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_clip = True
        return {'FINISHED'}

# Add Mirror Sphere #
class BLUI_OT_add_mirror_sphere(Operator):
    bl_idname = "blui.add_mirror_sphere"
    bl_label = "Add UV Sphere w Mirror Modifier"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_uv_sphere_add(radius=addon_prefs.MirrorSphereRadiusPreference, location=(0, 0, addon_prefs.MirrorSphereRadiusPreference))
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(0, 0, 0), plane_no=(1, 0, 0), xstart=0, xend=100, ystart=0, yend=100, clear_outer=False, clear_inner=True)
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_clip = True
        return {'FINISHED'}

# Add Hard Surface Plane #
class BLUI_OT_add_hs_plane(Operator):
    bl_idname = "blui.add_hs_plane"
    bl_label = "Add Hard Surface Plane"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        bpy.ops.mesh.primitive_plane_add(size=addon_prefs.HardSurfacePlaneSizePreference)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(0, 0, 0), plane_no=(1, 0, 0), xstart=0, xend=100, ystart=0, yend=100, clear_outer=False, clear_inner=True)
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_clip = True
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].thickness = 2
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].uv_smooth = 'NONE'
        bpy.context.object.modifiers["Subdivision"].subdivision_type = 'SIMPLE'
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision.001"].uv_smooth = 'NONE'
        bpy.context.object.modifiers["Subdivision.001"].levels = 2
        bpy.ops.object.shade_smooth()
        return {'FINISHED'}

# Add Hard Surface Cube #
class BLUI_OT_add_hs_cube(Operator):
    bl_idname = "blui.add_hs_cube"
    bl_label = "Add Hard Surface Cube"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences
        
        bpy.ops.mesh.primitive_cube_add(size=addon_prefs.HardSurfaceCubeSizePreference, location=(0, 0, addon_prefs.HardSurfaceCubeSizePreference/2))
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.bisect(plane_co=(0, 0, 0), plane_no=(1, 0, 0), xstart=0, xend=100, ystart=0, yend=100, clear_outer=False, clear_inner=True)
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_clip = True
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].thickness = 2
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].uv_smooth = 'NONE'
        bpy.context.object.modifiers["Subdivision"].subdivision_type = 'SIMPLE'
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision.001"].uv_smooth = 'NONE'
        bpy.context.object.modifiers["Subdivision.001"].levels = 2
        bpy.ops.object.shade_smooth()
        return {'FINISHED'}

#################
# Panel Operators 
#################

# Create an integer to track which Panel to display
bpy.types.Scene.PanelSelect = bpy.props.IntProperty(
    name="Panel Select",
    default=0,
    min=0,
    max=4
)
bpy.types.Scene.PanelSelect = 0

###########################
# Panel Selection Operators
###########################

# Show the Basic Panel #
class BLUI_OT_show_basic_panel(Operator):
    bl_idname = "blui.show_basic_panel"
    bl_label = "Shows the Basic Panel Items"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        bpy.types.Scene.PanelSelect = 0
        return {'FINISHED'}


# Show the Lights Panel #
class BLUI_OT_show_lights_panel(Operator):
    bl_idname = "blui.show_lights_panel"
    bl_label = "Shows the Lights Panel Items"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        bpy.types.Scene.PanelSelect = 1
        return {'FINISHED'}


# Show the Camera Panel #
class BLUI_OT_show_camera_panel(Operator):
    bl_idname = "blui.show_camera_panel"
    bl_label = "Shows the Camera Panel Items"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        bpy.types.Scene.PanelSelect = 2
        return {'FINISHED'}


# Show the Visual Effects Panel #
class BLUI_OT_show_vfx_panel(Operator):
    bl_idname = "blui.show_vfx_panel"
    bl_label = "Shows the Visual Effects Panel Items"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        bpy.types.Scene.PanelSelect = 3
        return {'FINISHED'}


# Show the Geometry Panel #
class BLUI_OT_show_geometry_panel(Operator):
    bl_idname = "blui.show_geometry_panel"
    bl_label = "Shows the Geometry Panel Items"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        bpy.types.Scene.PanelSelect = 4
        return {'FINISHED'}


# Show the Extras Panel #
class BLUI_OT_show_extras_panel(Operator):
    bl_idname = "blui.show_extras_panel"
    bl_label = "Shows the Extras Panel Items"
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        bpy.types.Scene.PanelSelect = 5
        return {'FINISHED'}



#####################
# Panel Selection GUI
#####################

# This is the main panel, it can be hidden or shown via Addon Preferences
class BLUI_PT_custom_objects_panel(Panel):
    #bl_parent_id = "BLUI_PT_custom_parent_panel"
    bl_label = "Custom Objects"
    bl_idname = "BLUI_PT_custom_objects_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context_mode = "OBJECT"
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        if addon_prefs.ShowInViewport:
            layout = self.layout
            layout.scale_y = 1.3

    # This splits the layout in half, giving the left side 40%, and the right side 60%
            split = layout.split(factor=0.4)

    # This sets up the first column with all of the category changing buttons
            column = split.column(align=True)
            column.operator("blui.show_basic_panel", text="Basic")
            column.operator("blui.show_lights_panel", text="Lights")
            column.operator("blui.show_camera_panel", text="Cinematic")
            column.operator("blui.show_vfx_panel", text="Visual FX")
            column.operator("blui.show_geometry_panel", text="Geometry")
            column.operator("blui.show_extras_panel", text="Extras")

    # This sets up the second column, and will show different items depending on which category you picked in the first column
    # if 0, show the Basic Panel items
            if bpy.types.Scene.PanelSelect == 0:
                column = split.column(align=True)
                column.operator("blui.add_empty", text="Empty", icon='EMPTY_DATA')
                column.operator("blui.add_skeleton", text="Skeleton", icon='OUTLINER_OB_ARMATURE')
                column.operator("blui.add_point_light", text="Light", icon='LIGHT')
                column.operator("blui.add_cube", text="Cube", icon='MESH_CUBE')
                column.operator("blui.add_uv_sphere",text="Sphere", icon='MESH_UVSPHERE')
                column.operator("blui.add_cylinder",text="Cylinder", icon='MESH_CYLINDER')
                column.operator("blui.add_cone", text="Cone", icon='MESH_CONE')
                column.operator("blui.add_plane", text="Plane", icon='MESH_PLANE')
                column.operator("blui.add_floor_plane", text="Floor Plane", icon='MESH_PLANE')

    # or else, if it's 1, show the Lights Panel
            elif bpy.types.Scene.PanelSelect == 1:
                column = split.column(align=True)
                column.operator("blui.add_directional_light",text="Directional", icon='LIGHT_AREA')
                column.operator("blui.add_point_light",text="Point", icon='LIGHT_POINT')
                column.operator("blui.add_spot_light",text="Spot", icon='LIGHT_SPOT')
                column.operator("blui.add_sun_light", text="Sun", icon='LIGHT_SUN')

    # or else, if it's 2, show the Cinematic Panel
            elif bpy.types.Scene.PanelSelect == 2:
                column = split.column(align=True)
                column.operator("blui.add_long_camera", text="Camera", icon='VIEW_CAMERA')
                
    # or else, if it's 3, show the Visual Effects Panel
            elif bpy.types.Scene.PanelSelect == 3:
                column = split.column(align=True)
                column.operator("blui.add_cubemap", text="Cubemap",icon='LIGHTPROBE_CUBEMAP')
                column.operator("blui.add_planar", text="Planar",icon='LIGHTPROBE_PLANAR')
                column.operator("blui.add_grid", text="Irradiance", icon='LIGHTPROBE_GRID')
                
    # or else, if it's 4, show the Geometry Panel
            elif bpy.types.Scene.PanelSelect == 4:
                column = split.column(align=True)
                column.operator("blui.add_plane", text="Plane", icon='MESH_PLANE')
                column.operator("blui.add_cube", text="Cube", icon='MESH_CUBE')
                column.operator("blui.add_circle", text="Circle",icon='MESH_CIRCLE')
                column.operator("blui.add_uv_sphere",text="UV Sphere", icon='MESH_UVSPHERE')
                column.operator("blui.add_ico_sphere",text="Ico Sphere", icon='MESH_ICOSPHERE')
                column.operator("blui.add_cylinder",text="Cylinder", icon='MESH_CYLINDER')
                column.operator("blui.add_cone", text="Cone", icon='MESH_CONE')
                column.operator("blui.add_torus", text="Torus", icon='MESH_TORUS')
                column.operator("blui.add_monkey", text="Suzanne", icon='MESH_MONKEY')

    # or else, if it's 5, show the Extras Panel
            elif bpy.types.Scene.PanelSelect == 5:
                column = split.column(align=True)
                column.operator("blui.add_skeleton",text="Skeleton",icon='OUTLINER_OB_ARMATURE')
                column.operator("blui.add_mirror_cube",text="Mirror Cube",icon='MESH_CUBE')
                column.operator("blui.add_mirror_sphere",text="Mirror Sphere",icon='MESH_UVSPHERE')
                column.operator("blui.add_hs_plane", text="HardSurf Plane",icon='MESH_PLANE')
                column.operator("blui.add_hs_cube", text="HardSurf Cube",icon='MESH_CUBE')

##############
# Menu version
##############

class BLUI_MT_custom_basic_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_custom_basic_menu'
    bl_label = 'Basic'

    def draw(self, context):
        layout = self.layout
        layout.operator("blui.add_cube", text="Cube", icon='MESH_CUBE')
        layout.operator("blui.add_empty", text="Empty", icon='EMPTY_DATA')
        layout.operator("blui.add_point_light", text="Light", icon='LIGHT')
        layout.operator("blui.add_cube", text="Cube", icon='MESH_CUBE')
        layout.operator("blui.add_uv_sphere",text="Sphere", icon='MESH_UVSPHERE')
        layout.operator("blui.add_cylinder", text="Cylinder", icon='MESH_CYLINDER')


def menu_func(self, context):
    self.layout.menu("BLUI_MT_custom_basic_menu")


class BLUI_MT_custom_lights_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_custom_lights_menu'
    bl_label = 'Lights'

    def draw(self, context):
        layout = self.layout
        layout.operator("blui.add_directional_light", text="Directional", icon='LIGHT_AREA')
        layout.operator("blui.add_point_light", text="Point", icon='LIGHT_POINT')
        layout.operator("blui.add_spot_light", text="Spot", icon='LIGHT_SPOT')
        layout.operator("blui.add_sun_light", text="Sun", icon='LIGHT_SUN')


def menu_func(self, context):
    self.layout.menu("BLUI_MT_custom_lights_menu")


class BLUI_MT_custom_cinematic_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_custom_cinematic_menu'
    bl_label = 'Cinematic'

    def draw(self, context):
        layout = self.layout
        layout.operator("blui.add_long_camera", text="Camera", icon='VIEW_CAMERA')


def menu_func(self, context):
    self.layout.menu("BLUI_MT_custom_cinematic_menu")


class BLUI_MT_custom_vfx_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_custom_vfx_menu'
    bl_label = 'VFX'

    def draw(self, context):
        layout = self.layout
        layout.operator("blui.add_cubemap", text="Cubemap",icon='LIGHTPROBE_CUBEMAP')
        layout.operator("blui.add_planar", text="Planar",icon='LIGHTPROBE_PLANAR')
        layout.operator("blui.add_grid", text="Irradiance",icon='LIGHTPROBE_GRID')

def menu_func(self, context):
    self.layout.menu("BLUI_MT_custom_vfx_menu")


class BLUI_MT_custom_geometry_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_custom_geometry_menu'
    bl_label = 'Geometry'

    def draw(self, context):
        layout = self.layout
        layout.operator("blui.add_plane", text="Plane", icon='MESH_PLANE')
        layout.operator("blui.add_cube", text="Cube", icon='MESH_CUBE')
        layout.operator("blui.add_circle", text="Circle", icon='MESH_CIRCLE')
        layout.operator("blui.add_uv_sphere",text="UV Sphere", icon='MESH_UVSPHERE')
        layout.operator("blui.add_ico_sphere",text="Ico Sphere", icon='MESH_ICOSPHERE')
        layout.operator("blui.add_cylinder", text="Cylinder",icon='MESH_CYLINDER')
        layout.operator("blui.add_cone", text="Cone", icon='MESH_CONE')
        layout.operator("blui.add_torus", text="Torus", icon='MESH_TORUS')
        layout.operator("blui.add_monkey", text="Suzanne", icon='MESH_MONKEY')


def menu_func(self, context):
    self.layout.menu("BLUI_MT_custom_geometry_menu")


class BLUI_MT_custom_parent_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_custom_parent_menu'
    bl_label = 'Custom Objects'

    def draw(self, context):
        layout = self.layout
        layout.menu("BLUI_MT_custom_basic_menu", icon='MESH_CUBE')
        layout.menu("BLUI_MT_custom_lights_menu", icon='LIGHT')
        layout.menu("BLUI_MT_custom_cinematic_menu", icon='VIEW_CAMERA')
        layout.menu("BLUI_MT_custom_vfx_menu", icon='LIGHTPROBE_CUBEMAP')
        layout.menu("BLUI_MT_custom_geometry_menu", icon='MESH_ICOSPHERE')


def menu_func(self, context):
    self.layout.menu("BLUI_MT_custom_parent_menu", icon='EVENT_C')

##########################
# Classes and Registration
##########################

# Adding all the classes to an array to make the register/unregister functions below a little tidier
classes = [
    CustomObjectsPreferences,
    BLUI_PT_custom_objects_panel,
    BLUI_OT_show_basic_panel,
    BLUI_OT_show_lights_panel,
    BLUI_OT_show_camera_panel,
    BLUI_OT_show_vfx_panel,
    BLUI_OT_show_geometry_panel,
    BLUI_OT_show_extras_panel,
    BLUI_OT_add_cube,
    BLUI_OT_add_uv_sphere,
    BLUI_OT_add_ico_sphere,
    BLUI_OT_add_cone,
    BLUI_OT_add_torus,
    BLUI_OT_add_monkey,
    BLUI_OT_add_empty,
    BLUI_OT_add_point_light,
    BLUI_OT_add_directional_light,
    BLUI_OT_add_spot_light,
    BLUI_OT_add_sun_light,
    BLUI_OT_add_cylinder,
    BLUI_OT_add_plane,
    BLUI_OT_add_floor_plane,
    BLUI_OT_add_circle,
    BLUI_OT_add_long_camera,
    BLUI_OT_add_cubemap,
    BLUI_OT_add_planar,
    BLUI_OT_add_grid,
    BLUI_OT_add_skeleton,
    BLUI_OT_add_mirror_cube,
    BLUI_OT_add_mirror_sphere,
    BLUI_OT_add_hs_plane,
    BLUI_OT_add_hs_cube,
    BLUI_MT_custom_parent_menu,
    BLUI_MT_custom_basic_menu,
    BLUI_MT_custom_lights_menu,
    BLUI_MT_custom_cinematic_menu,
    BLUI_MT_custom_vfx_menu,
    BLUI_MT_custom_geometry_menu,
]

# Doing it this way lets me copy all the classes once into the array above, otherwise you're doing it twice, once for register, once for unregister
# Take the items in the array called classes, and for each class that you find, register it with BLender, so that Blender can see and use it

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_add.append(menu_func)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_add.remove(menu_func)

if __name__ == "__main__":
    register()
