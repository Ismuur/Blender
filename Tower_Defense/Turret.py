import bge


def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner
    sens = cont.sensors['Nearest']
    act = cont.actuators['trackTo']
    objList = sens.hitObjectList
    
    if near.sensor.positive:
        target = objList[0]
        act.object = target
        cont.activate(act)
    else:
        cont.desactivate(act)    
main()