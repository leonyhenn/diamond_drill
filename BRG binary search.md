# BRG Binary Search
## [Video Link](https://drive.google.com/file/d/12m8M-i_vebhd132fiIXGSFcqY7oyF2J2/view?usp=drive_link)
## Psudo Code
```
def BRG_binary_search(arr,tgt):
    b,r = -1,len(arr)
    def is_b():
        # something to distinguish the boundary
    while b+1 != r:
        g = (b+r) // 2
        if is_b(arr[g]):
            b = g
        else:
            r = g
    return 

```
## Return Value
1. if all array is blue, the red value will be len(array)
2. if all array is red, the blue value will be -1
3. so boundary check for both sides is still necessary