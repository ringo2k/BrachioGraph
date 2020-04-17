from brachiograph import BrachioGraph

# Uncomment the definition you want to use.

# This is an example BrachioGraph definition. If you build a plotter as
# described in the "Get started" section of the documentation, this definition
# is likely to work well. However, you should work out your own servo
# angle/pulse-width values as described in "Improve the plotter calibration".


# angles in degrees and# corresponding pulse-widths for the two arm servos
servo_1_angle_pws=[[-90.0, 2400], [-72.0, 2170], [-54.0, 1980], [-36.0, 1770], [-18.0, 1570], [0.0, 1381], [18.0, 1171], [36.0, 1005], [54.0, 815], [72.0, 645], [90.0, 509]]
servo_2_angle_pws=[[0.0, 530], [18.0, 680], [36.0, 880], [54.0, 1040], [72.0, 1260], [90.0, 1480], [108.0, 1690], [126.0, 1920]]

bg = BrachioGraph(
    # the lengths of the arms
    inner_arm=8,
    outer_arm=8,
    # the drawing area
    #bounds=(-12, 4, -4, 12),
    #bounds=(6, 6, 8, 8),
    # this results in 10x7
    bounds=(-2, 6, 7, 13),
    #bounds=(-1, 9, 3, 13),
    # 8 x 7
    # angles in degrees and corresponding pulse-widths for the two arm servos
    servo_1_angle_pws=servo_1_angle_pws,
    servo_2_angle_pws=servo_2_angle_pws,
    # pulse-widths for pen up/down
    pw_up=1290,
    pw_down=1390,
    hysteresis_correction_1=0,
    hysteresis_correction_2=0,
    #servo_1_centre=1500,
    #servo_2_centre=1526,
    #servo_1_degree_ms=-10,
    #servo_2_degree_ms=10,
)


# A "naively" calibrated plotter definition. We assume the default 10ms
# pulse-width difference = 1 degree of motor movement. If the arms appear to
# move in the wrong directions, try reversing the value of servo_1_degree_ms
# and/or servo_2_degree_ms.

# naive_bg = BrachioGraph(
#     # the lengths of the arms
#     inner_arm=8,
#     outer_arm=8,
#     # the drawing area
#     bounds=(-6, 4, 6, 12),
#     # relationship between servo angles and pulse-widths
#     servo_1_degree_ms=-10,
#     servo_2_degree_ms=10,
#     # pulse-widths for pen up/down
#     pw_down=1200,
#     pw_up=1850,
# )
