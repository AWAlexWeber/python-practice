'''
God I actually hate this problem so much.

Given a 2d matrix perform a spiral.
'''

from typing import List
RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3


class Grid(object):
  def __init__(self, matrix):
    self.matrix = matrix

  def __next_position(self, position, direction):
    if direction == RIGHT:
      return (position[0], position[1] + 1)
    elif direction == DOWN:
      return (position[0] + 1, position[1])
    elif direction == LEFT:
      return (position[0], position[1] - 1)
    elif direction == UP:
      return (position[0] - 1, position[1])

  def __next_direction(self, direction):
    return {
        RIGHT: DOWN,
        DOWN: LEFT,
        LEFT: UP,
        UP: RIGHT
    }[direction]

  def __is_valid_position(self, pos):
    return (0 <= pos[0] < len(self.matrix) and
            0 <= pos[1] < len(self.matrix[0]) and
            self.matrix[pos[0]][pos[1]] is not None)

  def spiralPrint(self):
    remaining = len(self.matrix) * len(self.matrix[0])
    current_direction = RIGHT
    current_position = (0, 0)
    result = ''
    while remaining > 0:
      remaining -= 1
      result += str(self.matrix[current_position[0]]
                    [current_position[1]]) + ' '
      self.matrix[current_position[0]][current_position[1]] = None

      next_position = self.__next_position(current_position, current_direction)
      if not self.__is_valid_position(next_position):
        current_direction = self.__next_direction(current_direction)
        current_position = self.__next_position(
            current_position, current_direction)
      else:
        current_position = self.__next_position(
            current_position, current_direction)

    return result


grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

print(Grid(grid).spiralPrint())
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12 