from random import randint
from constants.responses import STARTUP_MESSAGES, GREETINGS, MENTION_RESPONSES


def come_online() -> str:
    """
    Selects a random greeting to be printed when Cosette comes online.

    Returns:
        str: Randomly selected greeting.
    """

    # Select a random index within the range of greetings list
    random_index = randint(0, len(STARTUP_MESSAGES) - 1)

    # Retrieve the greeting at the random index
    selected_greeting = STARTUP_MESSAGES[random_index]

    return selected_greeting


def greet() -> str:
    """
    Selects a random greeting to be used **WHEN EXACTLY?**

    Returns:
        str: Randomly selected greeting.
    """

    # Select a random index within the range of greetings list
    random_index = randint(0, len(GREETINGS) - 1)

    # Retrieve the greeting at the random index
    selected_greeting = GREETINGS[random_index]

    return selected_greeting


def respond_to_mention() -> str:
    """
    Selects a random response from a list and returns it. Used when Cosette is being mentioned.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(MENTION_RESPONSES) - 1)

    # Retrieve the greeting at the random index
    selected_response = MENTION_RESPONSES[random_index]

    return selected_response
