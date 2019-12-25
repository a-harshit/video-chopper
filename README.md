# Python Video Chopper

Its a simple command line Python script that splits a video into chunks of a required size. Underneath, the script uses [FFMpeg]

Run `python3 video-chopper.py file_name chunk_size (in bytes)`

Example `python3 video-chopper.py file.mp4 30000000`

This splits `file.mp4` into chunks of 30 Megabytes and each chunk will be suffixed with numeric index, for example `file0.mp4`, `file1.mp4`, etc.

If no chunk size is given then by default, video will be splitted in to chunks of 10 Megabytes.

Tip: Do set your video size less than the required size as it may go a bit above as FFMpeg splits video on the basis of frames.

## Installing ffmpeg

See [FFmpeg installation guide](https://www.ffmpeg.org/download.html) for details.
[FFMpeg]: https://www.ffmpeg.org/

## Credits
Modified code to split on the basis of required chunk size. Credits to the due author.

## LICENSE

[APACHE](LICENSE)
