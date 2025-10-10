predictions = list(map(str,input().split()))
A = predictions.count("A")
B = predictions.count("B")
A_in_percentage = A/len(predictions)*100
B_in_percentage = B/len(predictions)*100

if A_in_percentage > 70 or B_in_percentage > 70:
    print("Biased Model")
else:
    print("Fair Model")