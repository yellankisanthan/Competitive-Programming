def find_rectangular_overlap(rect1, rect2):
    left_x = max(rect1['left_x'], rect2['left_x'])
    right_x = min(rect1['left_x'] + rect1['width'], rect2['left_x'] + rect2['width'])
    width = right_x - left_x

    lower_y = max(rect1['bottom_y'], rect2['bottom_y'])
    upper_y = min(rect1['bottom_y'] + rect1['height'], rect2['bottom_y'] + rect2['height'])
    height = upper_y - lower_y

    if width < 1 or height < 1:
        intersection = {'left_x': None, 'bottom_y': None, 'width': None, 'height': None}
    else:
        intersection = {'left_x': left_x, 'bottom_y': lower_y, 'width': width, 'height': height}
    return intersection

# Tests

rect1 = {
    'left_x': 1,
    'bottom_y': 1,
    'width': 6,
    'height': 3,
}
rect2 = {
    'left_x': 5,
    'bottom_y': 2,
    'width': 3,
    'height': 6,
}
expected = {
    'left_x': 5,
    'bottom_y': 2,
    'width': 2,
    'height': 2,
}
actual = find_rectangular_overlap(rect1, rect2)
print(actual == expected)


rect1 = {
    'left_x': 1,
    'bottom_y': 1,
    'width': 6,
    'height': 6,
}
rect2 = {
    'left_x': 3,
    'bottom_y': 3,
    'width': 2,
    'height': 2,
}
expected = {
    'left_x': 3,
    'bottom_y': 3,
    'width': 2,
    'height': 2,
}
actual = find_rectangular_overlap(rect1, rect2)
print(actual == expected)

rect1 = {
    'left_x': 2,
    'bottom_y': 2,
    'width': 4,
    'height': 4,
}
rect2 = {
    'left_x': 2,
    'bottom_y': 2,
    'width': 4,
    'height': 4,
}
expected = {
    'left_x': 2,
    'bottom_y': 2,
    'width': 4,
    'height': 4,
}
actual = find_rectangular_overlap(rect1, rect2)
print(actual == expected)

rect1 = {
    'left_x': 1,
    'bottom_y': 2,
    'width': 3,
    'height': 4,
}
rect2 = {
    'left_x': 2,
    'bottom_y': 6,
    'width': 2,
    'height': 2,
}
expected = {
    'left_x': None,
    'bottom_y': None,
    'width': None,
    'height': None,
}
actual = find_rectangular_overlap(rect1, rect2)
print(actual == expected)

rect1 = {
    'left_x': 1,
    'bottom_y': 2,
    'width': 3,
    'height': 4,
}
rect2 = {
    'left_x': 4,
    'bottom_y': 3,
    'width': 2,
    'height': 2,
}
expected = {
    'left_x': None,
    'bottom_y': None,
    'width': None,
    'height': None,
}
actual = find_rectangular_overlap(rect1, rect2)
print(actual == expected)

rect1 = {
    'left_x': 1,
    'bottom_y': 1,
    'width': 2,
    'height': 2,
}
rect2 = {
    'left_x': 3,
    'bottom_y': 3,
    'width': 2,
    'height': 2,
}
expected = {
    'left_x': None,
    'bottom_y': None,
    'width': None,
    'height': None,
}
actual = find_rectangular_overlap(rect1, rect2)
print(actual == expected)

rect1 = {
    'left_x': 1,
    'bottom_y': 1,
    'width': 2,
    'height': 2,
}
rect2 = {
    'left_x': 4,
    'bottom_y': 6,
    'width': 3,
    'height': 6,
}
expected = {
    'left_x': None,
    'bottom_y': None,
    'width': None,
    'height': None,
}
actual = find_rectangular_overlap(rect1, rect2)
print(actual == expected)