def towersofhanoi(no_disk, start_rod =1 , end_rod = 3):
    print(no_disk,start_rod,end_rod)

    if no_disk:
        towersofhanoi(no_disk-1 ,start_rod, 6-start_rod-end_rod)
        towersofhanoi(no_disk-1,6-start_rod-end_rod, end_rod)
print(towersofhanoi(no_disk = 2))