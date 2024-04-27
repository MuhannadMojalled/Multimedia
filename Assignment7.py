from jes4py import *


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


# Load the sound file
filename = pickAFile()
sound = makeSound(filename)

# Define the size of the maximum filter window
window_size = 10  # Adjust as needed

# Apply maximum filter
filtered_sound_max = apply_maximum_filter(sound, window_size)
# Play the sound
blockingPlay(filtered_sound_max)

# Apply Minimum filter
filtered_sound_min = apply_maximum_filter(sound, window_size)
# Play the sound
blockingPlay(filtered_sound_min)
