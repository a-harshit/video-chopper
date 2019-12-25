import shlex
from subprocess import check_call, PIPE, Popen
import re
import os
import sys

length_regex = re.compile('Duration: (\d{2}):(\d{2}):(\d{2})\.\d+,')


def calculate_video_size(video_file_path):
    p1 = Popen(["ffmpeg", "-i", video_file_path], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    output = Popen(["grep", 'Duration'], stdin=p1.stderr, stdout=PIPE, universal_newlines=True)
    p1.stdout.close()
    matches = length_regex.search(output.stdout.read())
    if matches:
        video_size = int(matches.group(1)) * 3600 + \
            int(matches.group(2)) * 60 + int(matches.group(3))
        return video_size
    else:
        print("Can not determine video size.")
        raise SystemExit


def chop_video(video_file_path, chunk_size):
    video_size = calculate_video_size(video_file_path)
    file_name = os.path.basename(video_file_path)

    parsed_video_size = 0
    counter = 0
    raw_name, ext = file_name.rsplit(".", 1)
    while video_size - parsed_video_size:
        cmd = f"ffmpeg -i {video_file_path} -vcodec copy -strict -2 -fs {chunk_size} -ss \
        {parsed_video_size} {raw_name}{counter}.{ext}"
        check_call(shlex.split(cmd), universal_newlines=True)
        parsed_video_size = parsed_video_size + \
            calculate_video_size(raw_name + str(counter) + '.' + ext)
        counter = counter + 1


def main():
    default_size = 10000000
    video_file_path = sys.argv[1]
    chunk_size = sys.argv[2] if len(sys.argv) == 3 else default_size
    chop_video(video_file_path, chunk_size)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("An error occured. " + str(e))
