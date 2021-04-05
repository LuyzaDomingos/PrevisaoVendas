import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div(children=[html.Div(children=[
    dcc.Link('Go to Page 1', href='/apps/app1', className='link'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/apps/app2', className='link'),
], className='landing')])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return index_page

if __name__ == '__main__':
    app.run_server(debug=True)