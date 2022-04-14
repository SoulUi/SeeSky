import rhinoscriptsyntax as rs

Psl = []
ps = []
n = 0
for p in Pt:
    if n == Num - 1:
        ps.append(p)
        Psl.append(ps)
        ps = []
        n = 0
    else:
        ps.append(p)
        n += 1

Nor = []
for srf, pts in zip(Srf, Psl):
    numerator = Num
    for pt in pts:
        param = rs.SurfaceClosestPoint(srf, pt)
        normal = rs.SurfaceNormal(srf, param)
        nor = rs.AddLine(pt, pt + Far * normal)
        intersections = []
        for b in Buildings:
            intersection_list = rs.CurveBrepIntersect(nor, b)
            if intersection_list is not None:
                # print(len(intersection_list))
                for i in intersection_list:
                    if len(i) != 0:
                        for ii in i:
                            intersections.append(ii)

        if len(intersections) != 0:
            dis = Far
            for inter in intersections:
                # print(inter)
                distance = rs.Distance(pt, inter)
                if dis > distance:
                    dis = distance
            # print(dis)
            nor = rs.AddLine(pt, pt + dis * normal)
            numerator -= 1

        Nor.append(nor)
    per = numerator / Num
    print(per)

a = Nor