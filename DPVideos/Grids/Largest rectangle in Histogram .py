# Solution 

# Solution
# 1. We have to find largest rectangle including each bar one by one
# 2. Take maximum of all the max areas for each bar
# 
# For 1st we need to find the nearest left bar with height less than the current index
# and also the nearest right bar with height less than the current index
# and width = right - left +1
# https://www.youtube.com/watch?v=vcv3REtIvEo&list=PLEJXowNB4kPxBwaXtRO1qFLpCzF75DYrS&index=37

# We need to know index of the first smaller (smaller than ‘x’) bar on left of ‘x’ and index of first smaller bar on right of ‘x’. Let us call these indexes as ‘left index’ and ‘right index’ respectively. 
# We traverse all bars from left to right, maintain a stack of bars. Every bar is pushed to stack once. A bar is popped from stack when a bar of smaller height is seen. When a bar is popped, we calculate the area with the popped bar as smallest bar. How do we get left and right indexes of the popped bar – the current index tells us the ‘right index’ and index of previous item in stack is the ‘left index’. Following is the complete algorithm.
# 1) Create an empty stack.
# 2) Start from first bar, and do following for every bar ‘hist[i]’ where ‘i’ varies from 0 to n-1. 
# ……a) If stack is empty or hist[i] is higher than the bar at top of stack, then push ‘i’ to stack. 
# ……b) If this bar is smaller than the top of stack, then keep removing the top of stack while top of the stack is greater. Let the removed bar be hist[tp]. Calculate area of rectangle with hist[tp] as smallest bar. For hist[tp], the ‘left index’ is previous (previous to tp) item in stack and ‘right index’ is ‘i’ (current index).
# 3) If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar.


# int largest_rectangle(vector<int> buildings) {
#     int n = buildings.size();
#     // initalize max area to zero
#     int max_area = 0;
    
#     // iterate through all buildings
#     for(int i=0; i<n; i++) {
#         // current building
#         int current_building = buildings[i];
        
#         // adjacent buildings in left with same or greater height
#         int left_buildings = 0;
#         for(int j=i-1; j>=0; j--) {
#             if(current_building <= buildings[j])
#                 left_buildings++;
#             else break;
#         }
        
#         // adjacent buildings in right with same or greater height
#         int right_buildings = 0;
#         for(int j=i+1; j<n; j++) {
#             if(current_building <= buildings[j])
#                 right_buildings++;
#             else break;
#         }
        
#         // area will be total no of continuous buildings x current building height
#         // total buildings = left buildings + right buildings + 1 (for current building)
#         int area = (left_buildings + right_buildings + 1)*current_building;
        
#         // update max
#         max_area = max(area, max_area);
#     }
#     return max_area;
# }

#O(n^2)

def oneStack(heights):
        i = 0
        maxi = -1
        st = []
        heights.append(-1)
        for i in range(len(heights)):
            if len(st) > 0 and heights[i] <= heights[st[-1]]:
                while len(st) > 0 and heights[st[-1]] >= heights[i]:
                    temp = st.pop()
                    maxi = max(maxi, heights[temp] * (i if len(st) == 0 else (i - st[-1] - 1)))
            st.append(i)

        return maxi


def twoArraySolution( height ):
    n = len(height)
    prevSmall = getPrevSmall(height)
    nextSmall = getNextSmall(height)

    maxArea = 0
    for i in range(n):
        currArea = (nextSmall[i] - prevSmall[i] -1) * height[i]
        maxArea = max(maxArea , currArea)
    print(maxArea)

def getPrevSmall(height):
    stack = []
    prevSmall = [0]*len(height) 

    for i in range(len(height)):
        while stack and height[stack[-1]] >= height[i]:
            stack.pop()
        if not stack:      
            prevSmall[i] = 0
        else:
            prevSmall[i] = stack[-1]
        
        stack.append(i)
    return prevSmall

def getNextSmall( height ):
    stack = []
    nextSmall = [0]*len(height)

    for i in range(len(height) -1 , -1 , -1):
        while stack and height[stack[-1]] >= height[i]:
            stack.pop()
        if not stack:
            nextSmall[i] = len(height)
        else:
            nextSmall[i] = stack[-1]
        
        stack.append(i)
    return nextSmall    


arr = [ 2 , 1, 5 , 6 , 2 , 3] 

# oneStack(arr)
(twoArraySolution(arr))


# One pass https://www.youtube.com/watch?v=jC_cWLy7jSI&t=593s


    

