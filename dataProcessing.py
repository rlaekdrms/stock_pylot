from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def mean_average(data, mean_width):
    new_array = []
    mean_width = int(mean_width)
    half_width = int(mean_width / 2)

    # for _ in range(half_width):
    #     new_array.append(0)

    for idx, _ in enumerate(data):
        if idx < half_width:
            newValue = None
        elif idx > len(data) - (half_width + 1):
            newValue = None
        else:
            newValue = sum(data[idx - half_width : idx + half_width + 1]) / mean_width
        new_array.append(newValue)

    # for _ in range(half_width):
    #     new_array.append(0)

    return new_array


def GetFiltered_clpr(data):
    columns = ["dates","values"]
    df = pd.DataFrame(columns=columns)

    for row in data['output2']:
        dateText = f"{row['stck_bsop_date'][2:4]}/{row['stck_bsop_date'][4:6]}/{row['stck_bsop_date'][6:8]}"
        # dateText = f"{row['stck_bsop_date'][4:6]}/{row['stck_bsop_date'][6:8]}"
        new_row =  pd.DataFrame([{"dates":dateText,"values":int(row['stck_clpr'])}])
        df = pd.concat([df,new_row],ignore_index=True)

    # Destructure 비구조화
    # 내용1, 내용2, 내용3 -> [내용1, 내용2, 내용3] : 구조화
    # [내용1, 내용2, 내용3] -> 내용1, 내용2, 내용3 : 비구조화
    # 비구조화를 사용하면 리스트나 튜플 등의 자료형을 여러 변수에 할당할 수 있다.

    fig, ax = plt.subplots()
    df_sorted = df.sort_values("dates")

    # 스무딩 처리
    df_smoothed1 = mean_average(df_sorted["values"], 5)
    df_smoothed2 = mean_average(df_sorted["values"], 15)
    df_smoothed3 = mean_average(df_sorted["values"], 30)

    ax.plot(df_sorted["dates"], df_sorted["values"])
    ax.plot(df_smoothed1, "orange")
    ax.plot(df_smoothed2, "red")
    ax.plot(df_smoothed3, "green")
    ax.legend(["Original", "Smoothed1", "Smoothed2", "Smoothed3"])
    # ax.legend(["Original", "Smoothed1"])

    # y축에 0원부터 표시됐으면 좋겠는데, 기간 내 최저가부터 표시가 됨. 이를 수정해야 함.
    # ax.set_ylim(bottom=0)
    # 성공. 채택 안함.

    ax.set_xlabel("Date") # x-axis label

    # TODO: X축 레이블 예쁘게 만들기
    ax.tick_params(axis='x', labelrotation=45)

    # plt.plot(df["dates"], df["values"],"orange")
    # fig.show()
    # fig.waitforbuttonpress()
    fig.savefig(f"{data['output1']['stck_shrn_iscd']}_result.png")

    print(df)
    return True
