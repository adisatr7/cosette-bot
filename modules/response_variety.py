import constants.responses as responses
from random import randint


def come_online() -> str:
    """
    Selects a random greeting to be printed when Cosette comes online.

    Returns:
        str: Randomly selected greeting.
    """

    # Select a random index within the range of greetings list
    random_index = randint(0, len(responses.STARTUP) - 1)

    # Retrieve the greeting at the random index
    selected_greeting = responses.STARTUP[random_index]

    return selected_greeting


def greet() -> str:
    """
    Selects a random greeting to be used **WHEN EXACTLY?**

    Returns:
        str: Randomly selected greeting.
    """

    # Select a random index within the range of greetings list
    random_index = randint(0, len(responses.GREETINGS) - 1)

    # Retrieve the greeting at the random index
    selected_greeting = responses.GREETINGS[random_index]

    return selected_greeting


def respond_to_mention() -> str:
    """
    Selects a random response from a list and returns it. Used when Cosette is being mentioned.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.MENTIONED) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.MENTIONED[random_index]

    return selected_response

def starts_playing_a_song() -> str:
    """
    Selects a random response from a list for when when a user starts playing a 
    song for the first time.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.NEW_SONG) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.NEW_SONG[random_index]

    return selected_response


def add_song_to_queue() -> str:
    """
    Selects a random response from a list for when a user starts adding a
    song to the queue while the music player is playing.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.ADD_TO_QUEUE) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.ADD_TO_QUEUE[random_index]

    return selected_response


def no_song() -> str:
    """
    Selects a random response from a list for when a user
    calls a music command but Cosette is not even playing
    anything.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.NO_SONG) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.NO_SONG[random_index]

    return selected_response


def skip_song() -> str:
    """
    Selects a random response from a list for when Cosette is skipping
    a song to the next queue while the music player is playing.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.SKIPPING_SONGS) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.SKIPPING_SONGS[random_index]

    return selected_response


def no_more_songs() -> str:
    """
    Selects a random response from a list for when Cosette is skipping
    a song but there is no more songs in the queue.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.NO_MORE_SONGS) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.NO_MORE_SONGS[random_index]

    return selected_response


def pause() -> str:
    """
    Selects a random response from a list for when Cosette is pausing
    a song.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.PAUSING) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.PAUSING[random_index]

    return selected_response


def music_already_paused() -> str:
    """
    Selects a random response from a list for when the user calls for
    /pause but the music is already paused.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.MUSIC_ALREADY_PAUSED) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.MUSIC_ALREADY_PAUSED[random_index]

    return selected_response


def resume_song() -> str:
    """
    Selects a random response from a list for when the user
    calls for /resume.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.RESUMING_SONG) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.RESUMING_SONG[random_index]

    return selected_response


def already_resumed() -> str:
    """
    Selects a random response from a list for when the user
    calls for /resume but the music is already resumed.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.RESUMING_SONG) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.RESUMING_SONG[random_index]

    return selected_response
