import pandas as pd


def date():
    date = ""
    for line in open("curr-DWS.tmp"):
        date = line.split(" ")[0]
    return date


def work_time(time_file):
    time_args = []
    for line in open(time_file):
        time_args.append(line.split(" ")[0])
        time_sum = line.strip().split(" ")[1].split(":")
        time_sum[0] = int(time_sum[0]) * 3600
        time_sum[1] = int(time_sum[1]) * 60
        time_sum[2] = int(time_sum[2])
        time_args.append(sum(time_sum))

    worktime = float(time_args[3] - time_args[1]) / 60
    if time_args[0] != time_args[2]:
        worktime += 1440
    return round(worktime, 1)


def work_today():
    df = pd.read_csv('DWS_records.csv', index_col='Date')
    return round(df.loc[date()]['DW time'] / 60, 1)


def work_all():
    df = pd.read_csv('DWS_records.csv', index_col='Date')
    return round(df['DW time'].sum() / 60, 1)


def add_record(time, desc, df):
    if date() in df.index:
        actual_desc = df.loc[date()]['Description']
        if type(actual_desc) is not str:
            actual_desc = "None"
        time += df.loc[date()]['DW time']
        if actual_desc == "None" and desc == '':
            desc = 'None'
        elif actual_desc != "None" and desc != '':
            desc = actual_desc + '; ' + desc
        elif actual_desc != "None" and desc == '':
            desc = actual_desc
    elif desc == '':
        desc = 'None'
    df.loc[date()] = {'DW time': time, 'Description': desc}
    df.to_csv("DWS_records.csv", index_label='Date')


def user_input(manual):
    try:
        df = pd.read_csv('DWS_records.csv', index_col='Date')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['DW time', 'Description'])
    if date() in df.index:
        desc = input(f'Want to add another description to today? (curr.: {
            df.loc[date()]["Description"]}): ')
    else:
        desc = input('Session description: ')
    if manual:
        while True:
            try:
                manual_time = float(input(
                    "How much time do you want to add to today? (min): "))
                add_record(manual_time, desc, df)
                break
            except ValueError:
                print("Enter valid time format (plain number)")
    else:
        add_record(work_time('curr-DWS.tmp'), desc, df)


def stats():
    try:
        df = pd.read_csv('DWS_records.csv', index_col='Date')
        df = df.tail(7)
        df.loc['Total'] = pd.Series(
            f"{round(df['DW time'].sum() / 60, 1)} hrs", index=['DW time'])
        df = df.rename(columns={"DW time": "DW time (min)"})
        print(df)
    except FileNotFoundError:
        print("No records yet")
