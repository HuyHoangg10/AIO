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


box_a = (2, 3, 7, 9)
box_b = (4, 5, 9, 10)

print(compute_iou(box_a, box_b))
