from api.firestore import db


class MessageButtons:
    def get(self, guild_id: int) -> tuple[int, int]:
        """
        Fetches message ID for a guild.

        Returns:
            tuple[int, int]: Message ID and active channel
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

    def set(self, guild_id: int, message_id: int) -> None:
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

    def clear(self, guild_id: int) -> None:
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
