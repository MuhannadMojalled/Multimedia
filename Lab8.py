from jes4py import *


# filename = pickAFile()
# aSound = makeSound(filename)
# print(aSound)
# blockingPlay(aSound)


def increaseVolume(sound):
    for sample in getSamples(sound):
        value = getSampleValue(sample)
        setSampleValue(sample, value * 2)


def increaseVolumeByRange(sound):
    for sampleIndex in range(0, getLength(sound)):
        value = getSampleValueAt(sound, sampleIndex)
        setSampleValueAt(sound, sampleIndex, value * 10)


def normalize(sound):
    largest = 0
    for s in getSamples(sound):
        largest = max(largest, getSampleValue(s))
    multiplier = 32767.0 / largest
    print("Largest sample value in original sound was", largest)
    print("Multiplier is", multiplier)
    for s in getSamples(sound):
        louder = multiplier * getSampleValue(s)
        setSampleValue(s, louder)


def merge():
    filename = pickAFile()
    aSound = makeSound(filename)
    filename2 = pickAFile()
    bSound = makeSound(filename2)
    target = makeEmptySoundBySeconds(20)
    index = 0

    for source in range(0, getLength(aSound)):
        value = getSampleValueAt(aSound, source)
        setSampleValueAt(target, index, value)
        index = index + 1

    # Copy in 0.1 second pause (silence) (0)
    for source in range(0, int(2 * getSamplingRate(target))):
        setSampleValueAt(target, index, 0)
        index = index + 1

    for source in range(0, getLength(bSound)):
        value = getSampleValueAt(bSound, source)
        setSampleValueAt(target, index, value)
        index = index + 1
    blockingPlay(target)


def apply_maximum_filter(sound, window_size):
    # Get the number of samples in the sound
    length = getNumSamples(sound)
    # Create a new sound object to store the filtered result
    filtered_sound = makeEmptySound(length)

    # Apply maximum filter
    for i in range(length):
        # Define the window range
        start = max(0, i - window_size // 2)
        end = min(length - 1, i + window_size // 2)

        # Apply maximum filter within the window
        max_sample = max(getSampleValueAt(sound, j) for j in range(start, end + 1))
        # Set the filtered sample value
        setSampleValueAt(filtered_sound, i, max_sample)

    return filtered_sound


def apply_minimum_filter(sound, window_size):
    # Get the number of samples in the sound
    length = getNumSamples(sound)
    # Create a new sound object to store the filtered result
    filtered_sound = makeEmptySound(length)

    # Apply minimum filter
    for i in range(length):
        # Define the window range
        start = max(0, i - window_size // 2)
        end = min(length - 1, i + window_size // 2)

        # Apply minimum filter within the window
        min_sample = min(getSampleValueAt(sound, j) for j in range(start, end + 1))
        # Set the filtered sample value
        setSampleValueAt(filtered_sound, i, min_sample)

    return filtered_sound


def add_sounds(sound1, sound2):
    # Get the number of samples in the sounds
    length1 = getNumSamples(sound1)
    print(length1)
    length2 = getNumSamples(sound2)
    print(length2)

    # use the larger one as a length for the output
    if length1 > length2:
        length = length1
    else:
        length = length2

    # Create a new sound object to store the output result
    output = makeEmptySound(length)

    # add the two
    for i in range(length):
        if length1 > i and length2 > i:
            sample = getSampleValueAt(sound1, i) + getSampleValueAt(sound2, i)
        elif length1 > i and length2 < i:
            sample = getSampleValueAt(sound1, i)
        elif length1 < i and length2 > i:
            sample = getSampleValueAt(sound2, i)
        setSampleValueAt(output, i, sample)

    return output


# Load the sound file
filename1 = pickAFile()
sound1 = makeSound(filename1)
filename2 = pickAFile()
sound2 = makeSound(filename2)
sound = add_sounds(sound1, sound2)
blockingPlay(sound)


# Define the size of the maximum filter window
# window_size = 3  # Adjust as needed

# # Apply maximum filter
# filtered_sound = apply_maximum_filter(sound, window_size)
# filtered_sound2 = apply_maximum_filter(sound, window_size)
# # Save the filtered sound to a new file
# writeSoundTo(filtered_sound, "filtered_sound.wav")
# s = makeSound("filtered_sound.wav")
# blockingPlay(s)
# writeSoundTo(filtered_sound, "filtered_sound2.wav")
# s2 = makeSound("filtered_sound2.wav")
# blockingPlay(s2)
# increaseVolumeByRange(aSound)
# blockingPlay(aSound)
# normalize(aSound)
# blockingPlay(aSound)
# merge()
