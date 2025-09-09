for _ in range(3):
    lst = list(map(int,input().split()))
    in_hour = lst[0]
    in_min = lst[1]
    in_sec = lst[2]
    out_hour = lst[3]
    out_min = lst[4]
    out_sec = lst[5]
    
    in_total = in_hour * 3600 + in_min * 60 + in_sec
    out_total = out_hour * 3600 + out_min * 60 + out_sec
    
    work_total = out_total - in_total
    
    work_hour = work_total // 3600
    work_min = (work_total % 3600) // 60
    work_sec = (work_total % 3600) % 60
    
    print(work_hour, work_min, work_sec, end=" ")