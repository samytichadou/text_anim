import bpy

from .misc_functions import get_list_from_controller

def evaluation_linear_pct(animation, controller):
    inf_list=[]
    #props=controller.text_anim[0]
    object_list=get_list_from_controller(controller)
    
    lgt=len(object_list)
    start=animation.start_pct/100
    end=animation.end_pct/100
    
    coef=100/lgt/100
    
    for i in range(0, lgt):
        
        ob_st=(i*coef)
        ob_en=(i+1)*coef
        
        if start<ob_en and start>ob_st:
            diff_st=(start-ob_st)*lgt
        elif start<=ob_st:
            diff_st=0
        else:
            diff_st=1
            
        if ob_st<end and ob_en>end:
            diff_en=(ob_en-end)*lgt
        elif ob_en<=end:
            diff_en=0    
        else:
            diff_en=1
            
        if end>=start:
            inf=diff_st+diff_en
        else:
            inf=1-(diff_st+diff_en-1)
        
        inf_list.append(inf)
        
        #debug
#        print()
#        print(object_list[i].name)
#        print(str(coef))
#        print(str(ob_st))
#        print(str(ob_en))
#        print(str(inf))
        
    return inf_list
