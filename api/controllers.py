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

        return []


def fetch_active_channel(guild_id: int) -> int:
    """
    Fetches active channel for a guild.

    Returns:
        list[]: List of guild IDs

    Exceptions:
        Exception: If the guild ID does not exist in Firestore
    """
    try:
        print(f"Fetching active channel for guild ID {guild_id}...")
        docs = db.collection("guilds").document(f"{guild_id}").get()
        print("Fetched active channel successfully!")

        return docs.to_dict()["active_channel"]

    except Exception as e:
        print("Error: Could not fetch active channel!")
        set_active_channel(guild_id, -1)

        return -1


def set_active_channel(guild_id: int, active_channel: int) -> None:
    """
    Sets active channel for a guild.

    Returns:
        None

    Exceptions:
        Exception: If the guild ID does not exist in Firestore
    """
    try:
        print(f"Setting active channel ID {active_channel} for guild ID {guild_id}")
        db.collection("guilds").document(f"{guild_id}").set(
            {"active_channel": active_channel},
            merge=True
        )
        print(f"Successfully set up channel ID {active_channel} as active channel!")

    except Exception as e:
        print("Could not set active channel...")


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
        print("Defaulting to off...")
        set_loop_mode(guild_id, "off")

        return "off"


def set_loop_mode(guild_id: int, loop_mode: Literal["off", "single", "all"]) -> None:
    """
    Sets loop mode for a guild.

    Returns:
        None
    """
    try:
        print(f"Setting loop mode for guild {guild_id}...")
        db.collection("guilds").document(f"{guild_id}").set(
            {"loop_mode": loop_mode},
            merge=True
        )

        print(f"Loop mode for guild Id {guild_id} has been successfully set to {loop_mode}!")

    except Exception as e:
        print(f"Failed to set loop mode for guild {guild_id}!")


def fetch_message_id_with_buttons(guild_id: int) -> tuple[int, int]:
    """
    Fetches message ID for a guild.

    Returns:
        int: Message ID
    """
    try:
        print(f"Fetching for message ID for guild {guild_id} where the player buttons are attached to...")
        doc = db.collection("guilds").document(f"{guild_id}").get()

        # If the document exists, retrieve the message ID
        message_id: int = doc.to_dict()["message_id_with_buttons"]

        # Also retrieve the active channel
        active_channel: int = doc.to_dict()["active_channel"]

        # Console log the success message
        print(f"Player buttons are attached to message ID {message_id} in channel ID {active_channel}!")

        return message_id, active_channel

    # Exception handling: Set the message ID to -1 by default
    except Exception as e:
        print(f"Could not detect message ID for guild {guild_id}!")

        return -1


def set_message_id_with_buttons(guild_id: int, message_id: int) -> None:
    """
    Sets message ID for a guild.

    Returns:
        None
    """
    try:
        print(f"Attaching player buttons to a message somewhere in guild ID {guild_id}...")
        db.collection("guilds").document(f"{guild_id}").set(
            {"message_id_with_buttons": message_id},
            merge=True
        )

        print(f"Player buttons for guild ID {guild_id} have been sucessfully attached to message ID {message_id}!")

    except Exception as e:
        print(f"Failed to set message ID for guild {guild_id}!")


def clear_message_id_with_buttons(guild_id: int) -> None:
    """
    Clears message ID for a guild.

    Returns:
        None
    """
    try:
        print(f"Clearing message ID where the player buttons are for guild {guild_id}...")
        db.collection("guilds").document(f"{guild_id}").set(
            {"message_id_with_buttons": 0},
            merge=True
        )

        print(f"Cleared! Player buttons for guild ID {guild_id} are no longer attached to any message!")

    except Exception as e:
        print(f"Failed to clear message ID where player buttons are for guild ID {guild_id}!")
