from decimal import Decimal

WH_butun_S = Decimal(0)
WH_B_romp_S = Decimal(0)
j_t_romp_S = Decimal(0)
S = Decimal(0)
w, h, d = map(float, input().split())


def b_romps_S(w, h, d):
    romp_B_S = d * (d / 2)
    WH_B_romp_S = ((w // d) * (h // d)) * romp_B_S
    return WH_B_romp_S


def q_rompsW_orH_S(w, h, d):
    q_romp_x = w - (d * (w // d))
    if q_romp_x <= (d / 2):
        q_bitta_rS = ((q_romp_x * 2) * q_romp_x) / 2
    else:
        q_bitta_rS = (d * (d / 2)) / 2
        q_bitta_rS += q_bitta_rS - (((d - q_romp_x) * 2) * (d - q_romp_x)) / 2
    j_t_romp_S = (h // d) * q_bitta_rS
    return j_t_romp_S


def noqulay_sh(w, h, d):
    S = Decimal(0)
    q_sh_w = w - ((w // d) * d)
    q_sh_h = h - ((h // d) * d)
    if (d / 2) < q_sh_h and (d / 2) < q_sh_w:
        if (q_sh_w - (d / 2)) + (q_sh_h - (d / 2)) >= (d / 2):
            S1 = (((d - q_sh_h) * 2) * (d - q_sh_h)) / 2
            S2 = (((d - q_sh_w) * 2) * (d - q_sh_w)) / 2
            S = (d * (d / 2)) - S1 - S2
        else:
            S1 = ((q_sh_h - (d / 2)) * (q_sh_w)) - (((q_sh_h - (d / 2)) * (q_sh_h - (d / 2))) / 2)
            S2 = ((q_sh_w - (d / 2))) * (d / 2) - (((q_sh_w - (d / 2)) * (q_sh_w - (d / 2))) / 2)
            S3 = ((d / 2) * (d / 2)) / 2
            S = S1 + S2 + S3
    elif (q_sh_w < (d / 2)) and (q_sh_h < (d / 2)):
        if ((d / 2) - q_sh_w) + ((d / 2) - q_sh_h) >= (d / 2):
            S = 0
        else:
            S_l = q_sh_w - ((d / 2) - q_sh_h)
            S = (S_l * S_l) / 2
    elif (q_sh_w > (d / 2)) and (q_sh_h < (d / 2)):
        if (q_sh_w - (d / 2)) + ((d / 2) - q_sh_h) > (d / 2):
            S = ((q_sh_h * 2) * q_sh_h) / 2
        else:
            S1 = ((q_sh_w - (d / 2)) * q_sh_h) - (((q_sh_w - (d / 2)) * (q_sh_w - (d / 2))) / 2)
            S2 = (q_sh_h * q_sh_h) / 2
            S = S1 + S2
    elif (q_sh_w < (d / 2)) and (q_sh_h > (d / 2)):
        if ((q_sh_h - (d / 2)) + ((d / 2) - q_sh_w)) > (d / 2):
            S = ((q_sh_w * 2) * q_sh_w) / 2
        else:
            S1 = ((q_sh_h - (d / 2)) * (q_sh_w)) - (
                ((q_sh_h - (d / 2)) * (q_sh_h - (d / 2))) / 2
            )
            S2 = (q_sh_w * q_sh_w) / 2
            S = S1 + S2
    elif q_sh_w == (d / 2) and q_sh_h == (d / 2):
        S = (q_sh_w * q_sh_w) / 2
    return S


if w % d == 0 and h % d == 0:
    print("%.4f" % (b_romps_S(w, h, d)))
elif w % d != 0 and h % d == 0:
    print("%.4f" % (b_romps_S(w, h, d) + q_rompsW_orH_S(w, h, d)))
elif w % d == 0 and h % d != 0:
    print("%.4f" % (b_romps_S(w, h, d) + q_rompsW_orH_S(h, w, d)))
else:
    print(
        "%.4f"
        % (
            b_romps_S(w, h, d)
            + q_rompsW_orH_S(h, w, d)
            + q_rompsW_orH_S(w, h, d)
            + noqulay_sh(w, h, d)
        )
    )
