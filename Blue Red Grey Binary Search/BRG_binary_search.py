def BRG_binary_search(arr,tgt):
    blue,red = -1,len(arr)
    def is_blue():
        # TBD
    while blue+1 != red:
        grey = (blue+red) // 2
        if is_blue(arr[grey]):
            blue = grey
        else:
            red = grey
    # TBD
    return 
# blue,red has to be initialized as -1 and len(arr) due to otherwise we are putting uncatagorized elements [0] into blue and [len(arr)-1] into red
# is_blue determines if an element should be in blue team or red team
# return value is determined in specific case, blue or red.
