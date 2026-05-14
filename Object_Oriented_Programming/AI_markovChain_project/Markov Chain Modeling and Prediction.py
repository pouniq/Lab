# Instructions:
# - Complete only the TODO sections.
# - Do not change function names or input/output formats.
# - You may use numpy functions where needed.
# - Your code should run directly by executing this file.
# - Keep the program structure unchanged.
import numpy as np

STATES = ["Sunny", "Cloudy", "Rainy"]

OBSERVED_SEQUENCE = [
    "Sunny", "Sunny", "Cloudy", "Sunny", "Rainy", "Cloudy", "Cloudy", "Sunny",
    "Sunny", "Sunny", "Cloudy", "Rainy", "Cloudy", "Sunny", "Cloudy", "Cloudy",
    "Rainy", "Rainy", "Cloudy", "Sunny", "Sunny", "Cloudy", "Cloudy", "Cloudy",
    "Rainy", "Cloudy", "Sunny", "Sunny", "Rainy", "Cloudy", "Sunny", "Sunny",
    "Cloudy", "Rainy", "Cloudy", "Sunny", "Cloudy", "Cloudy", "Sunny", "Rainy"
]


def create_state_index(states):
    """
    Create a mapping from state name to integer index.
    Example:
        {"Sunny": 0, "Cloudy": 1, "Rainy": 2}
    """
    return {state: i for i, state in enumerate(states)}


def normalize_rows(matrix):
    """
    Normalize each row so that row sums become 1.
    """
    row_sums = matrix.sum(axis=1, keepdims=True)
    return matrix / row_sums


def build_transition_matrix(states, sequence):
    """
    Build a transition matrix from an observed sequence.

    Steps:
    1. Count transitions between consecutive states
    2. Normalize the count matrix row-wise

    Returns:
        transition_matrix: numpy array of shape (n_states, n_states)
    """
    n_states = len(states)
    state_to_idx = create_state_index(states)

    counts = np.zeros((n_states, n_states), dtype=float)

    # TODO 1:
    # Fill the counts matrix using the observed sequence.
    # counts[i, j] should store how many times state i is followed by state j.
    for current, next_one in zip(sequence[:-1], sequence[1:]):
        i = state_to_idx[current]
        j = state_to_idx[next_one]
        counts[i,j] = counts[i,j] + 1

    # TODO 2:
    # Convert the counts matrix into a probability transition matrix
    # by normalizing each row.
    counts = normalize_rows(counts)

    transition_matrix = counts  # replace this line
    return transition_matrix


def get_initial_distribution(states, current_state):
    """
    Create a one-hot probability distribution for the current state.
    Example:
        current_state = "Cloudy"
        output = [0, 1, 0]
    """
    distribution = np.zeros(len(states))
    idx = create_state_index(states)[current_state]
    distribution[idx] = 1.0
    return distribution


def predict_n_steps(initial_distribution, transition_matrix, n):
    """
    Predict the state distribution after n steps.

    Formula:
        p_n = p_0 @ (T^n)

    Returns:
        numpy array representing the probability distribution after n steps
    """

    # TODO 3:
    # Compute T^n using numpy
    transition_power = np.linalg.matrix_power(transition_matrix, n)
    

    # TODO 4:
    # Compute the predicted distribution after n step
    predicted_distribution = initial_distribution @ transition_power # replace this line
    return predicted_distribution


def sample_next_state(states, probs):
    """
    Sample the next state using the probability vector `probs`.
    """
    # TODO 5:
    # Return one state sampled according to probs
    return np.random.choice(states, p=probs)



def simulate_sequence(states, transition_matrix, start_state, num_steps):
    """
    Simulate a sequence of states using the Markov chain.

    Args:
        states: list of possible states
        transition_matrix: row-stochastic transition matrix
        start_state: starting state as string
        num_steps: number of transitions to simulate

    Returns:
        list of visited states, including the start state
    """
    state_to_idx = create_state_index(states)
    current_state = start_state
    simulated = [current_state]

    # TODO 6:
    # Repeatedly sample the next state using the current state's row
    # in the transition matrix, then update current_state.
    
    for _ in range(num_steps):
        current_index = state_to_idx[current_state]
        next_one_prob = transition_matrix[current_index]
        next_one_state = sample_next_state(states, next_one_prob)
        
        simulated.append(str(next_one_state))
        current_state = next_one_state
    

    return simulated


def estimate_stationary_distribution(transition_matrix, num_iterations=100):
    """
    Estimate the stationary distribution using power iteration.

    Start from a uniform distribution and repeatedly multiply by T.

    Returns:
        numpy array representing the estimated stationary distribution
    """
    n_states = transition_matrix.shape[0]
    distribution = np.ones(n_states) / n_states

    # TODO 7:
    # Repeatedly update the distribution using:
    # distribution = distribution @ transition_matrix
    for _ in range(num_iterations):
       distribution = distribution @ transition_matrix 

    return distribution


def print_distribution(states, distribution, title):
    """
    Print a probability distribution in a readable format.
    """
    print(title)
    for state, prob in zip(states, distribution):
        print(f"{state}: {prob:.4f}")
    print()


def main():
    transition_matrix = build_transition_matrix(STATES, OBSERVED_SEQUENCE)

    print("Transition Matrix:")
    print(np.round(transition_matrix, 4))
    print()

    current_state = "Cloudy"
    initial_distribution = get_initial_distribution(STATES, current_state)

    for n in [1, 2, 5]:
        predicted = predict_n_steps(initial_distribution, transition_matrix, n)
        print_distribution(STATES, predicted, f"Predicted distribution after {n} step(s):")

    simulated_sequence = simulate_sequence(
        STATES,
        transition_matrix,
        start_state="Sunny",
        num_steps=15
    )
    print("Simulated sequence:")
    print(simulated_sequence)
    print()

    stationary = estimate_stationary_distribution(transition_matrix, num_iterations=200)
    print_distribution(STATES, stationary, "Estimated stationary distribution:")


if __name__ == "__main__":
    main()
