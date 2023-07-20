
num = int(input("Enter number of tasks: "))
arival_time  = {"Name":[],"Arrival Time":[],"Burst Time":[], "Completition Time":[], "TAT":[],"Waiting Time":[]}
for i in range(num):
	arival_time["Name"].append(f"P{i}")
	arival_time["Arrival Time"].append(int(input(f"Enter arival time of task P{i}: ")))
	arival_time["Burst Time"].append(int(input(f"Enter Burst time of task P{i}: ")))
	            
def bubbleSort(arr,arr2,arr3):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
                arr3[j], arr3[j+1] = arr3[j+1], arr3[j]
                swapped = True
        if (swapped == False):
            break
           
bubbleSort(arival_time["Arrival Time"],arival_time["Name"],arival_time["Burst Time"])
#print(arival_time)
completion_time = 0
for i in range(len(arival_time["Arrival Time"])):
	completion_time += arival_time["Burst Time"][i]
	arival_time["Completition Time"].append(completion_time)

for i in range(num):
	TAT = 0
	WT = 0
	TAT = arival_time["Completition Time"][i] - arival_time["Arrival Time"][i]
	arival_time["TAT"].append(TAT)
	WT = arival_time["TAT"][i] - arival_time["Burst Time"][i]
	arival_time["Waiting Time"].append(WT)

for key, value in arival_time.items():
    print(f'{key: <20}{value}')













