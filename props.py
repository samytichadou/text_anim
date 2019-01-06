import bpy

from .update_functions import update_fct_main

### FONT ###
class TextAnimFontPropsColl(bpy.types.PropertyGroup):
    '''name = StringProperty() '''
    
    controller = bpy.props.StringProperty(default="")
    index = bpy.props.IntProperty()
    original_location = bpy.props.FloatVectorProperty(name="Original Location")
    original_scale = bpy.props.FloatVectorProperty(name="Original Scale", default=[1,1,1])
    original_spacing = bpy.props.FloatProperty(name="Original Spacing", default=0.0)
    original_pass_index = bpy.props.IntProperty(name="Original Object Pass", default=0)

### ANIMATIONS ###
class TextAnimAnimationColl(bpy.types.PropertyGroup):
    
    ### animation ###
    
    #misc
    hidden = bpy.props.BoolProperty(name="Hidden", default=False)
    active = bpy.props.BoolProperty(name="Active", default=True, update=update_fct_main)
    
    #range
    start_pct = bpy.props.IntProperty(name="Start", default=0, min=0, max=100, update=update_fct_main)
    end_pct = bpy.props.IntProperty(name="End", default=100, min=0, max=100, update=update_fct_main)

    #interpolation
    overlap_value = bpy.props.IntProperty(name="Overlap", default=0, min=0, max=100, update=update_fct_main)
    smooth_in = bpy.props.FloatProperty(name="Smooth In", default=0, min=0, max=1, update=update_fct_main)
    smooth_out = bpy.props.FloatProperty(name="Smooth Out", default=0, min=0, max=1, update=update_fct_main)

    #active props
    location_active = bpy.props.BoolProperty(name="Location Toggle", default=False, update=update_fct_main)
    spacing_active = bpy.props.BoolProperty(name="Spacing Toggle", default=False, update=update_fct_main)
    node_active = bpy.props.BoolProperty(name="Node Toggle", default=False, update=update_fct_main)
    scale_active = bpy.props.BoolProperty(name="Scale Toggle", default=False, update=update_fct_main)
    
    #location
    location = bpy.props.FloatVectorProperty(name="Location", update=update_fct_main)
    
    #spacing
    spacing = bpy.props.FloatProperty(name="Spacing", default=0, update=update_fct_main)
    spacing_offset = bpy.props.BoolProperty(name="Offset", default=False, update=update_fct_main)
    spacing_type = bpy.props.EnumProperty(items= (('LEFT', 'Left', 'From left'),    
                                                 ('RIGHT', 'Right', 'From Right')),
                                                 name = "Type", default='LEFT', update=update_fct_main)
                                                 
    #node data
    custom_node_data_base = bpy.props.FloatProperty(name="Node Data Base", default=0, update=update_fct_main)
    custom_node_data_target = bpy.props.FloatProperty(name="Node Data Target", default=1, update=update_fct_main)
    
    #scale
    scale = bpy.props.FloatVectorProperty(name="Scale", default=[1,1,1], update=update_fct_main)
    unified_scale_toggle = bpy.props.BoolProperty(name="Unified", default=True, update=update_fct_main)
    scale_unified = bpy.props.FloatProperty(name="Scale", default=1, update=update_fct_main)
    scale_offset = bpy.props.BoolProperty(name="Offset", default=True, update=update_fct_main)
    

### CONTROLLER ###
class TextAnimEmptyPropsColl(bpy.types.PropertyGroup):
    '''name = StringProperty() '''
    
    body = bpy.props.StringProperty()
    animations = bpy.props.CollectionProperty(type=TextAnimAnimationColl, name='Animations')
    animation_index = bpy.props.IntProperty()