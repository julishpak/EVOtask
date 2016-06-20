import numpy


array = numpy.random.randint(0, 9, (10, 10, 10))
result = 0


def columns_sum(x, y, z):
    sum_x, sum_y, sum_z = 0, 0, 0

    for i in xrange(10):
        sum_x += array[i, y, z]
        sum_y += array[x, i, z]
        sum_z += array[x, y, i]
    return sum_x + sum_y + sum_z - array[x, y, z]*2

for i in xrange(10):
    for j in xrange(10):
        for k in xrange(10):
            sum = columns_sum(i, j, k)

            if sum > result:
                result = sum


print array
print result
