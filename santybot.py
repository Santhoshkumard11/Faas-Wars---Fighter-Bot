def main(args):
    res = []
    ev = args["event"] if "event" in args else ""
    try:
        if ev == "idle":
            if args["data"]:
                my_angle = args["angle"]
                enemy_angle = args["data"]["angle"]
                res.append({"turn_turret_left": my_angle - enemy_angle} if my_angle > enemy_angle else {"turn_turret_right": enemy_angle - my_angle})
                res.append({"shoot":True,"data": {},"shoot":True,"shoot":True})
            else:
                res.append({"move_forwards": 10,"turn_turret_left":150})
                res.append({"move_forwards": 10,"turn_turret_right":150})
            
        elif ev == "wall-collide":
            res.append({"move_opposide":300})
            res.append({"turn_left":90})
            
        elif ev == "hit":
            res.append({"move_backwards": 100,"yell": "Oops!"})

        elif ev == "enemy-spot":
            enemy_spot = args["enemy_spot"]["angle"]
            # my_angle = args["angle"]
            # res.append({"turn_turret_left": my_angle - enemy_spot} if my_angle > enemy_spot else {"turn_turret_right": enemy_spot - my_angle})
            res.append({"data":{"angle":enemy_spot},"yell":"Enemy Spotted"})
            
        else:
            print(args)
    except:
        return {"body": res.append({"move_forwards": 10,"turn_turret_left":90})}
    return {"body": res}

# game = {"event":"idle"}

# main(game)
