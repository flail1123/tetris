'''
Block is a set of 4 fields(component parts), there is the main component part and the rest's position is relative
to the position of the main component part, block also has possible rotations and initial position depending on
rotation
Block is created with the number of block which is the type of a block:
1: ****  2: ***  3: ***  4: ***  5:  **  6: **  7: **
            *         *      *      **       **    **
'''
allComponentParts = [[], [[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, 1), (0, 2), (0, -1)]],
                     [[(0, 0), (1, 0), (2, 0), (0, 1)], [(0, 0), (0, 1), (0, -1), (-1, -1)],
                      [(0, 0), (1, 0), (2, 0), (2, -1)], [(0, 0), (0, 1), (0, -1), (1, 1)]],
                     [[(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (0, 1), (0, -1), (-1, 1)],
                      [(0, 0), (1, 0), (2, 0), (0, -1)], [(0, 0), (0, 1), (0, -1), (1, -1)]],
                     [[(0, 0), (1, 0), (2, 0), (1, 1)], [(0, 0), (0, 1), (0, -1), (-1, 0)],
                      [(0, 0), (1, 0), (2, 0), (1, -1)], [(0, 0), (0, 1), (0, -1), (1, 0)]],
                     [[(0, 0), (1, 0), (1, -1), (2, -1)], [(0, 0), (0, -1), (1, 0), (1, 1)]],
                     [[(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (1, 0), (1, -1)]],
                     [[(0, 0), (0, 1), (1, 0), (1, 1)]]]
allRotations = [[], [0, 90], [0, 90, 180, 270], [0, 90, 180, 270], [0, 90, 180, 270], [0, 90], [0, 90], [0]]

allPositions = [[()], [(3, 0), (4, 0)], [(3, 0), (4, 0), (3, 0), (4, 0)], [(3, 0), (4, 0), (3, 0), (4, 0)],
                [(3, 0), (4, 0), (3, 0), (4, 0)], [(3, 1), (4, 0)], [(3, 0), (4, 0)], [(4, 0)]]


class Block:
    def __init__(self, number):
        self.__componentPart = allComponentParts[number]  # this is a list of component parts at every rotation
        self.__rotations = allRotations[number]  # this is a list of rotations of block for example [0, 90, 180, 270]
        self.currentRotation = 0
        self.__positions = allPositions[number] # list of all initial position for every rotation
        self.__number = number

    def number(self):
        return self.__number

    def position(self):
        if self.currentRotation == 0:
            return self.__positions[0]
        elif self.currentRotation == 90:
            return self.__positions[1]
        elif self.currentRotation == 180:
            return self.__positions[2]
        elif self.currentRotation == 270:
            return self.__positions[3]

    def currentComponentParts(self):
        # returns relative coordinates of all component part relative to the main part (0, 0)
        if self.currentRotation == 0:
            return self.__componentPart[0]
        elif self.currentRotation == 90:
            return self.__componentPart[1]
        elif self.currentRotation == 180:
            return self.__componentPart[2]
        elif self.currentRotation == 270:
            return self.__componentPart[3]

    def rotations(self):
        return self.__rotations

