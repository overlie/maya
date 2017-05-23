import maya.cmds as cmds


redClr = 0.9, 0.1, 0.1
redDrkClr = 0.4, 0.0, 0.0

blueClr = 0.19, 0.4, 0.63
blueDrkClr = 0.0, 0.0, 0.6

greenClr = 0.0, 0.6, 0.0
greenDrkClr = 0.0, 0.3, 0.0

yellowClr = 0.9, 0.9, 0.1
yellowDrkClr = 0.6, 0.6, 0.0



btnW = 64
btnH = 24



def red(*args):

    myList= cmds.ls(selection=True)

    if myList:
        myShapes = p.listRelatives(myList, shapes=True)

        for my in myShapes:
            cmds.setAttr(my + ".overrideEnabled", 1)
            cmds.setAttr(my + '.overrideRGBColors', 1)
            cmds.setAttr(my + ".overrideColorRGB", redClr[0],redClr[1],redClr[2] )

    else:
        cmds.warning( "Nothing is selected" )









def redDark(*args):

    myList= cmds.ls(selection=True)

    if myList:
        myShapes = p.listRelatives(myList, shapes=True)

        for my in myShapes:
            cmds.setAttr(my + ".overrideEnabled", 1)
            cmds.setAttr(my + '.overrideRGBColors', 1)
            cmds.setAttr(my + ".overrideColorRGB", redDrkClr[0], redDrkClr[1], redDrkClr[2] )

    else:
        cmds.warning( "Nothing is selected" )






def blue(*args):

    myList= cmds.ls(selection=True)

    if myList:
        myShapes = p.listRelatives(myList, shapes=True)

        for my in myShapes:
            cmds.setAttr(my + ".overrideEnabled", 1)
            cmds.setAttr(my + '.overrideRGBColors', 1)
            cmds.setAttr(my + ".overrideColorRGB", blueClr[0], blueClr[1], blueClr[2])

    else:
        cmds.warning( "Nothing is selected" )






def blueDark(*args):

    myList= cmds.ls(selection=True)

    if myList:
        myShapes = p.listRelatives(myList, shapes=True)

        for my in myShapes:
            cmds.setAttr(my + ".overrideEnabled", 1)
            cmds.setAttr(my + '.overrideRGBColors', 1)
            cmds.setAttr(my + ".overrideColorRGB", blueDrkClr[0], blueDrkClr[1], blueDrkClr[2])

    else:
        cmds.warning( "Nothing is selected" )








def yellowDark(*args):

    myList= cmds.ls(selection=True)

    if myList:
        myShapes = p.listRelatives(myList, shapes=True)

        for my in myShapes:
            cmds.setAttr(my + ".overrideEnabled", 1)
            cmds.setAttr(my + '.overrideRGBColors', 1)
            cmds.setAttr(my + ".overrideColorRGB", yellowDrkClr[0], yellowDrkClr[1], yellowDrkClr[2])

    else:
        cmds.warning( "Nothing is selected" )







def green(*args):

    myList= cmds.ls(selection=True)

    if myList:
        myShapes = p.listRelatives(myList, shapes=True)

        for my in myShapes:
            cmds.setAttr(my + ".overrideEnabled", 1)
            cmds.setAttr(my + '.overrideRGBColors', 1)
            cmds.setAttr(my + ".overrideColorRGB", greenClr[0],greenClr[1], greenClr[2])

    else:
        cmds.warning( "Nothing is selected" )







def greenDark(*args):

    myList= cmds.ls(selection=True)

    if myList:
        myShapes = p.listRelatives(myList, shapes=True)
        
        for my in myShapes:
            cmds.setAttr(my + ".overrideEnabled", 1)
            cmds.setAttr(my + '.overrideRGBColors', 1)
            cmds.setAttr(my + ".overrideColorRGB", greenDrkClr[0],greenDrkClr[1], greenDrkClr[2])         
    
    else: 
        cmds.warning( "Nothing is selected" )




####CREATE WINDOW####
if cmds.window("clrWindow", exists = True):
    cmds.deleteUI("clrWindow")


cmds.window( "clrWindow", title="clrWindow", width=132 )
cmds.columnLayout()
rootLayout = cmds.columnLayout()
frameOne = cmds.columnLayout()

# create content
cmds.rowColumnLayout(numberOfColumns=4, columnWidth=[(1,btnW),(2,btnW),(3,btnW),(4,btnW)])
cmds.button( label='', w=btnW, h=btnH, bgc= redClr, command=red )
cmds.button( label='', w=btnW, h=btnH, bgc= greenClr, command=green )
cmds.button( label='', w=btnW, h=btnH, bgc= blueClr, command=blue  )
cmds.button( label='', w=btnW, h=btnH, bgc= yellowClr, command=yellow )
cmds.setParent('..')
cmds.rowColumnLayout(numberOfColumns=4, columnWidth=[(1,btnW),(2,btnW),(3,btnW),(4,btnW)])
cmds.button( label='', w=btnW, h=btnH, bgc= redDrkClr, command=redDark)
cmds.button( label='', w=btnW, h=btnH, bgc= greenDrkClr, command=greenDark )
cmds.button( label='', w=btnW, h=btnH, bgc= blueDrkClr, command=blueDark  )
cmds.button( label='', w=btnW, h=btnH, bgc= yellowDrkClr, command=yellowDark )
cmds.showWindow()





