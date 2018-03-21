#!/usr/bin/python

def merge_ranges(meetings):
    # Merge meeting ranges
    last = False
    if len(meetings) < 2:
        return meetings
    result = []
    meetings.sort(key=lambda x: x[0]) # sort on early time
    # print(meetings)
    pt_a = meetings.pop(0)
    pt_b = meetings.pop(0)
    if not meetings:
        last = True # go through once if not already
    # print("a: {} b: {}".format(pt_a, pt_b))
    while meetings or last:
        # print("a: {} b: {}".format(pt_a, pt_b))
        if pt_a[0] <= pt_b[0] <= pt_a[1]:
            if pt_b[1] >= pt_a[1]:
                # merge
                # results.append((pt_a[0], pt_b[1]))
                pt_a = (pt_a[0], pt_b[1])
            if meetings:
                pt_b = meetings.pop(0)
            else:
                result.append(pt_a)
        else:
            result.append(pt_a)
            pt_a = pt_b
            if meetings:
                pt_b = meetings.pop(0)
            else:
                result.append(pt_a)
            # print("just moved onto next pt, a: {} b: {}, meetings left: {}".format(pt_a, pt_b, meetings))

        last = True if not meetings and not last else False

    return result


# meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# meetings = [(0, 1), (0, 3), (0, 8), (0, 12), (0, 10)]
# meetings = [(0, 1), (0, 3)]
meetings = [(1, 5), (6, 8)]
print(merge_ranges(meetings))
