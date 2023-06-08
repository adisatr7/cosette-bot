from api.firestore import db


class ActiveChannel:
    def get(self, guild_id: int) -> int:
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
            self.set(guild_id, -1)

            return -1

    def set(self, guild_id: int, active_channel: int) -> None:
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
            