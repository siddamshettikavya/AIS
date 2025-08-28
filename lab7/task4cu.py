def compute_ratios(values):
    results=[]
    for i in range(len(values)):
        for j in range(len(values)):
            if i!=j:
                if values[j]!=0:
                    results.append(values[i]/ values[j])
                else:
                    results.append(float('inf'))
    return results
nums=[5,10,15,20,25]
print(compute_ratios(nums))
