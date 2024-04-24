import streamlit as st
import pandas as pd
import altair as alt
import datetime

st.set_page_config(page_title="Performance Viewer")

# sidebar selection
with st.sidebar:
    st.title("Performance Viewer")

    strategy = st.selectbox(
        'Strategy',
        [
            'BTC Buy and Hold',
            'ETH Buy and Hold',
        ]
    )

    date = '2024-04-21'
    st.write("Date: ", date)

    # data preprocessing
    df = pd.read_csv(f"data/raw/{strategy[:3]}USDT-1m-{date}.csv")
    df['datetime_utc'] = pd.to_datetime(df['close_time'], unit='ms')
    df['datetime_utc_str'] = df['datetime_utc'].astype(str)
    df['time_str'] = df['datetime_utc_str'].str[11:16]
    
    df['pos'] = 1 # FIXME
    df['cummax'] = df['close'].cummax()
    df['drawdown'] = df['close'] / df['cummax'] - 1
    
    MIN_PLOT_DD = df['drawdown'].min() * 1.5
    MAX_PLOT_POS = df['pos'].max() * 5


    start_time, end_time = st.select_slider(
        'Time Range',
        options=df['time_str'],
        value=(df['time_str'].iloc[0], df['time_str'].iloc[-1])
    )

# plotting
df_sub = df.query(f"(time_str >= '{start_time}') & (time_str <= '{end_time}')").copy()
df_sub['cummax'] = df_sub['close'].cummax()
df_sub['drawdown'] = df_sub['close'] / df_sub['cummax'] - 1
df_sub['return'] = (df_sub['close'] / df_sub['close'].shift() - 1).round(4)
df_sub['pos'] = 1 # FIXME

annual_return = (df_sub['return'] * (60 * 24 * 365)).mean()
annual_risk = (df_sub['return'] * (60 * 24 * 365)**0.5).std()
max_dd = -df_sub['drawdown'].min()
sharpe = annual_return / annual_risk
calmar = annual_return / max_dd

risk_stat = pd.DataFrame({
    'Strategy': strategy,
    'Annualized Return': '{:.2%}'.format(annual_return),
    'Annualized Risk': '{:.2%}'.format(annual_risk),
    'Maximum Drawdown': '{:.2%}'.format(max_dd),
    'Sharpe Ratio': annual_return / annual_risk,
    'Calmar Ratio': annual_return / max_dd
}, index=[0]).set_index('Strategy')

av_chart = (
    alt.Chart(df_sub)
    .mark_line()
    .encode(
        x=alt.X('datetime_utc_str:T').axis(title="Time (UTC)"),
        y=alt.Y('close').scale(zero=False).axis(title='Value in USD', format='$,.0f')
    )
)

dd_chart = (
    alt.Chart(df_sub)
    .mark_line()
    .encode(
        x=alt.X('datetime_utc_str:T').axis(title="Time (UTC)"),
        y=alt.Y('drawdown').scale(domain=[MIN_PLOT_DD, 0]).axis(title="Percentage", format='%'),
        color=alt.value('orange'))
    .properties(
        height=200
    )
)

pos_chart = (
    alt.Chart(df_sub)
    .mark_bar()
    .encode(
        x=alt.X('datetime_utc_str:T').axis(title="Time (UTC)"),
        y=alt.Y('pos').scale(domain=[0, MAX_PLOT_POS]).axis(title="Asset Position"))
    .properties(
        height=200
    )
)

return_dist_chart = (
    alt.Chart(df_sub)
    .transform_density('return', as_=['return', 'density'])
    .mark_area(opacity=0.5)
    .encode(
        x=alt.X("return").axis(title="Return in Percentage", format='%'),
        y=alt.Y('density:Q').axis(title="Density"),
    )
)


# main panel
st.markdown("##### Asset Value")
st.altair_chart(
    av_chart,
    use_container_width=True
)

st.markdown("##### Drawdown")
st.altair_chart(
    dd_chart,
    use_container_width=True
)

st.markdown("##### Position")
st.altair_chart(
    pos_chart,
    use_container_width=True
)

st.markdown("##### Risk Statistics")
st.table(data=risk_stat)

st.markdown("##### Return Distribution")
st.altair_chart(
    return_dist_chart,
    use_container_width=True
)

