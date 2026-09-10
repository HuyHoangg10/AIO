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

box1 = (0,0,5,5)
box2 = (2.5,2.5,7.5,7.5)
result_iou = iou_cal(box1,box2)
print(result_iou)