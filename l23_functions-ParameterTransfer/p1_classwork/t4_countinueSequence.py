def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)
        # doing sequence + sequence just makes a copy instead of actually changing the array
