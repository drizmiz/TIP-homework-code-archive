
var pist_x_axis_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120];
var pist_series_data = [3530, 3390, 2897, 3377, 9724, 16065, 25070, 33567, 44023, 50560, 58900, 63524, 70653, 73673, 81084, 81252, 87392, 85113, 91411, 91826, 99485, 100904, 107820, 105704, 110405, 106800, 110310, 106645, 110188, 107707, 111613, 108307, 111458, 107142, 110692, 105921, 108205, 102493, 103830, 97758, 99747, 93002, 93152, 88262, 88203, 82339, 82228, 77670, 77192, 72179, 71017, 66334, 66210, 60957, 60190, 55478, 54328, 50282, 48821, 44970, 44155, 40545, 39646, 36677, 35817, 32646, 31936, 29045, 28595, 26117, 25786, 23322, 22831, 20846, 20525, 18560, 17889, 16528, 15931, 14535, 14120, 12859, 12245, 11202, 10889, 10028, 9424, 8481, 8498, 7631, 7175, 6491, 6369, 5877, 5609, 4846, 4778, 4105, 4042, 3644, 3582, 3228, 3020, 2728, 2644, 2366, 2370, 1990, 2025, 1885, 1688, 1658, 1619, 1429, 1319, 1207, 1210, 1070, 1032, 972, 474];
var pisc_x_axis_data = ['00:00-00:09', '00:10-00:19', '00:20-00:29', '00:30-00:39', '00:40-00:49', '00:50-00:59', '01:00-01:09', '01:10-01:19', '01:20-01:29', '01:30-01:39', '01:40-01:49', '01:50-01:59', '02:00-02:09', '02:10-02:19', '02:20-02:29', '02:30-02:39', '02:40-02:49', '02:50-02:59', '03:00-03:09', '03:10-03:19', '03:20-03:29', '03:30-03:39', '03:40-03:49', '03:50-03:59', '04:00-04:09', '04:10-04:19', '04:20-04:29', '04:30-04:39', '04:40-04:49', '04:50-04:59', '05:00-05:09', '05:10-05:19', '05:20-05:29', '05:30-05:39', '05:40-05:49', '05:50-05:59', '06:00-06:09', '06:10-06:19', '06:20-06:29', '06:30-06:39', '06:40-06:49', '06:50-06:59', '07:00-07:09', '07:10-07:19', '07:20-07:29', '07:30-07:39', '07:40-07:49', '07:50-07:59', '08:00-08:09', '08:10-08:19', '08:20-08:29', '08:30-08:39', '08:40-08:49', '08:50-08:59', '09:00-09:09', '09:10-09:19', '09:20-09:29', '09:30-09:39', '09:40-09:49', '09:50-09:59', '10:00-10:09', '10:10-10:19', '10:20-10:29', '10:30-10:39', '10:40-10:49', '10:50-10:59', '11:00-11:09', '11:10-11:19', '11:20-11:29', '11:30-11:39', '11:40-11:49', '11:50-11:59', '12:00-12:09', '12:10-12:19', '12:20-12:29', '12:30-12:39', '12:40-12:49', '12:50-12:59', '13:00-13:09', '13:10-13:19', '13:20-13:29', '13:30-13:39', '13:40-13:49', '13:50-13:59', '14:00-14:09', '14:10-14:19', '14:20-14:29', '14:30-14:39', '14:40-14:49', '14:50-14:59', '15:00-15:09', '15:10-15:19', '15:20-15:29', '15:30-15:39', '15:40-15:49', '15:50-15:59', '16:00-16:09', '16:10-16:19', '16:20-16:29', '16:30-16:39', '16:40-16:49', '16:50-16:59', '17:00-17:09', '17:10-17:19', '17:20-17:29', '17:30-17:39', '17:40-17:49', '17:50-17:59', '18:00-18:09', '18:10-18:19', '18:20-18:29', '18:30-18:39', '18:40-18:49', '18:50-18:59', '19:00-19:09', '19:10-19:19', '19:20-19:29', '19:30-19:39', '19:40-19:49', '19:50-19:59', '20:00-20:09', '20:10-20:19', '20:20-20:29', '20:30-20:39', '20:40-20:49', '20:50-20:59', '21:00-21:09', '21:10-21:19', '21:20-21:29', '21:30-21:39', '21:40-21:49', '21:50-21:59', '22:00-22:09', '22:10-22:19', '22:20-22:29', '22:30-22:39', '22:40-22:49', '22:50-22:59', '23:00-23:09', '23:10-23:19', '23:20-23:29', '23:30-23:39', '23:40-23:49', '23:50-23:59'];
var pisc_series_data = [0, 0, -28, -29, -32, -34, -34, -34, -34, -34, -34, -34, -34, -34, -34, -34, -34, -34, -34, -34, -34, -34, -34, -34, -34, -28, -23, 0, 85, 976, 2240, 4266, 7054, 10723, 15652, 22955, 32458, 45449, 64039, 90716, 127377, 174162, 226042, 288065, 355837, 422339, 492905, 553441, 574769, 574769, 569253, 533397, 481014, 423724, 372105, 317570, 279726, 242182, 204372, 174396, 158473, 145945, 137518, 131302, 125969, 121513, 119563, 118387, 116817, 115968, 115057, 115219, 116771, 118631, 120083, 120937, 121754, 122309, 122722, 123680, 123680, 123177, 120587, 119604, 120587, 121993, 122767, 122451, 121554, 121180, 121797, 125505, 128126, 131142, 135318, 137271, 141383, 147871, 152841, 159228, 169472, 180726, 206543, 256849, 288948, 316109, 370644, 395688, 402950, 441194, 462166, 443966, 410242, 372714, 331544, 299497, 266717, 236067, 213868, 187642, 167132, 158446, 148202, 142111, 136726, 130238, 124256, 122443, 117136, 111130, 103877, 93622, 85987, 78545, 66575, 54974, 42551, 28141, 18336, 11353, 6166, 3069, 944, 0];