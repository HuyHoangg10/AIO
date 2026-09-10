def iou_cal(box1,box2):
    xA = max(box1[0],box2[0])
    yA = max(box1[1],box2[1])

    xB = min(box1[2],box2[2])
    yB = min(box1[3],box2[3])

    interception = max(0,xB - xA + 1) * max(0,yB - yA +1)

    area_box1 = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] +1)
    area_box2 = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] +1)

    iou = interception / (area_box1 + area_box2 - interception)
    return iou 
def non_max_supression(boxes,scores,iou_thresh):
  sorted_index = sorted(range(len(scores)),key= lambda k:scores[k],reverse=True)
  kept_index = []

  while sorted_index:
     i = sorted_index.pop(0)
     kept_index.append(i)
     filter_index = []
     for j in sorted_index:
      if iou_cal(boxes[i],boxes[j]) <= iou_thresh:
         filter_index.append(j)
     sorted_index = filter_index
  return kept_index

# 5 Bounding Boxes với tọa độ lộn xộn (x_min, y_min, x_max, y_max)
boxes = [
    [30, 30, 80, 80],    
    [0, 0, 20, 20],      
    [35, 35, 85, 85],    
    [100, 100, 150, 150],
    [28, 28, 78, 78]     
]

scores = [0.85, 0.4, 0.92, 0.65, 0.5]

iou_threshold = 0.2

print(non_max_supression(boxes,scores,iou_threshold))