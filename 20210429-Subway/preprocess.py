import pandas as pd


def clock_to_sec(c: int) -> int:
    hour, remainder = divmod(c, 10000)
    minute, sec = divmod(remainder, 100)
    return hour * 3600 + minute * 60 + sec


# format: %H%M%S
def clock_diff(c1: int, c2: int) -> int:
    return clock_to_sec(c2) - clock_to_sec(c1)


def time_diff(t1: int, t2: int) -> int:
    # returns -1 if this observation should not be used
    date1, clock1 = divmod(t1, int(1e6))
    date2, clock2 = divmod(t2, int(1e6))
    if date1 != 20180301 or date2 != 20180301:
        return -1
    diff = clock_diff(clock1, clock2)

    # 清除下车时间早于等于上车时间的数据和超过120min的数据.
    # 注意由于四舍五入，耗时为0“分钟”不代表下车时间等于上车时间成立.
    if diff < 0 or diff > 120 * 60:
        return -1
    else:
        return diff


def classify(t: int) -> int:
    clock = t % int(1e6)
    clock = clock // 100
    hour, minute = divmod(clock, 100)
    return hour * 6 + minute // 10


def read_file() -> pd.DataFrame:
    in_filename = "data/Subway_20180301.txt"
    in_sfilename = "data/Subway_20190301_top100000.txt"
    return pd.read_csv(in_filename)


def write_file(df: pd.DataFrame):
    df.to_csv("Subway_20180301.ppfull.txt", index=False)


def main():
    df = read_file()
    df.drop(labels=["carType", "cardType", "tradeType", "State"],
            axis=1, inplace=True)

    df["TimeDiff"] = df.apply(lambda row: time_diff(row["UpTime"], row["DownTime"]), axis=1)
    df = df[df["TimeDiff"] != -1]

    df["DiffInMin"] = df.apply(lambda row: round(row["TimeDiff"] / 60), axis=1)

    df["UpClass"] = df.apply(lambda row: classify(row["UpTime"]), axis=1)
    df["DownClass"] = df.apply(lambda row: classify(row["DownTime"]), axis=1)

    write_file(df)


if __name__ == '__main__':
    main()
