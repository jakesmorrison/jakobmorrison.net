

class Softball_Methods():
    def season_stats(df):
        df = df.groupby(["Season","Player"]).sum().reset_index()
        max_games_season = int(sorted(list(set(df["Games"].tolist())))[-1] / 2)
        if max_games_season == 0:
            df = df[df["Games"] > max_games_season]
        else:
            df = df[df["Games"] >= max_games_season]

        df = Softball_Methods.stats_calc(df)
        return df

    def game_stats(df):
        df = Softball_Methods.stats_calc(df)
        df = df[df["Games"]==1]
        return df

    def stats_calc(df):
        df["TB"] = 1*df["1B"]+2*df["2B"]+3*df["3B"]+4*df["4B"]+4*df["HR"]
        df["AVG"] = (df["H"]/df["AB"]).apply(lambda x: float('%.3f'%x))
        df["OBP"] = ((df["H"]+df["BB"])/(df["AB"]+df["BB"])).apply(lambda x: float('%.3f'%x))
        df["SLG"] = (df["TB"]/df["AB"]).apply(lambda x: float('%.3f'%x))
        df["OPS"] = (df["OBP"] + df["SLG"]).apply(lambda x: float('%.3f'%x))
        df["Ranking"] = df['OPS'].rank(ascending=False)
        df = df.fillna(0)
        df["Ranking"] = df["Ranking"].apply(lambda x: int(x))
        df = df.sort(["Ranking"])
        return df
    def plot_data(df):
        df = df.groupby(["Player","Date"]).sum().reset_index()
        df = Softball_Methods.stats_calc(df)
        return df