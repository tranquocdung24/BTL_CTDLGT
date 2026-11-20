def layTen(ten):
    parts = ten.split()
    return parts[-1] if parts else ""

def soSanhTheoMa(a,b):
    return a.maKH < b.maKH

def soSanhTheoTen(a,b):
    tenA = layTen(a.hoTen)
    tenB = layTen(b.hoTen)
    if tenA != tenB: return tenA < tenB
    else : return a.hoTen < b.hoTen

