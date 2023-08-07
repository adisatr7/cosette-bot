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
    Selects a random response from a list for when when a user
    starts playing a song for the first time.

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


def user_not_in_voice_channel() -> str:
    """
    Selects a random response from a list for when a user starts adding a
    song to the queue while the music player is playing.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.USER_NOT_IN_VOICE_CHANNEL) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.USER_NOT_IN_VOICE_CHANNEL[random_index]

    return selected_response


def no_song_playing() -> str:
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


def song_already_paused() -> str:
    """
    Selects a random response from a list for when the user calls for
    /pause but the music is already paused.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.SONG_ALREADY_PAUSED) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.SONG_ALREADY_PAUSED[random_index]

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


def song_already_resumed() -> str:
    """
    Selects a random response from a list for when the
    user calls for /resume but the music is already resumed.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.SONG_ALREADY_RESUMED) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.SONG_ALREADY_RESUMED[random_index]

    return selected_response


def leave_vc_mid_performance() -> str:
    """
    Selects a random response from a list for when the
    user calls for /stop command, in which Cosette
    will leave the voice channel.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.LEAVING_VC_MID_PERFORMANCE) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.LEAVING_VC_MID_PERFORMANCE[random_index]

    return selected_response


def leave_vc_no_users() -> str:
    """
    Selects a random response from a list for when the
    user calls for /stop command, in which Cosette
    will leave the voice channel because there are no
    users left in the voice channel.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(
        0, len(responses.LEAVING_VC_NO_USERS_LEFT) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.LEAVING_VC_NO_USERS_LEFT[random_index]

    return selected_response


def already_stopped():
    """
    Selects a random response from a list for when the
    user calls for /stop command but Cosette is not even
    in any voice channel.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.ALREADY_STOPPED) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.ALREADY_STOPPED[random_index]

    return selected_response


def queue_is_empty() -> str:
    """
    Selects a random response from a list for when the
    user calls for /queue command but the queue is empty.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.QUEUE_IS_EMPTY) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.QUEUE_IS_EMPTY[random_index]

    return selected_response


def rolling_dice() -> str:
    """
    Selects a random response from a list for when the
    Cosette is about to roll dice.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.ROLLING) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.ROLLING[random_index]

    return selected_response


def get_rick_rolled() -> str:
    """
    Selects a random response from a list for when Cosette
    detects a rick roll.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.RICK_ROLLED) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.RICK_ROLLED[random_index]

    return selected_response


def move_to_different_vc() -> str:
    """
    Selects a random response from a list for when Cosette
    is about to move to a different voice channel while she's
    already in another voice channel.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.MOVING_TO_DIFFERENT_VC) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.MOVING_TO_DIFFERENT_VC[random_index]

    return selected_response

def final_song_over() -> str:
    """
    Selects a random response from a list for when Cosette
    is about to move to a different voice channel while she's
    already in another voice channel.

    Returns:
        str: Randomly selected response.
    """

    # Select a random index within the range of responses list
    random_index = randint(0, len(responses.FINAL_SONG_OVER) - 1)

    # Retrieve the greeting at the random index
    selected_response = responses.FINAL_SONG_OVER[random_index]

    return selected_response
