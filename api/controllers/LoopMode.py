from api.firestore import db
from typing import Literal


class LoopMode:
    def get(self, guild_id: int) -> Literal["off", "single", "all"]:
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
            set(guild_id, "off")

            return "off"

    def set(self, guild_id: int, loop_mode: Literal["off", "single", "all"]) -> None:
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
