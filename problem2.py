def tower_of_hanoi(pnum, psource, pauxiliary, ptarget):
    if pnum == 1:
        print(f"Move disk 1 from {psource} to {ptarget}")
        return
    tower_of_hanoi(pnum-1, psource, ptarget, pauxiliary)
    print(f"Move disk {pnum} from {psource} to {ptarget}")
    tower_of_hanoi(pnum-1, pauxiliary, psource, ptarget)

pnumber = int(input("Enter number of disks: "))
print("The sequence of moves is:")
tower_of_hanoi(pnumber, "A", "B", "C")
