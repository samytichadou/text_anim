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
    

### ANIMATIONS ###
class TextAnimAnimationColl(bpy.types.PropertyGroup):
    
    ### animation ###
    
    #misc
    hidden = bpy.props.BoolProperty(name="Hidden", default=False)
    active = bpy.props.BoolProperty(name="Active", default=True)
    
    #range
    start_pct = bpy.props.IntProperty(name="Start", default=0, min=0, max=100, update=update_fct_main)
    end_pct = bpy.props.IntProperty(name="End", default=100, min=0, max=100, update=update_fct_main)
    
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
    
    ### switch between test and real anim system ###
    
    test_switch=bpy.props.BoolProperty()
    
    ### animation props for testing purposes ###
    
    
    #range
    start_pct = bpy.props.IntProperty(name="Start", default=0, min=0, max=100, update=update_fct_main)
    end_pct = bpy.props.IntProperty(name="End", default=100, min=0, max=100, update=update_fct_main)
    
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