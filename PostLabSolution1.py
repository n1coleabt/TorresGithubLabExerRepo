def median(lyst):
    lyst.sort()
    if(len(lyst)%2==0):
        f=lyst[len(lyst) // 2]
        s=lyst[len(lyst) // 2-1]
        m=(f+s)/2
    else:
        m=lyst[len(lyst) // 2]

    return m

def mean(lyst):
    sum_list=sum(lyst)
    return sum_list/len(lyst)

def mode(lyst):
    mode1=max(lyst,key=lyst.count)
    return mode1

    

def main():

    lyst = []

    for i in range(6):

      lyst.append(int(input('Enter a Value for the list: ')))

    print("List:", lyst)

    print("Mode:", mode(lyst))

    print("Median:", median(lyst))

    print("Mean:", mean(lyst))

if __name__ == "__main__":

    main()
