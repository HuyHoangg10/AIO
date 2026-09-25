def compute_iou(
    box_a: tuple[int, int, int, int], box_b: tuple[int, int, int, int]
) -> float:
    xA_min, yA_min, xA_max, yA_max = box_a
    xB_min, yB_min, xB_max, yB_max = box_b

    xI_min = max(xA_min, xB_min)
    yI_min = max(yA_min, yB_min)

    xI_max = min(xA_max, xB_max)
    yI_max = min(yA_max, yB_max)

    intersection_area = max(0, xI_max - xI_min + 1) * max(0, yI_max - yI_min + 1)

    box_a_area = (xA_max - xA_min + 1) * (yA_max - yA_min + 1)
    box_b_area = (xB_max - xB_min + 1) * (yB_max - yB_min + 1)
    union_area = box_a_area + box_b_area - intersection_area

    return intersection_area / union_area
        

def apply_nms(
    boxes: list[tuple[int, int, int, int, float]], iou_threshold: float
) -> list[tuple[int, int, int, int, float]]:
    sorted_boxes = sorted(boxes, key=lambda box: box[4], reverse=True)
    selected_boxes = []

    while sorted_boxes:
        highest_score_box = sorted_boxes.pop(0)
        selected_boxes.append(highest_score_box)

        sorted_boxes = [
            box
            for box in sorted_boxes
            if compute_iou(highest_score_box[:4], box[:4]) < iou_threshold
        ]

    return selected_boxes


boxes = [
    (12, 84, 140, 212, 0.95),
    (24, 84, 152, 212, 0.70),
    (12, 90, 140, 215, 0.60),
    (100, 100, 220, 220, 0.90),
]

iou_threshold = 0.5

print(apply_nms(boxes, iou_threshold))
