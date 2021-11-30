# video-io
   * Read video file from openCV.
   * Need to specify decodebin, nvvidconv interpolation-method, video/x-raw, videoconvert when running a Jetson platform.
   * relase writer before releasing reader
   * example: ``` python videoio.py -i input.mp4 -o out.mp4 -s ```
