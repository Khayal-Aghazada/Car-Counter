# python -m apps.car_counter --mirror 0



"""Vehicle counter via YOLO + SORT + line counting with optional ROI mask."""
import argparse
import cv2
import numpy as np
from modules import (
    Camera, YOLODetector, SortTracker, LineCounter, ImageOps,
    tracks as draw_tracks, lines as draw_lines, texts as draw_texts
)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--src", default="assets/demo_video/cars.mp4")
    p.add_argument("--weights", default="yoloW/yolov8n.pt")
    p.add_argument("--conf", type=float, default=0.30)
    p.add_argument("--max-age", type=int, default=20)
    p.add_argument("--min-hits", type=int, default=3)
    p.add_argument("--iou-thr", type=float, default=0.30)
    p.add_argument("--wait", type=int, default=1)
    p.add_argument("--mirror", type=int, default=0)
    p.add_argument("--line", type=int, nargs=4, default=[350, 300, 680, 300])
    p.add_argument("--mask", type=str, default=None, help="path to ROI mask (grayscale)")
    p.add_argument("--invert-mask", type=int, default=0, help="invert ROI mask if 1")
    return p.parse_args()


def main():
    args = parse_args()
    cam = Camera(args.src, mirror=bool(args.mirror), wait=args.wait)
    det = YOLODetector(args.weights, classes=["car", "bus", "truck", "motorcycle"], conf=args.conf)
    trk = SortTracker(max_age=args.max_age, min_hits=args.min_hits, iou_threshold=args.iou_thr)
    lc = LineCounter({"veh": tuple(args.line)}, tol=18)

    roi = None
    for frame in cam.iterate():
        if args.mask and roi is None:
            roi = ImageOps.load_roi_mask(args.mask, shape=frame.shape)
            if args.invert_mask:
                roi = cv2.bitwise_not(roi)

        det_frame = ImageOps.apply_roi(frame, roi) if roi is not None else frame

        boxes, scores, _names = det.infer(det_frame)
        dets = np.hstack([boxes, scores[:, None]]) if boxes.shape[0] else np.empty((0, 5), dtype=float)

        tracks = trk.update(dets)
        counts, _ = lc.update(tracks)

        draw_lines(frame, lc.lines)
        draw_tracks(frame, tracks)
        draw_texts(frame, [(f"Count: {counts.get('veh', 0)}", (50, 80), 1.8, (0, 255, 0), 3)])
        cam.show("Car Counter", frame)

    cam.release()


if __name__ == "__main__":
    main()
