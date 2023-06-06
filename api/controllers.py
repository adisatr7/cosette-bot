from api.firestore import db
from typing import Literal


def fetch_guild_ids() -> list[int]:
    """
    Fetches all guilds IDs stored in Firestore.

    Returns:
        list[]: List of guild IDs
    """
    try:
        print("Fetching guild IDs...")
        docs = db.collection("guilds").stream()
        print("Fetched guild IDs successfully!")

        return [doc.id for doc in docs]

    except Exception as e:
        print("Could not fetch guild IDs. Defaulting to empty list...")
        print(e)

        return []


def fetch_command_channel(guild_id: int) -> int:
    """
    Fetches command channel for a guild.

    Returns:
        list[]: List of guild IDs

    Exceptions:
        Exception: If the guild ID does not exist in Firestore
    """
    try:
        print(f"Fetching command channel for guild ID {guild_id}...")
        docs = db.collection("guilds").document(f"{guild_id}").get()
        print("Fetched command channel successfully!")

        return docs.to_dict()["command_channel"]

    except Exception as e:
        print("Error: Could not fetch command channel!")
        print(e)

        return -1


def set_command_channel(guild_id: int, command_channel: int) -> None:
    """
    Sets command channel for a guild.

    Returns:
        None

    Exceptions:
        Exception: If the guild ID does not exist in Firestore
    """
    try:
        print(f"Setting command channel ID {command_channel} for guild ID {guild_id}")
        db.collection("guilds").document(f"{guild_id}").set(
            {"command_channel": command_channel}
        )
        print("Set command channel successfully!")

    except Exception as e:
        print("Could not set command channel...")
        print(e)


def fetch_loop_mode(guild_id: int) -> Literal["off", "single", "all"]:
    """
    Fetches loop mode for a guild.

    Returns:
        Literal["off", "single", "all"]: Loop mode
    """
    try:
        print(f"Fetchhin loop mode for guild {guild_id}...")
        doc = db.collection("guilds").document(f"{guild_id}").get()

        # If the document exists, retrieve the loop mode
        loop_mode = doc.to_dict()["loop_mode"]
        print(f"Detected loop mode: {loop_mode}")

        return loop_mode

    # Exception handling: Set the loop mode to off by default
    except Exception as e:
        print(f"Could not detect loop mode for guild {guild_id}.")
        print(e)
        print("Defaulting to off...")

        return "off"


def set_loop_mode(guild_id: int, loop_mode: Literal["off", "single", "all"]) -> None:
    """
    Sets loop mode for a guild.

    Returns:
        None
    """
    try:
        print(f"Setting loop mode for guild {guild_id}...")
        db.collection("guilds").document(f"{guild_id}").set({"loop_mode": loop_mode})

        print(f"Set loop mode for guild {guild_id} successfully!")

    except Exception as e:
        print(f"Failed to set loop mode for guild {guild_id}...")
        print(e)
