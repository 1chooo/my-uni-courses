# First through the machine eplison. (HW2-5)

def machineEpsilon() :
    epsilon = 1.0

    while (epsilon > 0) :
        xmin = epsilon
        epsilon = epsilon / 2

    return xmin


def IterMeth(val, es, maxIterator) :
    iter = 1
    sol = val
    ea = 100
    count = 1

    while True :
        preSol = sol
        sol = (sol + (val / sol)) / 2
        iter = iter + 1

        if sol != 0 :
            ea = abs((sol - preSol) / sol) * 100      

        if (ea < es or iter >= maxIterator) :
            break

        print(f"Times: {count}, Root: {sol :.4f}; Approximate relative error: {ea :.4f}%.")

        count += 1

    print("\nThe evaluate root:", sol)

    return sol

print("Machine eplison:", machineEpsilon())
print("What the value of \"a\" we picked up -> 25\n")
print("Start evaluate: ")

IterMeth(25, machineEpsilon(), 100)