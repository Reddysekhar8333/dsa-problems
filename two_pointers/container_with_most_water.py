# given an array of heights, find two lines that together hold more the water.
# input : heights=[1,8,6,2,5,4,8,3,7]
# output: 49

def container_with_most_water(height):
    # my approach is area of rectangle (lenght*breadth) & using two pointers
    left = 0
    right = len(height)-1
    area = 0
    while left < right:
        lenght = right - left
        breadth = min(height[left], height[right])
        area = max(area, lenght*breadth)
        if height[left]< height[right]:
            left += 1
        else:
            right -= 1
    return area

heights=[1,8,6,2,5,4,8,3,7]
print(container_with_most_water(heights))