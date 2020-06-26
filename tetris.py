from matrix import *
from random import *
import time
import threading
import msvcrt

setOfBlockObjects = [[[[0, 0, 1],
                       [1, 1, 1],
                       [0, 0, 0]],
                      [[0, 1, 0],
                       [0, 1, 0],
                       [0, 1, 1]],
                      [[0, 0, 0],
                       [1, 1, 1],
                       [1, 0, 0]],
                      [[1, 1, 0],
                       [0, 1, 0],
                       [0, 1, 0]]],
                     [[[1, 0, 0],
                       [1, 1, 1],
                       [0, 0, 0]],
                      [[0, 1, 1],
                       [0, 1, 0],
                       [0, 1, 0]],
                      [[0, 0, 0],
                       [1, 1, 1],
                       [0, 0, 1]],
                      [[0, 1, 0],
                       [0, 1, 0],
                       [1, 1, 0]]],
                     [[[0, 1, 0],
                       [1, 1, 1],
                       [0, 0, 0]],
                      [[0, 1, 0],
                       [0, 1, 1],
                       [0, 1, 0]],
                      [[0, 0, 0],
                       [1, 1, 1],
                       [0, 1, 0]],
                      [[0, 1, 0],
                       [1, 1, 0],
                       [0, 1, 0]]]]

arrayScreen = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

class Tetris:
    def __init__(self,dy,dx):
        self.idxBlockDegree = randint(0,3)
        self.idxBlockType = randint(0,2)
        self.currBlk = Matrix(setOfBlockObjects[self.idxBlockType][self.idxBlockDegree])
        self.iScreenDy = dy
        self.iScreenDx = dx
        self.iScreenDw = 4
        self.top = 0
        self.left = self.iScreenDw + self.iScreenDx // 2 - 2
        self.newBlockNeeded = False
        self.iScreen = Matrix(arrayScreen)
        self.oScreen = Matrix(self.iScreen)
        self.tempBlk = self.iScreen.clip(self.top, self.left, self.top + self.currBlk.get_dy(), self.left + self.currBlk.get_dx())
        self.tempBlk = self.tempBlk + self.currBlk
        self.oScreen.paste(self.tempBlk, self.top, self.left)
        self.draw_matrix(self.oScreen)

    def get_type(self):
        return self.idxBlockType

    def draw_matrix(self,m):
        array = m.get_array()
        for y in range(m.get_dy()):
            for x in range(m.get_dx()):
                if array[y][x] == 0:
                    print("□", end='')
                elif array[y][x] == 1:
                    print("■", end='')
                else:
                    print("X", end='')
            print()

    def update_blk(self):
        self.currBlk = Matrix(setOfBlockObjects[self.idxBlockType][self.idxBlockDegree])
        self.tempBlk = self.iScreen.clip(self.top, self.left, self.top + self.currBlk.get_dy(), self.left + self.currBlk.get_dx())
        self.tempBlk = self.tempBlk + self.currBlk

    def erase_fullline(self):
        for y in reversed(range(self.top, 15)):  # reversed would be better choice
            if sum(self.oScreen._array[y]) == 18:
                self.oScreen.clip(0, 0, y, 18)
                self.clipBlk = self.oScreen.clip(0, 0, y, 18)
                self.oScreen.paste(self.clipBlk, 1, 0)
                self.newBlockNeeded = True

    def main(self):

        while 1:
            if msvcrt.kbhit():
            #key = 's'
                key = msvcrt.getwch()
            #print(key)
            #key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ',1)
            # def gravity(self):
            #    while(1):
            #        top += 1
            # threading.Timer(1.0,gravity).start()
                if key == 'q':
                    print('Game terminated...')
                    break
                elif key == 'a':  # move left
                    self.left -= 1
                elif key == 'd':  # move right
                    self.left += 1
                elif key == 's':  # move down
                    self.top += 1
                elif key == 'w':  # rotate the block clockwise
                    self.idxBlockDegree = (self.idxBlockDegree + 1) % 4
                # print('Not implemented')

                elif key == ' ':  # drop the block
                    while not self.tempBlk.anyGreaterThan(1):  # collision 바로 전으로
                        self.top += 1
                        self.update_blk()
                    #tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
                    #tempBlk = tempBlk + currBlk
                    self.top -= 1
                    self.newBlockNeeded = True
                # print('Not implemented')

            else:
                self.top += 1
                time.sleep(0.2)

                # print('Wrong key!!!')
                # continue
            #self.top += 1
            #time.sleep(0.5)

            # ' ' also need to copy again cuz of -1 , rotate didn't update in tempBlk
            self.update_blk()

            if self.tempBlk.anyGreaterThan(1):
                if key == 'a':  # undo: move right
                    self.left += 1
                elif key == 'd':  # undo: move left
                    self.left -= 1
                elif key == 's':  # undo: move up
                    self.top -= 1
                    self.newBlockNeeded = True
                elif key == 'w':  # undo: rotate the block counter-clockwise
                    self.idxBlockDegree -= 1
                    # print('Not implemented')
                elif key == ' ':  # undo: move up
                    # top = temp
                    print('Not implemented')
                    # currBlk = Matrix(setOfBlockObjects[idxBlockType][idxBlockDegree])
                    # tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
                    # tempBlk = tempBlk + currBlk
                else:
                    self.top -= 1
                    self.newBlockNeeded = True     

            self.update_blk()

            self.oScreen = Matrix(self.iScreen)  # previous stage screen
            self.oScreen.paste(self.tempBlk, self.top, self.left)
            self.erase_fullline()
            # iScreen = Matrix(arrayScreen)
            # draw_matrix(oScreen); print()

            if self.newBlockNeeded:
                self.iScreen = Matrix(self.oScreen)
                self.top = 0
                self.left = self.iScreenDw + self.iScreenDx // 2 - 2
                self.newBlockNeeded = False
                self.idxBlockDegree = randint(0, 3)
                self.idxBlockType = randint(0, 2)
                self.update_blk()
                if self.tempBlk.anyGreaterThan(1):
                    print('Game Over!!!')  # tempBlk 뿐만아니라 위에 블럭을 침입하면 game over하게 고치기!
                    break

            self.oScreen = Matrix(self.iScreen)  # previous stage screen
            self.oScreen.paste(self.tempBlk, self.top, self.left)
            self.draw_matrix(self.oScreen);
            print()