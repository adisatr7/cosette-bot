import constants.responses as responses
from random import randint


def __random_response(responses_list: list[str]) -> str:
    """
    Selects a random response from a list of responses.

    Args:
        responses_list (list[str]): List of responses.

    Returns:
        str: Randomly selected response.
    """
    # Select a random index from the list of responses
    random_index = randint(0, len(responses_list) - 1)

    # Select the response at the random index
    selected_response = responses_list[random_index]

    # Return the selected response
    return selected_response


def come_online() -> str:
    """
    Selects a random greeting to be printed when Cosette comes online.

    Returns:
        str: Randomly selected greeting.
    """
    return __random_response(responses.STARTUP)


def greet() -> str:
    """
    Selects a random greeting to be used **WHEN EXACTLY?**

    Returns:
        str: Randomly selected greeting.
    """
    return __random_response(responses.GREETINGS)


def respond_to_mention() -> str:
    """
    Selects a random response from a list and returns it. Used when Cosette is being mentioned.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.MENTIONED)


def starts_playing_a_song() -> str:
    """
    Selects a random response from a list for when when a user
    starts playing a song for the first time.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.NEW_SONG)


def add_song_to_queue() -> str:
    """
    Selects a random response from a list for when a user starts adding a
    song to the queue while the music player is playing.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.ADD_TO_QUEUE)


def user_not_in_voice_channel() -> str:
    """
    Selects a random response from a list for when a user starts adding a
    song to the queue while the music player is playing.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.USER_NOT_IN_VOICE_CHANNEL)


def no_song_playing() -> str:
    """
    Selects a random response from a list for when a user
    calls a music command but Cosette is not even playing
    anything.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.NO_SONG)


def skip_song() -> str:
    """
    Selects a random response from a list for when Cosette is skipping
    a song to the next queue while the music player is playing.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.SKIPPING_SONGS)


def no_more_songs() -> str:
    """
    Selects a random response from a list for when Cosette is skipping
    a song but there is no more songs in the queue.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.NO_MORE_SONGS)


def pause() -> str:
    """
    Selects a random response from a list for when Cosette is pausing
    a song.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.PAUSING)


def song_already_paused() -> str:
    """
    Selects a random response from a list for when the user calls for
    /pause but the music is already paused.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.SONG_ALREADY_PAUSED)


def resume_song() -> str:
    """
    Selects a random response from a list for when the user
    calls for /resume.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.RESUMING_SONG)


def song_already_resumed() -> str:
    """
    Selects a random response from a list for when the
    user calls for /resume but the music is already resumed.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.SONG_ALREADY_RESUMED)


def leave_vc_mid_performance() -> str:
    """
    Selects a random response from a list for when the
    user calls for /stop command, in which Cosette
    will leave the voice channel.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.LEAVING_VC_MID_PERFORMANCE)


def leave_vc_no_users() -> str:
    """
    Selects a random response from a list for when the
    user calls for /stop command, in which Cosette
    will leave the voice channel because there are no
    users left in the voice channel.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.LEAVING_VC_NO_USERS_LEFT)


def already_stopped() -> str:
    """
    Selects a random response from a list for when the
    user calls for /stop command but Cosette is not even
    in any voice channel.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.ALREADY_STOPPED)


def queue_is_empty() -> str:
    """
    Selects a random response from a list for when the
    user calls for /queue command but the queue is empty.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.QUEUE_IS_EMPTY)


def rolling_dice() -> str:
    """
    Selects a random response from a list for when the
    Cosette is about to roll dice.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.ROLLING)


def get_rick_rolled() -> str:
    """
    Selects a random response from a list for when Cosette
    detects a rick roll.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.RICK_ROLLED)


def move_to_different_vc() -> str:
    """
    Selects a random response from a list for when Cosette
    is about to move to a different voice channel while she's
    already in another voice channel.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.MOVING_TO_DIFFERENT_VC)


def final_song_over() -> str:
    """
    Selects a random response from a list for when Cosette
    is about to move to a different voice channel while she's
    already in another voice channel.

    Returns:
        str: Randomly selected response.
    """
    return __random_response(responses.FINAL_SONG_OVER)
