import cv2
import argparse

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', '--input_uri', metavar="URI", required=True, help=
                        'URI to input stream\n'
                        'video file (e.g. video.mp4)\n')
    parser.add_argument('-o', '--output_uri', required=True, metavar="URI",
                        help='URI to output video (e.g. output.mp4)')

    parser.add_argument('-s', '--show', action='store_true', help="shows output")
    args = parser.parse_args()

    pipeline = 'filesrc location=%s ! decodebin ! ' % args.input_uri
    cvt_pipeline = (
                    'nvvidconv interpolation-method=5 ! '
                    'video/x-raw, width=960, height=540, format=BGRx !'
                    'videoconvert ! appsink sync=false'
                )

    in_stream = pipeline + cvt_pipeline
    ou_stream = 'appsrc ! autovideoconvert ! omxh264enc preset-level=2 ! qtmux ! filesink location=%s' % args.output_uri

    reader = cv2.VideoCapture(in_stream)

    w  = int(reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(reader.get(cv2.CAP_PROP_FRAME_HEIGHT))

    writer = cv2.VideoWriter(ou_stream, cv2.CAP_GSTREAMER, 0,  25, (w, h), True)

    while(reader.isOpened()):
        ret, frame = reader.read()
        if ret and args.show:
            cv2.imshow("frame", frame)
            cv2.waitKey(1)
        if not ret:
            break        

        writer.write(frame)

    writer.release()
    reader.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
