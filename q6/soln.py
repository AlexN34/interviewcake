from collections import OrderedDict
import json
def rectangle_love(rect1, rect2):
    # write the body of your function here
    rect1, rect2 = _calc_leftmost(rect1, rect2)
    final_x, final_width = _calc_dims(rect1['left_x'], rect2['left_x'], rect1['width'], rect2['width'])
    final_y, final_height = _calc_dims(rect1['bottom_y'], rect2['bottom_y'], rect1['height'], rect2['height'])
    if (final_x == 0 and final_width == 0) or (final_y == 0 and final_height == 0):
        final_x, final_width, final_y, final_height = (None, None, None, None)
    return OrderedDict({
        'left_x': final_x,
        'bottom_y': final_y,
        'width': final_width,
        'height': final_height,
    })

def _calc_leftmost(rect1, rect2):
    if rect1['left_x'] <= rect2['left_x']:
        return (rect1, rect2)
    else:
        return (rect2, rect1)



def _calc_dims(coord_leftmost, coord_other, length_leftmost, length_other):
    if coord_leftmost + length_leftmost > coord_other:
        if coord_other + length_other > coord_leftmost + length_leftmost:
            return (coord_other, coord_leftmost + length_leftmost - coord_other)
        else:
            return (coord_other, length_other)
    else:
        return (None, None)

# run your function through some test cases here
# remember: debugging is half the battle!
my_rectangle1 = OrderedDict({

    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,

})

my_rectangle2 = OrderedDict({

    # Coordinates of bottom-left corner
    'left_x'   : 7,
    'bottom_y' : 2,

    # Width and height
    'width'    : 3,
    'height'   : 6,

})

print(json.dumps(rectangle_love(my_rectangle1, my_rectangle2)))
