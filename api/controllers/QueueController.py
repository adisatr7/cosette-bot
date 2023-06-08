import api
from api.firestore import db


class QueueController:
    def get_song_id(self, guild_id: int, position: int) -> str:
        """
        Fetches song from the guild's queue playlist.

        Returns:
            str: wavelink.Playable base64 id
        """
        try:
            print(f"Fetching song for guild {guild_id}...")
            docs = db.collection("guilds").document(f"{guild_id}").collection("queue").where("position", "==", position).get()

            # If the document exists, the document ID is the song ID
            song_id = docs[0].id

            return song_id

        # Exception handling: Set the song to "" by default
        except Exception as e:
            print(f"Could not detect song for guild {guild_id}.")
            print("Defaulting to empty string...")
            set(guild_id, "")

            return ""

    def add_song_id(self, guild_id: int, song_id: str) -> None:
        """
        Adds a song ID to the guild's queue playlist.

        Returns:
            None
        """
        try:
            print(f"Adding song ID {song_id} to queue for guild {guild_id}...")
            db.collection("guilds").document(f"{guild_id}").collection("queue").add(
                {
                    "song_id": song_id,
                    "position": self.length(guild_id) + 1
                }
            )
            print(f"Successfully added song ID {song_id} to queue for guild {guild_id}!")

        except Exception as e:
            print(f"Could not add song ID {song_id} to queue for guild {guild_id}!")

    def length(self, guild_id: int) -> int:
        """
        Fetches the length of the guild's queue playlist.

        Returns:
            int: Length of the guild's queue playlist
        """
        try:
            print(f"Fetching queue length for guild {guild_id}...")
            docs = db.collection("guilds").document(f"{guild_id}").collection("queue").get()

            return len(docs)

        except Exception as e:
            print(f"Could not fetch queue length for guild {guild_id}!")
            return 0

    def set_song_id_at_position(self, guild_id: int, song_id: str, position: int) -> None:
        """
        Sets a song ID at a position in the guild's queue playlist.

        Returns:
            None
        """
        try:
            print(f"Setting song ID {song_id} at position {position} for guild {guild_id}...")
            db.collection("guilds").document(f"{guild_id}").collection("queue").document(f"{position}").set(
                {
                    "song_id": song_id,
                    "position": position
                }
            )
            print(f"Successfully set song ID {song_id} at position {position} for guild {guild_id}!")

        except Exception as e:
            print(f"Could not set song ID {song_id} at position {position} for guild {guild_id}!")

    def clear(self, guild_id: int) -> None:
        """
        Clears the guild's queue playlist.

        Returns:
            None
        """
        try:
            print(f"Clearing queue for guild {guild_id}...")
            docs = db.collection("guilds").document(f"{guild_id}").collection("queue").get()

            for doc in docs:
                doc.reference.delete()

            print(f"Successfully cleared queue for guild {guild_id}!")

        except Exception as e:
            print(f"Could not clear queue for guild {guild_id}!")
