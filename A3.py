import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("migration_nz.csv")
year_options = sorted(df["Year"].unique())

nz_lat, nz_lon = -40.9006, 174.8860
exclude_list = ["Oceania", "Asia", "Europe", "Americas", "Africa and the Middle East", "Antarctica", "New Zealand",
                "All countries", "Not stated"]

country_coords = {
    "Oceania": (-22.7359, 140.0188),
    "Antarctica": (-82.8628, 135.0000),
    "American Samoa": (-14.2710, -170.1322),
    "Australia": (-25.2744, 133.7751),
    "Cocos Islands": (-12.1642, 96.8700),
    "Cook Islands": (-21.2367, -159.7777),
    "Christmas Island": (-10.4475, 105.6904),
    "Fiji": (-17.7134, 178.0650),
    "Micronesia": (7.4256, 150.5508),
    "Guam": (13.4443, 144.7937),
    "Kiribati": (-3.3704, -168.7340),
    "Marshall Islands": (7.1315, 171.1845),
    "Northern Mariana Islands": (17.3303, 145.3843),
    "New Caledonia": (-20.9043, 165.6180),
    "Norfolk Island": (-29.0333, 167.95),
    "Nauru": (-0.5228, 166.9315),
    "Niue": (-19.0544, -169.8672),
    "New Zealand": (-40.9006, 174.8860),
    "French Polynesia": (-17.6797, -149.4068),
    "Papua New Guinea": (-6.314993, 143.95555),
    "Pitcairn Island": (-25.0667, -130.1000),
    "Palau": (7.5149, 134.5825),
    "Solomon Islands": (-9.6457, 160.1562),
    "French Southern Territories": (-49.3145, 69.3486),
    "Tokelau": (-9.2000, -171.8333),
    "Tonga": (-21.1790, -175.1982),
    "Tuvalu": (-7.1095, 179.1945),
    "Vanuatu": (-15.3767, 166.9592),
    "Wallis and Futuna": (-13.7687, -177.1561),
    "Samoa": (-13.7590, -172.1046),
    "Asia": (34.0479, 100.6197),
    "Afghanistan": (33.9391, 67.7100),
    "Armenia": (40.0691, 45.0382),
    "Azerbaijan": (40.1431, 47.5769),
    "Bangladesh": (23.6850, 90.3563),
    "Brunei Darussalam": (4.5353, 114.7277),
    "Bhutan": (27.5142, 90.4336),
    "China": (35.8617, 104.1954),
    "Georgia": (42.3154, 43.3569),
    "Hong Kong": (22.3193, 114.1694),
    "Indonesia": (-0.7893, 113.9213),
    "India": (20.5937, 78.9629),
    "Japan": (36.2048, 138.2529),
    "Kyrgyzstan": (41.2044, 74.7661),
    "Cambodia": (12.5657, 104.9910),
    "North Korea": (40.3399, 127.5101),
    "South Korea": (35.9078, 127.7669),
    "Kazakhstan": (48.0196, 66.9237),
    "Laos": (19.8563, 102.4955),
    "Sri Lanka": (7.8731, 80.7718),
    "Myanmar": (21.9162, 95.9560),
    "Mongolia": (46.8625, 103.8467),
    "Macau": (22.1987, 113.5439),
    "Maldives": (3.2028, 73.2207),
    "Malaysia": (4.2105, 101.9758),
    "Nepal": (28.3949, 84.1240),
    "Philippines": (12.8797, 121.7740),
    "Pakistan": (30.3753, 69.3451),
    "Singapore": (1.3521, 103.8198),
    "Thailand": (15.8700, 100.9925),
    "Tajikistan": (38.8610, 71.2761),
    "Timor-Leste": (-8.8742, 125.7275),
    "Turkmenistan": (38.9697, 59.5563),
    "Taiwan": (23.6978, 120.9605),
    "Uzbekistan": (41.3775, 64.5853),
    "Vietnam": (14.0583, 108.2772),
    "Europe": (54.5260, 15.2551),
    "Andorra": (42.5462, 1.6016),
    "Albania": (41.1533, 20.1683),
    "Austria": (47.5162, 14.5501),
    "Bosnia and Herzegovina": (43.9159, 17.6791),
    "Belgium": (50.8333, 4.0),
    "Bulgaria": (42.7339, 25.4858),
    "Belarus": (53.7098, 27.9534),
    "Switzerland": (46.8182, 8.2275),
    "Czechoslovakia": (49.8175, 15.4730),
    "Cyprus": (35.1264, 33.4299),
    "Czechia": (49.8175, 15.4730),
    "East Germany": (51.1657, 10.4515),
    "Germany": (51.1657, 10.4515),
    "Denmark": (56.2639, 9.5018),
    "Estonia": (58.5953, 25.0136),
    "Spain": (40.4637, -3.7492),
    "Finland": (61.9241, 25.7482),
    "Faeroe Islands": (62.0, -7.0),
    "France": (46.2276, 2.2137),
    "UK": (55.3781, -3.4360),
    "Gibraltar": (36.1408, -5.3536),
    "Greenland": (71.7069, -42.6043),
    "Greece": (39.0742, 21.8243),
    "Croatia": (45.1, 15.2),
    "Hungary": (47.1625, 19.5033),
    "Ireland": (53.4129, -8.2439),
    "Iceland": (64.9631, -19.0208),
    "Italy": (41.8719, 12.5674),
    "Kosovo": (42.6026, 20.9023),
    "Liechtenstein": (47.1660, 9.5554),
    "Lithuania": (55.1694, 23.8813),
    "Luxembourg": (49.8153, 6.1296),
    "Latvia": (56.8796, 24.6032),
    "Monaco": (43.7384, 7.4246),
    "Moldova": (47.4116, 28.3699),
    "Montenegro": (42.7087, 19.3744),
    "Macedonia": (41.6086, 21.7453),
    "Malta": (35.9375, 14.3754),
    "Netherlands": (52.1326, 5.2913),
    "Norway": (60.4720, 8.4689),
    "Poland": (51.9194, 19.1451),
    "Portugal": (39.3999, -8.2245),
    "Romania": (45.9432, 24.9668),
    "Serbia": (44.0165, 21.0059),
    "Russia": (61.5240, 105.3188),
    "Sweden": (60.1282, 18.6435),
    "Slovenia": (46.1512, 14.9955),
    "Slovakia": (48.6690, 19.6990),
    "San Marino": (43.9336, 12.4486),
    "USSR": (55.0, 82.0),
    "Ukraine": (48.3794, 31.1656),
    "Vatican City": (41.9029, 12.4534),
    "Yugoslavia/Serbia and Montenegro": (44.0165, 21.0059),
    "Americas": (8.0, -55.0),
    "Antigua and Barbuda": (17.0608, -61.7964),
    "Anguilla": (18.2206, -63.0686),
    "Netherlands Antilles": (12.5, -68.75),
    "Argentina": (-38.4161, -63.6167),
    "Aruba": (12.5211, -69.9683),
    "Barbados": (13.1939, -59.5432),
    "Bermuda": (32.3078, -64.7505),
    "Bolivia": (-16.2902, -63.5887),
    "Brazil": (-14.2350, -51.9253),
    "Bahamas": (25.0343, -77.3963),
    "Belize": (17.1899, -88.4976),
    "Canada": (56.1304, -106.3468),
    "Chile": (-35.6751, -71.5430),
    "Colombia": (4.5709, -74.2973),
    "Costa Rica": (9.7489, -83.7534),
    "Cuba": (21.5218, -77.7812),
    "Curacao": (12.1696, -68.9900),
    "Dominica": (15.4150, -61.3710),
    "Dominican Republic": (18.7357, -70.1627),
    "Ecuador": (-1.8312, -78.1834),
    "Falkland Islands": (-51.7963, -59.5236),
    "Grenada": (12.1165, -61.6790),
    "French Guiana": (3.9339, -53.1258),
    "Guadeloupe": (16.2650, -61.5510),
    "South Georgia and the South Sandwich Islands": (-54.4296, -36.5879),
    "Guatemala": (15.7835, -90.2308),
    "Guyana": (4.8604, -58.9302),
    "Honduras": (15.199999, -86.241905),
    "Haiti": (18.9712, -72.2852),
    "Jamaica": (18.1096, -77.2975),
    "St Kitts and Nevis": (17.3578, -62.782998),
    "Cayman Islands": (19.3133, -81.2546),
    "St Lucia": (13.9094, -60.9789),
    "Martinique": (14.6415, -61.0242),
    "Montserrat": (16.7425, -62.1874),
    "Mexico": (23.6345, -102.5528),
    "Nicaragua": (12.8654, -85.2072),
    "Panama": (8.5380, -80.7821),
    "Peru": (-9.189967, -75.015152),
    "St Pierre and Miquelon": (46.8852, -56.3159),
    "Puerto Rico": (18.2208, -66.5901),
    "Paraguay": (-23.4425, -58.4438),
    "Suriname": (3.9193, -56.0278),
    "El Salvador": (13.7942, -88.8965),
    "St Maarten": (18.0425, -63.0548),
    "Turks and Caicos": (21.6940, -71.7979),
    "Trinidad and Tobago": (10.6918, -61.2225),
    "US Minor Outlying Islands": (28.2167, -177.3667),
    "USA": (37.0902, -95.7129),
    "Uruguay": (-32.5228, -55.7658),
    "St Vincent and the Grenadines": (12.9843, -61.2872),
    "Venezuela": (6.4238, -66.5897),
    "British Virgin Islands": (18.4207, -64.6399),
    "US Virgin Islands": (18.3358, -64.8963),
    "Africa and the Middle East": (1.0, 20.0),
    "UAE": (23.4241, 53.8478),
    "Angola": (-11.2027, 17.8739),
    "Burkina Faso": (12.2383, -1.5616),
    "Bahrain": (25.9304, 50.6378),
    "Burundi": (-3.3731, 29.9189),
    "Benin": (9.3077, 2.3158),
    "Botswana": (-22.3285, 24.6849),
    "Democratic Republic of the Congo": (-4.0383, 21.7587),
    "Central African Republic": (6.6111, 20.9394),
    "Congo": (-0.2280, 15.8277),
    "Cote d'Ivoire": (7.539989, -5.5471),
    "Cameroon": (7.3697, 12.3547),
    "Cape Verde": (16.0021, -24.0132),
    "Djibouti": (11.8251, 42.5903),
    "Algeria": (28.0339, 1.6596),
    "Egypt": (26.8206, 30.8025),
    "Western Sahara": (24.2155, -12.8858),
    "Eritrea": (15.1794, 39.7823),
    "Ethiopia": (9.1450, 40.4897),
    "Gabon": (-0.8037, 11.6094),
    "Ghana": (7.9465, -1.0232),
    "Gambia": (13.4432, -15.3101),
    "Guinea": (9.9456, -9.6966),
    "Equatorial Guinea": (1.6508, 10.2679),
    "Guinea-Bissau": (11.8037, -15.1804),
    "Israel": (31.0461, 34.8516),
    "British Indian Ocean Territory": (-6.3432, 71.8765),
    "Iraq": (33.2232, 43.6793),
    "Iran": (32.4279, 53.6880),
    "Jordan": (30.5852, 36.2384),
    "Kenya": (-0.0236, 37.9062),
    "Comoros": (-11.8750, 43.8722),
    "Kuwait": (29.3759, 47.9774),
    "Lebanon": (33.8547, 35.8623),
    "Liberia": (6.4281, -9.4295),
    "Lesotho": (-29.6099, 28.2336),
    "Libya": (26.3351, 17.2283),
    "Morocco": (31.7917, -7.0926),
    "Madagascar": (-18.7669, 46.8691),
    "Mali": (17.5707, -3.9962),
    "Mauritania": (21.0079, -10.9408),
    "Mauritius": (-20.3484, 57.5522),
    "Malawi": (-13.2543, 34.3015),
    "Mozambique": (-18.6657, 35.5296),
    "Namibia": (-22.9576, 18.4904),
    "Niger": (17.6078, 8.0817),
    "Nigeria": (9.0820, 8.6753),
    "Oman": (21.5126, 55.9233),
    "Palestine": (31.9522, 35.2332),
    "Qatar": (25.3548, 51.1839),
    "Reunion": (-21.1151, 55.5364),
    "Rwanda": (-1.9403, 29.8739),
    "Saudi Arabia": (23.8859, 45.0792),
    "Seychelles": (-4.6796, 55.491977),
    "Sudan": (12.8628, 30.2176),
    "St Helena": (-15.9650, -5.7089),
    "Sierra Leone": (8.4606, -11.7799),
    "Senegal": (14.4974, -14.4524),
    "Somalia": (5.1521, 46.1996),
    "South Sudan": (7.8697, 29.6668),
    "Sao Tome and Principe": (0.1864, 6.6131),
    "Syria": (34.8021, 38.9968),
    "Swaziland": (-26.5225, 31.4659),
    "Chad": (15.4542, 18.7322),
    "Togo": (8.6195, 0.8248),
    "Tunisia": (33.8869, 9.5375),
    "Turkey": (38.9637, 35.2433),
    "Tanzania": (-6.3690, 34.8888),
    "Uganda": (1.3733, 32.2903),
    "South Yemen": (13.5, 45.0),
    "Yemen": (15.5527, 48.5164),
    "Mayotte": (-12.8275, 45.1662),
    "South Africa": (-30.5595, 22.9375),
    "Zambia": (-13.1339, 27.8493),
    "Zimbabwe": (-19.0154, 29.1549),
    "Not stated": (None, None),
    "All countries": (None, None),
}

continent_colors = {
    "Oceania": "#F88379",
    "Asia": "#F8DE7E",
    "Europe": "#93C572",
    "Americas": "#87CEEB",
    "Africa and the Middle East": "#D580FF"
}


def get_lat_lon(country_name):
    return country_coords.get(country_name, (None, None))

continents = ["Oceania", "Asia", "Europe", "Americas", "Africa and the Middle East"]

fig = make_subplots(
    rows=2, cols=4,
    specs=[
        [{"type": "scattergeo"}, {"type": "xy"}, {"type": "scattergeo"}, None],
        [{"type": "xy"}, {"type": "xy"}, {"type": "xy"}, {"type": "xy"}]
    ],
    column_widths=[1/3, 1/3, 1/3, 1/4],
    subplot_titles=(
        "Departures", "Top 10 Countries with Most Departures / Arrivals", "Arrivals",
        "Arrivals by Continent from 1979 to 2016",
        "Departures by Continent from 1979 to 2016", "Migration Trend(Arrivals vs. Departures)",
        "Net Migration from 1979 to 2016", ""
    )
)

measure_map = {"Arrivals": "#FFA07A", "Departures": "#1F51FF"}
trace_index = []

for measure in ["Arrivals", "Departures"]:
    for year in year_options:
        df_measure = df[(df["Measure"] == measure) & (df["Year"] == year)]
        df_measure = df_measure[df_measure["Citizenship"] == "Total All Citizenships"]
        df_measure = df_measure[df_measure["Value"] > 0]
        df_measure = df_measure[~df_measure["Country"].isin(exclude_list)]

        df_measure["lat_lon"] = df_measure["Country"].apply(get_lat_lon)
        df_measure["lat"] = df_measure["lat_lon"].apply(lambda x: x[0])
        df_measure["lon"] = df_measure["lat_lon"].apply(lambda x: x[1])
        df_measure = df_measure.dropna(subset=["lat", "lon"])

        col_num = 3 if measure == "Arrivals" else 1
        hover_text = [
            f"{row_item['Country']} → New Zealand：{row_item['Value']}" if measure == "Arrivals"
            else f"New Zealand → {row_item['Country']}：{row_item['Value']}"
            for _, row_item in df_measure.iterrows()
        ]

        fig.add_trace(go.Scattergeo(
            lon=df_measure["lon"],
            lat=df_measure["lat"],
            mode="markers",
            marker=dict(
                size=df_measure["Value"] ** 0.5 / 5 + 3,
                color=measure_map[measure],
                line=dict(width=0.5, color="white")
            ),
            hoverinfo="text",
            text=hover_text,
            visible=(year == year_options[0])
        ), row=1, col=col_num)
        trace_index.append((f"{measure}_points", year))

bar_y_positions = list(range(10))
for year in year_options:
    df_year = df[
        (df["Year"] == year) &
        (df["Citizenship"] == "Total All Citizenships") &
        (df["Value"] > 0) &
        (~df["Country"].isin(exclude_list))
    ]
    df_arrivals = df_year[df_year["Measure"] == "Arrivals"].groupby("Country")["Value"].sum().reset_index()
    df_departures = df_year[df_year["Measure"] == "Departures"].groupby("Country")["Value"].sum().reset_index()

    top_arrivals = df_arrivals.nlargest(10, "Value").reset_index(drop=True)
    top_departures = df_departures.nlargest(10, "Value").reset_index(drop=True)

    while len(top_arrivals) < 10:
        top_arrivals = pd.concat([top_arrivals, pd.DataFrame([{"Country": "", "Value": 0}])], ignore_index=True)
    while len(top_departures) < 10:
        top_departures = pd.concat([top_departures, pd.DataFrame([{"Country": "", "Value": 0}])], ignore_index=True)

    fig.add_trace(
        go.Bar(
            x=top_arrivals["Value"],
            y=bar_y_positions,
            orientation="h",
            marker=dict(color=measure_map["Arrivals"]),
            name=f"Arrivals Top10 ({year})",
            text=top_arrivals["Country"],
            textposition="outside",
            hovertemplate="%{text}: %{x}<extra></extra>",
            visible=(year == year_options[0])
        ),
        row=1, col=2
    )
    trace_index.append(("BarArrivals", year))

    fig.add_trace(
        go.Bar(
            x=[-v for v in top_departures["Value"]],
            y=bar_y_positions,
            orientation="h",
            marker=dict(color=measure_map["Departures"]),
            name=f"Departures Top10 ({year})",
            text=top_departures["Country"],
            textposition="outside",
            hovertemplate="%{text}: %{customdata[0]}<extra></extra>",
            customdata=[[top_departures.loc[i, "Value"]] for i in range(10)],
            visible=(year == year_options[0])
        ),
        row=1, col=2
    )
    trace_index.append(("BarDepartures", year))
    fig.update_xaxes(domain=[0.34, 0.62], row=1, col=2)


fig.update_yaxes(autorange="reversed", showticklabels=False, row=1, col=2)
fig.update_yaxes(domain=[0.6, 0.95], row=1, col=2)

df_total = df[df["Citizenship"] == "Total All Citizenships"]
df_arrivals = df_total[df_total["Measure"] == "Arrivals"].groupby("Year")["Value"].sum()
df_departures = df_total[df_total["Measure"] == "Departures"].groupby("Year")["Value"].sum()

arrival_trace_index = len(fig.data)
fig.add_trace(go.Scatter(
    x=df_arrivals.index,
    y=df_arrivals.values,
    mode="lines+markers",
    name="Arrivals",
    line=dict(color="#FFA07A", width=3),
    legendgroup="trend",
    visible=True
), row=2, col=3)

departure_trace_index = len(fig.data)
fig.add_trace(go.Scatter(
    x=df_departures.index,
    y=df_departures.values,
    mode="lines+markers",
    name="Departures",
    line=dict(color="#1F51FF", width=3),
    legendgroup="trend",
    visible=True
), row=2, col=3)

df_net = df[(df["Measure"] == "Net") & (df["Citizenship"] == "Total All Citizenships")]
net_migration = df_net.groupby("Year")["Value"].sum()
net_trace_index = len(fig.data)
fig.add_trace(
    go.Bar(
        x=net_migration.index,
        y=net_migration.values,
        name="Net Migration",
        marker_color=["green" if v >= 0 else "red" for v in net_migration.values],
        hovertemplate="Year %{x}: %{y}<extra></extra>",
        visible=True
    ),
    row=2,
    col=4
)

stacked_bar_indices = []
for continent in continents:
    values = []
    for year in year_options:
        df_year = df[
            (df["Year"] == year) &
            (df["Measure"] == "Arrivals") &
            (df["Citizenship"] == "Total All Citizenships") &
            (df["Country"] == continent)
        ]
        values.append(df_year["Value"].sum() if not df_year.empty else 0)

    fig.add_trace(
        go.Bar(
            x=year_options,
            y=values,
            name=continent,
            marker=dict(color=continent_colors[continent]),
            hovertemplate=continent + ": %{y}<extra></extra>",
            visible=True,
            showlegend=True
        ),
        row=2, col=1
    )
    stacked_bar_indices.append(len(fig.data)-1)


fig.update_layout(barmode='stack', bargap=0.15, bargroupgap=0.1)

stacked_bar_departures_indices = []
for continent in continents:
    values = []
    for year in year_options:
        df_year = df[
            (df["Year"] == year) &
            (df["Measure"] == "Departures") &
            (df["Citizenship"] == "Total All Citizenships") &
            (df["Country"] == continent)
        ]
        values.append(df_year["Value"].sum() if not df_year.empty else 0)

    fig.add_trace(
        go.Bar(
            x=year_options,
            y=values,
            name=continent + " (Departures)",
            marker=dict(color=continent_colors[continent]),
            hovertemplate=continent + ": %{y}<extra></extra>",
            visible=True
        ),
        row=2, col=2
    )
    stacked_bar_departures_indices.append(len(fig.data)-1)

fig.update_layout(barmode='stack', bargap=0.15, bargroupgap=0.1)

for idx, trace in enumerate(fig.data):
    if idx not in stacked_bar_indices:
        trace.showlegend = False

fig.update_layout(
    legend=dict(
        x=0.05,
        y=0.41,
        xanchor="left",
        yanchor="bottom",
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor="black",
        borderwidth=1
    )
)

buttons = []
for year in year_options:
    visible = [False] * len(fig.data)

    for idx, (name, trace_year) in enumerate(trace_index):
        if trace_year == year:
            visible[idx] = True

    visible[arrival_trace_index] = True
    visible[departure_trace_index] = True

    for idx in stacked_bar_indices:
        visible[idx] = True

    for idx in stacked_bar_departures_indices:
        visible[idx] = True

    visible[net_trace_index] = True

    buttons.append(dict(
        label=str(year),
        method="update",
        args=[{"visible": visible}]
    ))

fig.update_layout(
    updatemenus=[dict(
        buttons=buttons,
        x=1.0,
        y=1.0,
        xanchor="right",
        yanchor="top"
    )],
    title=dict(
        text="<b style='font-size:28px'>New Zealand Migration</b><br>"
             "<b style='font-size:20px'>Migration numbers to and from New Zealand from 1979 to 2016</b>",
        x=0.5,
        xanchor='center',
        yanchor='top'
    ),
    geo=dict(
        domain=dict(x=[0, 0.3], y=[0.55, 1]),
        scope="world",
        projection_type="natural earth",
        showland=True,
        landcolor="rgb(245,245,220)",
        showocean=True,
        oceancolor="rgb(220,235,245)",
        showcountries=True,
        countrycolor="rgb(200,200,200)",
        coastlinecolor="rgb(150,150,150)",
        showlakes=True,
        lakecolor="rgb(220,235,245)",
    ),
    geo2=dict(
        domain=dict(x=[0.67, 0.97], y=[0.55, 1]),
        scope="world",
        projection_type="natural earth",
        showland=True,
        landcolor="rgb(245,245,220)",
        showocean=True,
        oceancolor="rgb(220,235,245)",
        showcountries=True,
        countrycolor="rgb(200,200,200)",
        coastlinecolor="rgb(150,150,150)",
        showlakes=True,
        lakecolor="rgb(220,235,245)",
    ),
    height=900
)
annotations = fig.layout.annotations

annotations[0].x = 0.15
annotations[0].y = 0.95
annotations[0].xanchor = "center"
annotations[0].yanchor = "bottom"

annotations[1].x = 0.48
annotations[1].y = 0.95
annotations[1].xanchor = "center"
annotations[1].yanchor = "bottom"

annotations[2].x = 0.82
annotations[2].y = 0.95
annotations[2].xanchor = "center"
annotations[2].yanchor = "bottom"


fig.update_layout(annotations=annotations)
fig.update_layout(barmode="relative")

for annotation in fig.layout.annotations:
    annotation.font = dict(size=14, color="black", family="Arial Black")

fig.write_html(
    "index.html",
    include_plotlyjs="cdn",
    full_html=True
)


