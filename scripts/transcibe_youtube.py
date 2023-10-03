from youtube_transcript_api import YouTubeTranscriptApi

### LINK: https://github.com/jdepoix/youtube-transcript-api
from youtube_transcript_api.formatters import TextFormatter

video_id = "m0-CICGHRSo"
# https://www.youtube.com/watch?v=m0-CICGHRSo
# Must be a single transcript.
transcript = YouTubeTranscriptApi.get_transcript(video_id)

formatter = TextFormatter()

# .format_transcript(transcript) turns the transcript into a JSON string.
json_formatted = formatter.format_transcript(transcript)


# Now we can write it out to a file.
with open(
    "youtube_transctipts/social_radars_brian_chesky.txt", "w", encoding="utf-8"
) as json_file:
    json_file.write(json_formatted)
