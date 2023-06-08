import api
import wavelink
from wavelink import Playable, Player


def add_to_queue(guild_id: int, track: Playable, player: Player):
    """
    Adds a song to the guild's queue playlist.

    Returns:
        None
    """
    try:
        song_id: str = track.identifier

    except Exception as e:
        print(f"Could not add song {track.title} to queue for guild {guild_id}!")
