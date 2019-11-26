import hou


def promote_to_HDA () :
    selectedNodes = hou.selectedNodes()
    hdanode       = selectedNodes[0].parent()
    hda_definition    = hdanode.type().definition()


    ptg = hda_definition.parmTemplateGroup()


    # folder name
    new_folder_name = ()
    new_folder_name = hou.ui.readInput(
        message = "new_folder_name:",
        initial_contents = "l_arm")
    
    new_folder_name = new_folder_name[1]
    new_folder      = hou.FolderParmTemplate(new_folder_name, new_folder_name)


    ##################
    ## create parms ##

    for selectedNode in selectedNodes :
        parm_names = promote_to_HDA_parm_names(selectedNode)
        for parm_name in parm_names :
            # new template
            new_template = selectedNode.parmTuple(parm_name).parmTemplate()
            new_name     = selectedNode.name() + "_" + parm_name

            new_template.setName(new_name)
            new_template.setLabel(new_name)
            new_folder.addParmTemplate(new_template)

    ptg.append(new_folder)
    hda_definition.setParmTemplateGroup(ptg)

    #####################
    ## reference parms ##

    for selectedNode in selectedNodes :
        parm_list = promote_to_HDA_parm_list(selectedNode)
        for parm_name in parm_list :
            parm_node     = selectedNode.parmTuple(parm_name)
            parm_name_hda = selectedNode.name() + "_" + parm_name
            parm_hda      = selectedNode.parent().parmTuple(parm_name_hda)
            parm_hda.set(parm_node.eval())
            parm_node.set(parm_hda)

    # hda_definition.save(hda_definition.libraryFilePath())



def promote_to_HDA_parm_list (node) :
    if node.type().name() == "null" :
        parm_list = ["t", "r"]
    if node.type().name() == "bone" :
        parm_list = ["r", "length"]

    return parm_list