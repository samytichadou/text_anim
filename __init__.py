'''
Copyright (C) 2018 YOUR NAME
YOUR@MAIL.com

Created by YOUR NAME

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Your Addon Name",
    "description": "",
    "author": "Your Name",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object" }


import bpy


# load and reload submodules
##################################

import importlib
from . import developer_utils
importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())

from .props import TextAnimFontPropsColl, TextAnimEmptyPropsColl
from .handler import text_anim_handler

# register
##################################

import traceback

def register():
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
    
    print("Registered {} with {} modules".format(bl_info["name"], len(modules)))

    #add props
    bpy.types.TextCurve.text_anim = bpy.props.CollectionProperty(type=TextAnimFontPropsColl, name='Text Anim')
    bpy.types.Object.text_anim = bpy.props.CollectionProperty(type=TextAnimEmptyPropsColl, name='Text Anim')
    
    #handler
    bpy.app.handlers.frame_change_post.append(text_anim_handler)
    
def unregister():
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    print("Unregistered {}".format(bl_info["name"]))
    
    #del props
    del bpy.types.TextCurve.text_anim
    del bpy.types.Object.text_anim
    
    #handler
    bpy.app.handlers.frame_change_post.remove(text_anim_handler)