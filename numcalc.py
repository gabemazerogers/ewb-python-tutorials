def mean(numbers):
        numsum=0
        for i in numbers:
                numsum=numsum+i
        return numsum/len(numbers)

def median(numbers):
        numbers.sort();
        length = len(numbers)
        middle=length/2
        if length%2 == 0:
                return str(numbers[middle-1]) + " and " + str(numbers[middle])
        else:
                return numbers[middle]

def mode(numbers):
        highest=0
        for i in numbers:
                if numbers.count(i) > numbers.count(highest):
                        highest = i

        return highest

raw_numbers = raw_input("Enter you numbers, separated by a space\n: ");
numbers = map(int,raw_numbers.split());
print "Mean:   ", mean(numbers);
print "Median: ", median(numbers);
print "Mode:   ", mode(numbers);
