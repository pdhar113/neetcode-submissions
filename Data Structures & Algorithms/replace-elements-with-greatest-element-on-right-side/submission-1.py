class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #initial max=-1
        #rev iterate
        #new max= max(oldmax, arr[i])

        
        rightMax = -1
        for i in range(len(arr)-1,-1, -1):
            old = arr[i]
            arr[i] = rightMax
            if old>rightMax:
                rightMax = old
        return arr