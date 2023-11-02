import argparse
from pytube import YouTube


def arg_parser():
    parser = argparse.ArgumentParser()

    # Required start and end dates
    parser.add_argument("-source_url", required=True)
    parser.add_argument("-save_dir", required=True)
    parser.add_argument("-download_type", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = arg_parser()
    print("Selected Arguments:")
    print(args)

    yt = YouTube(args.source_url)

    if args.download_type == "video":
        stream = yt.streams.get_highest_resolution()
        stream.download(args.save_dir)

    elif args.download_type == "audio":
        audio = yt.streams.get_audio_only()
        audio.download(args.save_dir)

    else:
        print(f"Download type {args.download_type} does not exist")
