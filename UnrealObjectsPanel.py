import bpy
from bpy.props import (
    StringProperty,
    FloatProperty,
    FloatVectorProperty,
    IntProperty,
)
from bpy.types import ( 
    Operator,
    WorkSpaceTool,
    Panel
)

bl_info = {
    'name': 'Unreal Objects',
    'category': 'Object',
    'Author': 'Spectral Vectors',
    'version': (0,0,1),
    'blender': (2, 80, 0),
    'location': 'Toolbar & Add Menu'
    }

############################################Comment Box Operator

class BLUI_OT_comment_box(Operator):
    bl_idname = "blui.comment_box"
    bl_label = "Comment Box"
    bl_description = "Frames around the selected nodes, requests name and color"
    bl_options = {'REGISTER', 'UNDO'}
    bl_space_type = 'NODE_EDITOR'
    bl_context_mode = 'OBJECT'
    bl_property = 'comment_name'
    

    comment_name = bpy.props.StringProperty(
        name = 'Label -',
        default = 'Your Text Here'
    )
    
    comment_color = bpy.props.FloatVectorProperty(
        name = 'Color -',
        default = (0.8, 0.3, 0.3),
        min=0, max=1, step=1, precision=3,
        subtype='COLOR_GAMMA', size=3
    )
  

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'


    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


    def execute(self, context):

        nodes = context.selected_nodes
        selected = []
        for node in nodes:
            if node.select == True:
                selected.append(node)

        bpy.ops.node.add_node(type='NodeFrame')
        frame = context.active_node
        frame.label = self.comment_name
        frame.use_custom_color = True
        frame.color = self.comment_color

        for node in selected:
            node.parent = frame

        return {'FINISHED'}




############################################ Object Adding Operators 


####################### Empty and Camera


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
        bpy.ops.object.empty_add(radius=20)
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
        bpy.ops.object.camera_add(location=(00,-200,100),rotation=(1,0,0))
        bpy.context.object.data.clip_end = 10000000
        bpy.context.object.scale[0] = 50
        bpy.context.object.scale[1] = 50
        bpy.context.object.scale[2] = 50
        return {'FINISHED'}


####################### Meshes


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
       bpy.ops.mesh.primitive_cube_add(size=50)
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
       bpy.ops.mesh.primitive_uv_sphere_add(radius=30)
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
       bpy.ops.mesh.primitive_ico_sphere_add(radius=30)
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
       bpy.ops.mesh.primitive_cylinder_add(radius=20, depth=50)
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
       bpy.ops.mesh.primitive_cone_add(radius1=30, radius2=0, depth=60)
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
       bpy.ops.mesh.primitive_torus_add(major_radius=50, minor_radius=20)
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
       bpy.ops.mesh.primitive_monkey_add(size=50)
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
        bpy.ops.mesh.primitive_plane_add(size=100)
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
       bpy.ops.mesh.primitive_circle_add(radius=50)
       return {'FINISHED'}


#################### Lights


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
        bpy.ops.object.light_add(type='POINT', location=(0,0,300))
        bpy.context.object.data.energy = 1000000
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
        bpy.ops.object.light_add(type='AREA', location=(0,0,300))
        bpy.context.object.data.energy = 1000000
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
        bpy.ops.object.light_add(type='SPOT', location=(0,0,300))
        bpy.context.object.data.energy = 1000000
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
        bpy.ops.object.light_add(type='SUN', location=(0,0,300))
        bpy.context.object.data.energy = 5
        bpy.context.object.scale[0] = 50
        bpy.context.object.scale[1] = 50
        bpy.context.object.scale[2] = 50
        return {'FINISHED'}


####################### Lightprobes / Reflection Captures


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
        bpy.ops.object.lightprobe_add(type='CUBEMAP', radius=100)
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
        bpy.ops.object.lightprobe_add(type='PLANAR', radius=100)
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
        bpy.ops.object.lightprobe_add(type='GRID', radius=100)
        return {'FINISHED'}



######################################## Create an integer to track which Panel to display

bpy.types.Scene.PanelSelect = bpy.props.IntProperty(
    name="Panel Select", 
    default=0, 
    min=0, 
    max=4
    )
bpy.types.Scene.PanelSelect = 0




######################################################### Panel Selection Operators


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



############################################################################## Panel Selection GUI


# This is the Parent Panel, which we hide using bl_options, so only submenus are visible
class BLUI_PT_unreal_parent_panel(Panel):
    bl_label = "Unreal Objects"
    bl_idname = "BLUI_PT_unreal_parent_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context_mode = "OBJECT"
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        layout = self.layout


# This is the first visible panel, appears as "Unreal Objects" with a dropdown arrow, defaults to closed
class BLUI_PT_unreal_objects_panel(Panel):
    bl_parent_id = "BLUI_PT_unreal_parent_panel"
    bl_label = "Unreal Objects"
    bl_idname = "BLUI_PT_unreal_objects_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context_mode = "OBJECT"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.3


#This splits the layout in half, giving the left side 40%, and the right side 60%
        split = layout.split(factor=0.4)


# This sets up the first column with all of the category changing buttons
        column = split.column(align=True)
        column.operator("blui.show_basic_panel", text="Basic")
        column.operator("blui.show_lights_panel", text="Lights")
        column.operator("blui.show_camera_panel", text="Cinematic")
        column.operator("blui.show_vfx_panel", text="Visual FX")
        column.operator("blui.show_geometry_panel", text="Geometry")


# This sets up the second column, and will show different items depending on which category you picked in the first column
# if 0, show the Basic Panel items       
        if bpy.types.Scene.PanelSelect == 0:
            column = split.column(align=True)
            column.operator("blui.add_empty", text="Empty", icon='EMPTY_DATA')
            column.operator("blui.add_point_light", text="Light", icon='LIGHT')
            column.operator("blui.add_cube", text="Cube", icon='MESH_CUBE')
            column.operator("blui.add_uv_sphere", text="Sphere", icon='MESH_UVSPHERE')
            column.operator("blui.add_cylinder", text="Cylinder", icon='MESH_CYLINDER')
            column.operator("blui.add_cone", text="Cone", icon='MESH_CONE')
            column.operator("blui.add_plane", text="Plane", icon='MESH_PLANE')
# or else, if it's 1, show the Lights Panel
        elif bpy.types.Scene.PanelSelect == 1:
            column = split.column(align=True)
            column.operator("blui.add_directional_light", text="Directional", icon='LIGHT_AREA')
            column.operator("blui.add_point_light", text="Point", icon='LIGHT_POINT')
            column.operator("blui.add_spot_light", text="Spot", icon='LIGHT_SPOT')
            column.operator("blui.add_sun_light", text="Sun", icon='LIGHT_SUN')
# or else, if it's 2, show the Cinematic Panel
        elif bpy.types.Scene.PanelSelect == 2:
            column = split.column(align=True)
            column.operator("blui.add_long_camera", text="Camera", icon='VIEW_CAMERA')
# or else, if it's 3, show the Visual Effects Panel
        elif bpy.types.Scene.PanelSelect == 3:
            column = split.column(align=True)
            column.operator("blui.add_cubemap", text="Cubemap", icon='LIGHTPROBE_CUBEMAP')
            column.operator("blui.add_planar", text="Planar", icon='LIGHTPROBE_PLANAR')
            column.operator("blui.add_grid", text="Irradiance", icon='LIGHTPROBE_GRID')
# or else, if it's 4, show the Geometry Panel
        elif bpy.types.Scene.PanelSelect == 4:
            column = split.column(align=True)
            column.operator("blui.add_plane", text="Plane", icon='MESH_PLANE')
            column.operator("blui.add_cube", text="Cube", icon='MESH_CUBE')
            column.operator("blui.add_circle", text="Circle", icon='MESH_CIRCLE')
            column.operator("blui.add_uv_sphere", text="UV Sphere", icon='MESH_UVSPHERE')
            column.operator("blui.add_ico_sphere", text="Ico Sphere", icon='MESH_ICOSPHERE')
            column.operator("blui.add_cylinder", text="Cylinder", icon='MESH_CYLINDER')
            column.operator("blui.add_cone", text="Cone", icon='MESH_CONE')
            column.operator("blui.add_torus", text="Torus", icon='MESH_TORUS')
            column.operator("blui.add_monkey", text="Suzanne", icon='MESH_MONKEY')




####################################################################################### Menu version

class BLUI_MT_unreal_basic_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_unreal_basic_menu'
    bl_label = 'Basic'

    def draw(self, context):
        layout = self.layout
        layout.operator("blui.add_cube", text="Cube", icon='MESH_CUBE')
        layout.operator("blui.add_empty", text="Empty", icon='EMPTY_DATA')
        layout.operator("blui.add_point_light", text="Light", icon='LIGHT')
        layout.operator("blui.add_cube", text="Cube", icon='MESH_CUBE')
        layout.operator("blui.add_uv_sphere", text="Sphere", icon='MESH_UVSPHERE')
        layout.operator("blui.add_cylinder", text="Cylinder", icon='MESH_CYLINDER')

def menu_func(self, context):
    self.layout.menu("BLUI_MT_unreal_basic_menu")

class BLUI_MT_unreal_lights_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_unreal_lights_menu'
    bl_label = 'Lights'

    def draw(self, context):
        layout = self.layout
        layout.operator("blui.add_directional_light", text="Directional", icon='LIGHT_AREA')
        layout.operator("blui.add_point_light", text="Point", icon='LIGHT_POINT')
        layout.operator("blui.add_spot_light", text="Spot", icon='LIGHT_SPOT')
        layout.operator("blui.add_sun_light", text="Sun", icon='LIGHT_SUN')

def menu_func(self, context):
    self.layout.menu("BLUI_MT_unreal_lights_menu")

class BLUI_MT_unreal_cinematic_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_unreal_cinematic_menu'
    bl_label = 'Cinematic'

    def draw(self, context):
        layout = self.layout
        layout.operator("blui.add_long_camera", text="Camera", icon='VIEW_CAMERA')

def menu_func(self, context):
    self.layout.menu("BLUI_MT_unreal_cinematic_menu")

class BLUI_MT_unreal_vfx_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_unreal_vfx_menu'
    bl_label = 'VFX'

    def draw(self, context):
        layout = self.layout
        layout.operator("blui.add_cubemap", text="Cubemap", icon='LIGHTPROBE_CUBEMAP')
        layout.operator("blui.add_planar", text="Planar", icon='LIGHTPROBE_PLANAR')
        layout.operator("blui.add_grid", text="Irradiance", icon='LIGHTPROBE_GRID')

def menu_func(self, context):
    self.layout.menu("BLUI_MT_unreal_vfx_menu")

class BLUI_MT_unreal_geometry_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_unreal_geometry_menu'
    bl_label = 'Geometry'

    def draw(self, context):
        layout = self.layout
        layout.operator("blui.add_plane", text="Plane", icon='MESH_PLANE')
        layout.operator("blui.add_cube", text="Cube", icon='MESH_CUBE')
        layout.operator("blui.add_circle", text="Circle", icon='MESH_CIRCLE')
        layout.operator("blui.add_uv_sphere", text="UV Sphere", icon='MESH_UVSPHERE')
        layout.operator("blui.add_ico_sphere", text="Ico Sphere", icon='MESH_ICOSPHERE')
        layout.operator("blui.add_cylinder", text="Cylinder", icon='MESH_CYLINDER')
        layout.operator("blui.add_cone", text="Cone", icon='MESH_CONE')
        layout.operator("blui.add_torus", text="Torus", icon='MESH_TORUS')
        layout.operator("blui.add_monkey", text="Suzanne", icon='MESH_MONKEY')

def menu_func(self, context):
    self.layout.menu("BLUI_MT_unreal_geometry_menu")

class BLUI_MT_unreal_parent_menu(bpy.types.Menu):
    bl_idname = 'BLUI_MT_unreal_parent_menu'
    bl_label = 'Unreal Objects'

    def draw(self, context):
        layout = self.layout
        layout.menu("BLUI_MT_unreal_basic_menu", icon='MESH_CUBE')
        layout.menu("BLUI_MT_unreal_lights_menu", icon='LIGHT')
        layout.menu("BLUI_MT_unreal_cinematic_menu", icon='VIEW_CAMERA')
        layout.menu("BLUI_MT_unreal_vfx_menu", icon='LIGHTPROBE_CUBEMAP')
        layout.menu("BLUI_MT_unreal_geometry_menu", icon='MESH_ICOSPHERE')


def menu_func(self, context):
    #if context.preferences.addons['Unreal Objects'].preferences.showinaddmenu == True:
    self.layout.menu("BLUI_MT_unreal_parent_menu", icon='EVENT_U')






######################################################################### Classes and Registration


# Adding all the classes to an array to make the register/unregister functions below a little tidier
classes = [
    BLUI_OT_comment_box,
    BLUI_PT_unreal_parent_panel,
    BLUI_PT_unreal_objects_panel,
    BLUI_OT_show_basic_panel,
    BLUI_OT_show_lights_panel,
    BLUI_OT_show_camera_panel,
    BLUI_OT_show_vfx_panel,
    BLUI_OT_show_geometry_panel,
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
    BLUI_OT_add_circle,
    BLUI_OT_add_long_camera,
    BLUI_OT_add_cubemap,
    BLUI_OT_add_planar,
    BLUI_OT_add_grid,
    BLUI_MT_unreal_parent_menu,
    BLUI_MT_unreal_basic_menu,
    BLUI_MT_unreal_lights_menu, 
    BLUI_MT_unreal_cinematic_menu,
    BLUI_MT_unreal_vfx_menu,
    BLUI_MT_unreal_geometry_menu,
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
