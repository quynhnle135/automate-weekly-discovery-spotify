import argparse
from automate_spotify import *


def main():
    parser = argparse.ArgumentParser("Automate Python Program")
    parser.add_argument("-u", "--user", action="store_true", help="Show user's information.")
    parser.add_argument("-p", "--playlists", action="store_true", help="Show user's playlist.")
    parser.add_argument("-t", "--tracks", type=int, help="Show user's saved tracks. Enter the number of tracks you want to view.")
    parser.add_argument("-w", "--weekly", action="store_true", help="Show user's Discover Weekklt playlist generated by Spotify.")
    parser.add_argument("-d", "--daylist", action="store_true", help="Show user's current Daylist Playlist generated by Spotify.")
    parser.add_argument("-c", "--create", type=str, help="Create new playlist. Please provide name (required) and description (default)")
    parser.add_argument("-a", "--add", type=str, help="Add songs to the specified playlist.")
    parser.add_argument("-ad", "--adddaylist", type=str, help="Add songs from DayList to the specified playlist.")
    parser.add_argument("-aw", "--addweekly", type=str, help="Add songs from Discover Weekly to the specified playlist.")

    parser.add_argument("-de", "--description", type=str, help="Enter description for your new playlist.")
    parser.add_argument("-so", "--songs", type=str, nargs="+", help="Enter the list of songs' URLs you want to add to your playlist.")

    args = parser.parse_args()

    if args.user:
        print("*** You are viewing user info ***")
        view_user_info()
    elif args.playlists:
        print("*** You are viewing user playlists ***")
        view_user_playlists()
    elif args.tracks:
        print("*** You are viewing user saved tracks ***")
        view_user_saved_tracks(args.tracks)
    elif args.weekly:
        print("*** You are viewing this week Discover Weekly playlist's tracks ***")
        view_weekly_discovery_tracks()
    elif args.daylist:
        print("*** You are viewing user's current Day List playlist's track ***")
        view_day_list_tracks()
    elif args.create:
        print("*** New playlist is being created ***")
        create_playlist(args.create, args.description)
    elif args.add and args.songs:
        print("*** Songs are being added to your playlist ***")
        add_songs_to_playlist(args.add, args.songs)
    elif args.adddaylist:
        print("*** Songs from Day List playlist have been added to your playlist ***")
        add_songs_from_daylist_playlist(args.adddaylist)
    elif args.addweekly:
        print("*** Songs from Discover Weekly playlist have been added to your playlist ***")
        add_songs_from_weekly_playlist(args.addweekly)
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()