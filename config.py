from tobrot.get_cfg import get_config


class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = get_config("1721286813:AAHjx-PW5CqZJtKwdqvjYtoTr-iuy10dHI4", should_prompt=True)
    # The Telegram API things
    APP_ID = int(get_config("6516030", should_prompt=True))
    API_HASH = get_config("7ae157c68a4ac324c210da0fbdbf62b8", should_prompt=True)
    # Get these values from my.telegram.org
    # array to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(
        int(x) for x in get_config(
            "597639474",
            should_prompt=True
        ).split()
    )
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("./DOWNLOADS", "./DOWNLOADS")
    # Telegram maximum file upload size
    MAX_FILE_SIZE = int(get_config("50000000", 50000000))
    TG_MAX_FILE_SIZE = int(get_config("2097152000", 2097152000))
    FREE_USER_MAX_FILE_SIZE = int(
        get_config("50000000", 50000000)
    )
    # chunk size that should be used with requests
    CHUNK_SIZE = int(get_config("128", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config(
        "DEF_THUMB_NAIL_VID_S",
        "https://wallpaperaccess.com/full/819111.jpg"
    )
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = int(get_config(
        "4096",
        4096
    ))
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = int(get_config(
        "1800",
        3600
    ))
    #
    ARIA_TWO_STARTED_PORT = int(get_config(
        "6800",
        6800
    ))
    EDIT_SLEEP_TIME_OUT = int(get_config(
        "1",
        1
    ))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(get_config(
        "600",
        600
    ))
    MAX_TG_SPLIT_FILE_SIZE = int(get_config(
        "1900000000",
        1900000000
    ))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("█", "█")
    UN_FINISHED_PROGRESS_STR = get_config("░", "░")
    # add offensive API
    TG_OFFENSIVE_API = get_config(None, None)
    # URL for the rclone configuration
    R_CLONE_CONF_URI = get_config(None, None)
    # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
