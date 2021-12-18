import slippi as slp

def wavedash_waveland_counter(game):
    #number of wavedashs & wavelands
    #assumes using port 0 and 1; otherwise just change the line "for j in [0,1]"

    #wavedash/waveland animation is (43:LANDING_FALL_SPECIAL), after a jump (JUMP_F, JUMP_B: 25, 26)
    # or their aerial version (27,28)
    # or an air dodge (236:ESCAPE_AIR)
    # if perfect, the 2nd previous frame is 24:KNEE_BEND (jump startup)

    # a waveland is detected if none of the previous 6 frames was KNEE_BEND
    # this might mislabel especially unclean wavedashs as wavelands

    number_of_wavedashs, number_of_perfect_wavedashs, number_of_wavelands = [0,0], [0,0], [0,0]

    #use an offset of 6 to be able to compare with the 6th-previous frame
    for i in range(len(game.frames)-6):
        for j in [0,1]:
            #condition for wavedash/land
            if ((game.frames[i+6].ports[j].leader.pre.state == 43) and (game.frames[i+5].ports[j].leader.pre.state != 43)):
                #condition for perfect wavedash: 2nd-previous frame is 24:KNEE_BEND
                if (game.frames[i+4].ports[j].leader.pre.state == 24):
                    number_of_wavedashs[j]+=1
                    number_of_perfect_wavedashs[j]+=1
                else:
                    #non-perfect-wavedash condition, checking the 3rd-to-6th previous frame
                    for k in range(4):
                        if (game.frames[i+k].ports[j].leader.pre.state == 24):
                            number_of_wavedashs[j]+=1
                            break
                    #otherwise: waveland
                    number_of_wavelands[j]+=1

    return number_of_wavedashs, number_of_perfect_wavedashs, number_of_wavelands