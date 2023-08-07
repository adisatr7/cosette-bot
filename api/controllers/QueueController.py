from firebase_admin.firestore import DELETE_FIELD
from api.firestore import db
from wavelink import YouTubeTrack, Queue


class QueueController:
    def get(self, guild_id: int) -> Queue:
        """
        Retrieves queue for a guild.

        Returns:
            Queue: Queue object
        """

        docs = db.collection("guilds").document(f"{guild_id}").collection("queue").get()

        queue = Queue()

        for doc in docs:
            data = doc.to_dict()
            song = YouTubeTrack(data)
            queue.put(song)

        return queue

    def set(self, guild_id: int, queue: Queue) -> None:
        """
        Sets queue for a guild.

        Returns:
            None
        """
        try:
            queue_list = []

            for song in queue.copy():
                queue_list.append(song.data)

            print(f"Saving queue for guild {guild_id}...")
            db.collection("guilds").document(f"{guild_id}").set(
                {"queue": queue_list},
                merge=True
            )

            print(f"Queue for guild ID {guild_id} has been successfully set!")

        except Exception as e:
            print(f"Failed to set queue for guild {guild_id}!")

    def clear(self, guild_id: int) -> None:
        """
        Clears queue for a guild.

        Returns:
            None
        """
        # try:
        print(f"Clearing queue for guild {guild_id}...")
        db.collection("guilds").document(f"{guild_id}").update({"queue": DELETE_FIELD})

        # except Exception as e:
        #     print(f"Failed to clear queue for guild {guild_id}!")

    # def find(self, guild_id: int, position: int) -> YouTubeTrack:
    #     """
    #     Fetches song from the guild's queue playlist.

    #     Returns:
    #         YouTubeTrack: Song object
    #     """
    #     try:
    #         print(f"Fetching song for guild {guild_id}...")
    #         docs = db.collection("guilds").document(f"{guild_id}").collection("queue").where("position", "==", position).get()

    #         # If the document exists, deserialize it
    #         song_data: dict = docs.to_dict()
    #         song_object: YouTubeTrack = YouTubeTrack(data=song_data)

    #         return song_object

    #     # Exception handling: Set the song to "" by default
    #     except Exception as e:
    #         print(f"Could not detect song for guild {guild_id}.")
    #         print("Defaulting to empty string...")
    #         set(guild_id, "")

    #         return ""

    # def add(self, guild_id: int, song_object: YouTubeTrack) -> None:
    #     """
    #     Adds a song to the last position in the guild's queue playlist.

    #     Returns:
    #         None
    #     """
    #     # Serialize the song object
    #     song_data: dict = song_object.data

    #     # Overrides wavelink's queue position with the correct position from my custom queue
    #     song_data["position"] = self.length(guild_id) + 1

    #     # try:
    #     print(f"Adding song {song_data['info']['title']} to queue for guild {guild_id}...")
    #     db.collection("guilds").document(f"{guild_id}").collection("queue").add(song_data)
    #     print(f"Successfully added song {song_data['info']['title']} to queue for guild {guild_id}!")

    #     # except Exception as e:
    #     #     print(f"Could not add song {song_data['info']['title']} to queue for guild {guild_id}!")

    # def put(self, guild_id: int, song_id: str, position: int) -> None:
    #     """
    #     Sets a song ID at a position in the guild's queue playlist.

    #     Returns:
    #         None
    #     """
    #     try:
    #         print(f"Setting song ID {song_id} at position {position} for guild {guild_id}...")
    #         db.collection("guilds").document(f"{guild_id}").collection("queue").document(f"{position}").set(
    #             {
    #                 "song_id": song_id,
    #                 "position": position
    #             }
    #         )
    #         print(f"Successfully set song ID {song_id} at position {position} for guild {guild_id}!")

    #     except Exception as e:
    #         print(f"Could not set song ID {song_id} at position {position} for guild {guild_id}!")

    # def length(self, guild_id: int) -> int:
    #     """
    #     Fetches the length of the guild's queue playlist.

    #     Returns:
    #         int: Length of the guild's queue playlist
    #     """
    #     try:
    #         print(f"Fetching queue length for guild {guild_id}...")
    #         docs = db.collection("guilds").document(f"{guild_id}").collection("queue").get()

    #         return len(docs)

    #     except Exception as e:
    #         print(f"Could not fetch queue length for guild {guild_id}!")
    #         return 0

    # def clear(self, guild_id: int) -> None:
    #     """
    #     Clears the guild's queue playlist.

    #     Returns:
    #         None
    #     """
    #     try:
    #         print(f"Clearing queue for guild {guild_id}...")
    #         docs = db.collection("guilds").document(f"{guild_id}").collection("queue").get()

    #         for doc in docs:
    #             doc.reference.delete()

    #         print(f"Successfully cleared queue for guild {guild_id}!")

    #     except Exception as e:
    #         print(f"Could not clear queue for guild {guild_id}!")
