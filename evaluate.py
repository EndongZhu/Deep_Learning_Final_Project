import numpy as np


def getUnion(src_ranges, tar_ranges):
    combined = src_ranges + tar_ranges
    combined.sort()
    unions = []
    cur = list(combined[0])
    for idx in range(1, len(combined)):
        if combined[idx][0] > cur[1]:
            unions.append(cur)
            cur = list(combined[idx])
        else:
            cur[1] = max(cur[1], combined[idx][1])
    unions.append(cur)
    return unions

def getIntersection(interval_1, interval_2):
    start = max(interval_1[0], interval_2[0])
    end = min(interval_1[1], interval_2[1])
    if start < end:
        return (start, end)
    return None

def calcIOU(interval_1, interval_2):
    intersection = getIntersection(interval_1, interval_2)
    if intersection:
        union = getUnion([interval_1], [interval_2])
        union_len = 0
        for interval in union:
            union_len += (interval[1] - interval[0])
        intersection_len = intersection[1] - intersection[0]
        return 1.0 * intersection_len / union_len
    else:
        return 0;

def evaluate(src_ranges, tar_ranges, IOU_threshold):
    src_unions = getUnion(src_ranges, [])
    tar_unions = getUnion(tar_ranges, [])
    cnt = 0
    for src in src_unions:
        for tar in tar_unions:
            if calcIOU(src, tar) > IOU_threshold:
                cnt += 1
    mAP = 1.0 * cnt / len(src_unions)
    recall = 1.0 * cnt / len(tar_unions)
    return mAP, recall