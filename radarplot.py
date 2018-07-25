import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import flask
from flask_cors import CORS
import os


#Main app
app = dash.Dash()

app.layout = html.Div([
    #title banner
    html.Div([
        html.H2(
            'Multiparameter Classification of Diagnostic Device',
            id='title'
        )
    ],className='jumbotron',
    ),

    #body
    html.Div([
        html.Div([
            html.H4('Economic'),
            html.H5("Cost"),
            dcc.Dropdown(
                id='price-in',
                options=[
                    {'label': 'Above', 'value': 1},
                    {'label': 'slight Above', 'value': 2},
                    {'label': 'Industry standard', 'value': 3},
                    {'label': 'slight below', 'value': 4},
                    {'label': 'below', 'value': 5},
                    ],
                value=3
                ),
            html.H5("Time to Result"),
            dcc.Dropdown(
                id='time-in',
                options=[
                    {'label': 'Hours', 'value': 1},
                    {'label': 'Minutes', 'value':3},
                    {'label': 'Seconds', 'value':5},
                    ],
                value=3
                ),
            html.H5("Result Delivery"),
            dcc.Dropdown(
                id='delivery-in',
                options=[
                    {'label': 'Come Back Next Week', 'value': 1},
                    {'label': 'I Will Call You', 'value': 2.50},
                    {'label': 'Wait Here', 'value': 3.50},
                    {'label': 'Here it Is', 'value': 5},
                    ],
                value=2.5
                ),
            html.H4('Technical'),
            html.H5('Accuracy'),
            dcc.Dropdown(
                id='accuracy-in',
                options=[
                    {'label': 'Above', 'value': 1},
                    {'label': 'slight Above', 'value': 2},
                    {'label': 'Industry standard', 'value': 3},
                    {'label': 'slight below', 'value': 4},
                    {'label': 'below', 'value': 5},
                    ],
                value=3
                ),
            html.H5('Reliability'),
            dcc.Dropdown(
                id='reliability-in',
                options=[
                    {'label': 'Above', 'value': 1},
                    {'label': 'slight Above', 'value': 2},
                    {'label': 'Industry standard', 'value': 3},
                    {'label': 'slight below', 'value': 4},
                    {'label': 'below', 'value': 5},
                    ],
                value=3
                ),
            html.H5('Multiple Testing'),
            dcc.Dropdown(
                id='multiplex-in',
                options=[
                    {'label': 'Single Test', 'value': 1},
                    {'label': 'Parallel Testing', 'value':3},
                    {'label': 'Different Targets', 'value': 5},
                    ],
                value=3
                ),
            html.H4('Interaction'),
            html.H5('Portability'),
            dcc.Dropdown(
                id='portability-in',
                options=[
                    {'label': 'Heavy', 'value': 1},
                    {'label': 'Big', 'value': 2.50},
                    {'label': 'Small (tabpetop)', 'value': 3.50},
                    {'label': 'Pocket', 'value': 5},
                    ],
                value=2.5
                ),
            html.H5('Operation'),
            dcc.Dropdown(
                id='operation-in',
                options=[
                    {'label': 'Specialized Operator', 'value': 1},
                    {'label': 'Unspecialized Operator', 'value': 2.50},
                    {'label': 'supervised self-test', 'value': 3.50},
                    {'label': 'self-test', 'value': 5},
                    ],
                value=2.5
                ),
            html.H5('Comfort'),
            dcc.Dropdown(
                id='comfort-in',
                options=[
                    {'label': 'Invasive', 'value': 1},
                    {'label': 'Uncomfortable', 'value': 2.50},
                    {'label': 'Comfortable', 'value': 3.50},
                    {'label': 'Non-Invasive', 'value': 5},
                    ],
                value=2.5
                ),
            html.H4('Environmental'),
            html.H5('Disposal'),
            dcc.Dropdown(
                id='disposal-in',
                options=[
                    {'label': 'Special Disposal', 'value': 1},
                    {'label': 'Simple Disposal', 'value':3},
                    {'label': 'Recyclable', 'value': 5},
                    ],
                value=3
                ),
            html.H5('Stability (time)'),
            dcc.Dropdown(
                id='stability_time-in',
                options=[
                    {'label': 'Days', 'value': 1},
                    {'label': 'Weeks', 'value': 2.50},
                    {'label': 'Months', 'value': 3.50},
                    {'label': 'Years', 'value': 5},
                    ],
                value=2.5
                ),
            html.H5('Stability (condition)'),
            dcc.Dropdown(
                id='stability_condition-in',
                options=[
                    {'label': 'Needs Cold (upon use)', 'value': 1},
                    {'label': 'Needs Cold (for long term storage)', 'value': 2.50},
                    {'label': 'Requires Reconstitution', 'value': 3.50},
                    {'label': 'Ready to Use', 'value': 5},
                    ],
                value=2.5
                ),
            ], className='col-md-2'
            ),

            html.Div([
                html.Div([
                    dcc.Graph(id='main-graph-out')
                    ], className='center-block'
                    )
                ], className='col-md-10'
                )
        ], className='row'
        ),
    ], className='container-fluid'
    )

@app.callback(
    Output(component_id='main-graph-out', component_property='figure'),
    [
    Input(component_id='price-in', component_property='value'),
    Input(component_id='time-in', component_property='value'),
    Input(component_id='delivery-in', component_property='value'),
    Input(component_id='accuracy-in', component_property='value'),
    Input(component_id='reliability-in', component_property='value'),
    Input(component_id='multiplex-in', component_property='value'),
    Input(component_id='portability-in', component_property='value'),
    Input(component_id='operation-in', component_property='value'),
    Input(component_id='comfort-in', component_property='value'),
    Input(component_id='disposal-in', component_property='value'),
    Input(component_id='stability_time-in', component_property='value'),
    Input(component_id='stability_condition-in', component_property='value'),

    ]
)

def update_graph(
        price, time_to, delivery,
        accuracy, reliability, multiplex,
        portability, operation, comfort,
        disposal, stability_time, stability_condition
        ):

    data = [
        go.Scatterpolar(
            r=[
                price, time_to, delivery,
                accuracy, reliability, multiplex,
                portability, operation, comfort,
                disposal, stability_time, stability_condition,
                price,
                ],
            theta=[
                'Cost','Time to Result', 'Result Delivery',
                'Accuracy','Reliability', 'Multiple Testing',
                'Portability', 'Operation', 'Comfort',
                'Disposal', 'Stability (time)', 'stability (condition)',
                'Cost'
                ],
            mode='lines',
            fill='none',
            name='All',
            connectgaps=True,
            showlegend=False,
            line=dict(
                color='black',
                )
            ),
        go.Scatterpolar(
            r=[
                price, time_to, delivery,
                accuracy, 0, 0,
                0, 0, 0,
                0, 0, 0,
                ],
            theta=[
                'Cost','Time to Result', 'Result Delivery',
                'Accuracy','Reliability', 'Multiple Testing',
                'Portability', 'Operation', 'Comfort',
                'Disposal', 'Stability (time)', 'stability (condition)'
                ],
            mode='markers',
            marker=dict(
                symbol="0",
                color='fdae61',
                size=12,
                ),
            fill='toself',
            name='Economic'
            ),
        go.Scatterpolar(
            r = [
                0, 0, 0,
                accuracy, reliability, multiplex,
                portability, 0, 0,
                0, 0, 0,
                ],
            theta = [
                'Cost','Time to Result', 'Result Delivery',
                'Accuracy','Reliability', 'Multiple Testing',
                'Portability', 'Operation', 'Comfort',
                'Disposal', 'Stability (time)', 'stability (condition)'
                ],
            mode = 'markers',
            marker = dict(
                symbol = "0",
                color = 'd7191c',
                size=12,
                ),
            fill = 'toself',
            name = 'Technical',
            ),
        go.Scatterpolar(
            r = [
                0, 0, 0,
                0, 0, 0,
                portability, operation, comfort,
                disposal, 0, 0,
                ],
            theta = [
                'Cost','Time to Result', 'Result Delivery',
                'Accuracy','Reliability', 'Multiple Testing',
                'Portability', 'Operation', 'Comfort',
                'Disposal', 'Stability (time)', 'stability (condition)'
                ],
            mode = 'markers',
            marker = dict(
                symbol = "0",
                color = '2b83ba',
                size=12,
                ),
            fill = 'toself',
            name = 'Interaction',
            ),
        go.Scatterpolar(
            r = [
                price, 0, 0,
                0, 0, 0,
                0, 0, 0,
                disposal, stability_time, stability_condition,
                ],
            theta = [
                'Cost','Time to Result', "Result Delivery",
                'Accuracy','Reliability', 'Multiple Testing',
                'Portability', 'Operation', 'Comfort',
                'Disposal', 'Stability (time)', 'stability (condition)'
                ],
            mode = 'markers',
            unselected=dict(
                textfont=dict(
                    color='abdda4',
                    ),
                ),
            marker = dict(
                symbol = "0",
                color = 'abdda4',
                size=12,
                ),
            fill = 'toself',
            name = 'Environmental',
            ),
    ]
    layout = go.Layout(
        autosize=True,
        height=800,
        margin=dict(l='auto', r='auto', t='auto', b='auto', pad=0),
        polar =dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                ticks="",
                showticklabels=False,
                ),
            angularaxis=dict(
                tickprefix="",
                linewidth=2,
                tickwidth=2,
                ticklen=40,
                ticks='outside',
                tickfont=dict(
                    family='Raleway',
                    size=16,
                    ),
                ),
            ),
        showlegend = False,
        legend = dict(
            yanchor='top',
            xanchor='center',
            orientation = 'h',
            ),
        )

    return  {'data': go.Figure(data=data, layout=layout) }


external_css = [
    #"https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",  # Normalize the CSS
    "https://fonts.googleapis.com/css?family=Open+Sans|Roboto",  # Fonts
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css",
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css",
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js",
]

for css in external_css:
    app.css.append_css({"external_url": css})



if __name__ == '__main__':
    app.run_server(debug=True)
