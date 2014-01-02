import sys
import numpy

def dft(signal):
    N = len(signal)
    spectrum = numpy.zeros(N, dtype=numpy.complex)
    for k in xrange(N):
        for n in xrange(N):
            spectrum[k] += signal[n]*numpy.exp(-2j * numpy.pi * n * k / N)

    return spectrum/numpy.sqrt(N)

if __name__ == '__main__':
    signal = []
    with open(sys.argv[1],'r') as infile:
        for point in infile:
            if len(point.split()):
                signal.append([float(n) for n in point.split()])

    signal = numpy.array(signal)
    signal[0] = numpy.mean((signal[0],signal[-1]))
    spectrum = dft(signal[:,1])
    print spectrum
