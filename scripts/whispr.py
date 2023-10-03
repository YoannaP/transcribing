import time
import argparse
import whisper


def arg_parser():
    parser = argparse.ArgumentParser()

    # Required start and end dates
    parser.add_argument("-source_path", required=True)
    parser.add_argument("-save_dir", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    now = time.time()
    args = arg_parser()
    print("Selected Arguments:")
    print(args)

    model = whisper.load_model("tiny")
    text = model.transcribe(args.source_path)

    # outputile = "../output/whispr_transcripts/example_podcast_mp3.txt"

    with open(args.save_dir, "w") as text_file:
        text_file.write(text["text"])

    print(f"Time Taken: {time.time() - now}")
