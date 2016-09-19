

class Softball_Methods():
    def season_stats(df):
        df = df.groupby(["Season","Player"]).sum().reset_index()
        df = Softball_Methods.stats_calc(df)
        return df
    def stats_calc(df):
        df["TB"] = 1*df["1B"]+2*df["2B"]+3*df["3B"]+4*df["4B"]+5*df["HR"]
        df["AVG"] = (df["H"]/df["AB"]).apply(lambda x: float('%.3f'%x))
        df["OBP"] = ((df["H"]+df["BB"])/(df["AB"]+df["BB"])).apply(lambda x: float('%.3f'%x))
        df["SLG"] = (df["TB"]/df["AB"]).apply(lambda x: float('%.3f'%x))
        df["OPS"] = (df["OBP"] + df["SLG"]).apply(lambda x: float('%.3f'%x))
        df["Ranking"] = df['OPS'].rank(ascending=False)
        df = df.sort(["Ranking"])
        return df
    def plot_data(df):
        df = df.groupby(["Player","Date"]).sum().reset_index()
        df = Softball_Methods.stats_calc(df)
        return df