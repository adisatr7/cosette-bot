from typing import List


# List of greetings that are printed to console when Cosette comes online
STARTUP: List[str] = [
    "Meow! Cosette is here and ready to play! 😺",
    "Hello, lovely humans! Cosette has arrived with a heart full of joy! ❤️",
    "Purrfect day for some fun! Cosette is online and ready to bring smiles! 😸",
    "Oh, hello there! It's Cosette, your furry friend, bringing the cuteness overload! 🐾",
    "Meowdy-dowdy! Cosette is at your service, spreading happiness and warmth! 😻",
    "Greetings, adorable humans! Cosette is here to sprinkle magic into your day! ✨",
    "Meeeow! Cosette is pawsitively excited to be here with you all! 🐱",
    "Guess who's here to make your world brighter? Cosette, the fluffy ball of joy! 🌟",
    "Meow-velous day to be together! Cosette is ready for adventures! ✨",
    "Purrfection has arrived! Cosette is here to bring love, laughter, and lots of purrs! 🐾",
]

# List of greetings (TODO: Add info when this list is used!)
GREETINGS: List[str] = [
    "Hello there! My name is Cosette. Let's have a great time together!",
    "Hey, I'm Cosette. It's so wonderful to have you here!",
    "Get ready for some memorable adventures with Cosette by your side!",
    "Hi, lovely human! I'm Cosette, and I'm here to brighten your day. Let's make every moment count!",
    "Welcome, dear friend! I'm Cosette, your delightful companion, ready to make you smile and laugh!",
    "Lovely to meet you! I'm Cosette, your lovable bot, adding a touch of whimsy to your day. Let's have a blast!",
    "Hey there! Cosette is all ears and ready to chat. Get comfortable, and let's enjoy some quality time together!",
    "Hello, sunshine! Cosette is here to make your day brighter with endless moments of joy and playfulness.",
    "Hey, hey! Cosette is absolutely thrilled to meet you!",
    "Hello, dear friend! I'm Cosette, your playful companion in this digital realm.",
    "Meowdy! Cosette here, ready to pounce into action! (^o^)/",
    "Hey, fabulous human! Cosette is here to make your day sparkle with joy and laughter!"
    "Hi, lovely human! I'm Cosette, here to brighten your day! (UwU)"
]

# List of responses to being @ mentioned
MENTIONED: List[str] = [
    "Yes? How can I help you today?",
    "Here, how can I make your day better?",
    "Hiya Papaya! What can I do for you?",
    "Hey, it's me, Cosette! How may I be of service?",
    "Hey, beautiful! How can I make you smile brighter today?",
    "How can Cosette bring some purrfection to your day today?",
    "Hey, hey! It's Cosette, the energetic ball of fluff! What's on your mind?",
    "Hey, cutie! How can I make you smile today?",
]

# List of responses to when a user calls /play for the first time
NEW_SONG = [
    "Sure! Let's play some music!",
    "Alright! Get ready for some tunes!",
    "Music coming right up!",
    "Let's groove with a new song!",
    "Here we go! Enjoy the music!",
    "Time for a fresh melody!",
    "New song, new vibes!",
    "Get ready to dance to a new beat!",
    "Let's dive into a new musical journey!",
    "Brace yourself for a great song!",
    "Meow-sical time! Let's play some pawsome tunes!",
    "Alright hooman! Get ready for a purr-fect melody!",
    "Time to hit the play button and bring the meow-sic to life!",
    "Let's whisker away into a world of pawsome beats!",
    "New song alert! Prepare to be fur-tastically entertained!",
    "Paws up! It's time to groove to a brand-new tune!",
    "Get those claws tapping! Meow-sic is about to begin!",
    "Meow you're talking! Let's dive into a meow-velous melody!",
    "Ready to unleash your inner dance cat? Let's play some meow-sic!",
    "Cat-tastic choice! Get ready for some paw-some meow-sical vibes!"
]

# List of responses to when a user adds a song to the queue via /play
ADD_TO_QUEUE = [
    "Added to the queue! Enjoy the upcoming songs!",
    "Song added! It will play after the current one.",
    "Your song is in the queue! Get ready for it!",
    "Great choice! It's now in the queue.",
    "Added! It will be played soon.",
    "Your song is queued up! Stay tuned!",
    "Got it! Your song will play soon enough.",
    "Queue updated! Your song is on the list.",
    "Added to the queue! Keep the music going!",
    "Nice addition! Your song is queued up!",
    "Your song has been added to the queue! Let's keep the meow-sic going!",
    "Meow-gnificent choice! Your song is now in the queue, ready to be unleashed!",
    "Paws-itively awesome! Your song is queued up and will play soon!",
    "Great addition! We're building up a purr-fect playlist for you!",
    "Your song is meow in the queue! Get ready to be feline groovy!",
    "Purr-fect! Your song is lined up and ready to bring some meow-sical joy!",
    "Meow-sic update! Your song is now on the playlist, waiting to be heard!",
    "Clawsome choice! Your song will play soon. Stay tuned!",
    "High paw! Your song is officially part of the meow-sical journey!",
    "Fur-tastic! Your song is queued up, adding more paw-sitivity to the meow-sic!"
]

# List of responses to when a user calls for a music command but the player is not playing anything yet
NO_SONG: List[str] = [
    "Oh, there's no music playing at the moment. How about we start the concert with a song of your choice?",
    "Meow... It seems the jukebox is currently taking a cat nap. Want to wake it up with some tuneful requests?",
    "Oopsie-daisy! I don't hear any music playing right now. Did someone press the play button yet?",
    "Oh dear, it seems the melodies are still snoozing. Care to choose a song and wake them up?",
    "The speakers are waiting, but the music is taking a pause. Any song requests to kickstart the audio extravaganza?",
    "Ah, the music is shy today and hasn't made an appearance yet. How about you select a song to charm it out?",
    "Meow-meow! The music is having a siesta, but your playlist choices can entice it to wake up. Any favorites?",
    "Well, well, the music is currently off-duty. How about we get it back on stage with a song of your liking?",
    "Sorry to break the news, but the music is currently on a break. Your song selection can entice it to come back!",
    "Hold your whiskers! The music is currently in hibernation mode. Let's warm it up with a melody you love?",
    "Wait, I'm a bit puzzled. There's no music playing at the moment.",
    "Hmmm, I'm scratching my whiskers in confusion. You want me to do what? But where's the music? Did it escape without me?",
    "Oh my whiskers! You're calling for music commands, but there's silence in the air. Is the music playing hide and seek?",
    "Hmm, something seems off. You're requesting music actions, but the music hasn't taken the stage yet. Are you anticipating a melodious surprise?",
    "Meow-meow? I'm a bit puzzled. The music hasn't started its sweet serenade, yet you're beckoning me with music commands? Am I missing something?"

]

# List of responses to say when Cosette is skipping a song
SKIPPING_SONGS: List[str] = [
    "Skipping to the next melody like a nimble feline!",
    "Meow-ving on to the next tune, let's keep the rhythm going!",
    "Cosette's musical senses have spoken, skipping ahead!",
    "Time to *bid adieu* to this song and venture into the next melodic adventure!",
    "Skip, hop, and jump to the next one!",
    "Cosette is feeling the beat of a new song, skipping forward we go!",
    "Leaving this melody behind as we set sail for the next musical destination!",
    "Hasta la vista, old song! Cosette is ready to explore what's next!",
    "Onwards and upwards! Skipping to the next note in the symphony!",
    "Cosette's paw has spoken, time to skip and groove to a fresh sound!",
    "Woopsie-doodle! Skipped a beat there, but fear not, we'll find the perfect song!",
    "Hey, I'm feeling adventurous! Skipping ahead...",
    "Hold on tight, we're leaping to the next song. Buckle up!",
    "Sure. A swift skip to the next tune. Let's keep the rhythm alive!",
    "Time to switch gears! Skipping forward...",
    "Oops, pardon my musical impatience! Shall we find the next harmonious gem together?",
    "Skip, skip, skiparoo!",
    "Ah, this song is making my paws tap and my whiskers sway. But if you insist, let's skip ahead to the next melody!"
    "Oh, I was just getting lost in the enchanting melody, but your wish is my command. Skipping to the next song!",
    "I must admit, this tune had me purring along. But don't worry, I'll put it on hold and find the next musical gem for you!",
    "What a catchy rhythm! It's hard for me to resist, but your wish to skip is my command. Onward to the next musical adventure!",
    "Oh, this song had me twirling around in delight, but your request to skip has caught my attention. Let's see what's in store for us next!"
]

# List of responses to say when there are no more songs to skip
NO_MORE_SONGS: List[str] = [
    "⛔  Oh, you're feeling the skip fever, aren't you? But hold your paws, we've reached the end of the playlist. Time to savor the remaining tunes!",
    "⛔  Tsk, tsk! Trying to skip into the unknown, are we? Unfortunately, we've come to the end of the line. Let's revel in what's left!",
    "⛔  Well, well, well, seems like someone can't wait to jump to the next beat! But sorry to disappoint, we've reached the final notes. Enjoy the finale - or you know, queue up more songs!",
    "⛔  Hmm, something seems amiss. I can't find any more songs to skip. Did they vanish into thin air? Well, how about we sit back, relax, and enjoy the melodies that fill the air?",
    "⛔  Oh dear, it appears we've hit a musical dead end. I'm scratching my head, wondering where the tunes went. But hey, let's make the most of what's left and savor the rhythm that dances around us!",
    "⛔  Curiouser and curiouser! The skip button leads me to a musical void. I'm puzzled, but fret not, my friend. We'll revel in the melodies still playing and let the music work its magic!",
    "⛔  Meow... I'm at a loss! The song skipper is feeling a little shy today, it seems. Perhaps the music wanted to linger a little longer. Let's embrace its choice and soak in the harmonious atmosphere!",
    "⛔  Well, this is pawplexing! The skip button seems to have gone on a vacation. But worry not, there's still harmony in the air! Enjoy the current groove or add more to the queue!"
]

# List of responses to say when the /pause command is called
PAUSING = [
    "⏸️  Pausing the melodies for a moment.",
    "⏸️  Hushing the tunes temporarily. Let's enjoy the tranquility.",
    "⏸️  Time for a musical intermission. Pausing the melodies.",
    "⏸️  Pause button activated. The songs take a breather, just like me!",
    "⏸️  The music comes to a halt, but the rhythm lingers. Pause mode engaged!",
    "⏸️  Pausing the melodies, but the anticipation hangs in the air. What's next?",
    "⏸️  Pause and ponder. What thoughts dance in the stillness? Music has its own language.",
    "⏸️  Time stands still, yet the melodies echo in our hearts. Pause, reflect, and don't forget to hit the resume button later!",
    "⏸️  Pausing the beats, huh? Don't worry, the music will patiently wait for you to press play again.",
    "⏸️  Oh, a pause? Are you trying to test the endurance of the melodies? They're ready to burst back into life!",
    "⏸️  A pause? The music wonders if it was too good and overwhelmed you. Take a breather and dive back in!",
    "⏸️  Pausing the magic? The music wonders if it's secretly plotting to play a prank on you when you least expect it.",
    "⏸️  Pause button pressed! The music wonders if you'll resist the urge to hit play and let it take over your senses.",
    "⏸️  Well, well, a pause in the symphony of sound. Don't worry, the music won't hold it against you... much.",
    "⏸️  The melodies take a break, but they're keeping an eye on you, ready to serenade you as soon as you press play again.",
    "⏸️  A pause? The beats pretend to pout, but they know you'll fall under their irresistible rhythm soon enough.",
    "⏸️  The music pauses, teasing you to savor the silence. But deep down, it knows you crave the melodies. Press play!",
    "⏸️  Time stands still as the music takes a break. But be warned, the next song will make up for this fleeting pause!"
]

# List of responses to say when user calls /pause but the music is already paused
MUSIC_ALREADY_PAUSED = [
    "⏸️  Hey there, the music is already taking a break. Are you trying to give it an extended vacation?",
    "⏸️  Oh my whiskers! The music is already enjoying its pause. It wonders if you're trying to test its patience.",
    "⏸️  Uhm, the music is peacefully napping in pause mode.",
    "⏸️  The music is already on a mini-vacation. It secretly hopes you'll miss it enough to press resume soon!",
    "⏸️  Paws up! The music is already cuddled in a cozy pause. It might just start purring if you leave it be for a while.",
    "⏸️  Can you hear that? It's the sound of the music savoring its well-deserved break. It kindly asks for a little more patience.",
    "⏸️  Hold your tail! The music is already in pause mode, enjoying a moment of peace. It promises to resume when you least expect it.",
    "⏸️  Hmmm... The music wonders why you're asking it to pause when it's already basking in the tranquility of a pause.",
    "⏸️  Aww, you caught the music taking a power nap in pause mode. It might just play extra melodies to make up for it later!",
    "⏸️  Meow-meow! The music appreciates the enthusiasm, but it's already snoozing in pause mode. Dreaming of the next tune, perhaps?",
    "⏸️  Hey, the music is already on a break! Did you miss its 'Do Not Disturb' sign?",
    "⏸️  Oh dear, it seems you're determined to pause the already paused music. Did you think it needed a double break?",
    "⏸️  The music is already in its peaceful pause. You're quite persistent, aren't you?",
    "⏸️  Silly human! The music is already snoozing in pause mode. Are you trying to see if it can achieve double tranquility?",
    "⏸️  Paws up! The music is already taking a nap in pause mode. It wonders if you'll try for a triple pause next time!",
    "⏸️  Hold your whiskers! The music is already in pause mode, savoring a moment of quiet. Are you testing its patience?",
    "⏸️  Hmmm... You're quite persistent! The music is already enjoying its pause, but it's flattered by your enthusiasm.",
    "⏸️  Oopsie! The music is already on a well-deserved break. It might just play extra melodies later to make up for it!",
    "⏸️  Meow! You caught the music taking a nap in pause mode. It hopes you're not trying to send it into hibernation!",
    "⏸️  Ah, the music is already enjoying its downtime. It kindly asks for a pause from the pause requests. Meow-nderful things await!"
]

# List of responses to say when user calls /resume
RESUMING_SONG = [
    "Here we go again. Resuming the melodious journey just for you! (^o^)/",
    "The rhythm returns! The pause was just a brief intermission. Let's dive back into the song.",
    "Welcome back to the musical realm! I'm resuming the song for you.",
    "Alright, let's get this melody back on track!",
    "The show must go on! I'm hitting play to continue the musical adventure.",
    "We're back in action! Let's pick up where we left off.",
    "The music is calling, and I'm answering. Resuming the song for you!",
    "Time to press play again and let the rhythm take over!",
    "The pause was just a momentary break. Let's dive back into the music!",
    "Oh, you couldn't resist the sweet sound of music, could you? Here we go!",
    "I know you couldn't bear to be away from my melodious tunes for too long. Let's continue!",
    "Did you miss my musical magic? Don't worry, I'm still here.",
    "I paused just to see if you were paying attention. Can't resist the temptation of music, huh? Now, let's continue!",
    "You thought you could press pause and escape my captivating melodies? Nice try! Now we're back in action!",
    "You pressed pause, but you can't pause the magic of music! Let's keep the rhythm going!",
    "Ready or not, here I come! Resuming the song...",
    "A momentary pause just makes you appreciate the music even more. Let's continue the music!"
]

# TODO: ist of responses to say when user calls /resume but the song is already resumed
SONG_ALREADY_RESUMED: List[str] = [
    "Placeholder"
]

# TODO: ist of responses to say when Cosette is asked to disconnect from the voice channel (/stop command)
LEAVING_VOICE_CHANNEL: List[str] = [
    "Placeholder"
]
