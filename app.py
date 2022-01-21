import dash
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
# https://community.plotly.com/t/drag-and-drop-cards/42480/6

app = dash.Dash(
    __name__,
    external_scripts=["https://cdnjs.cloudflare.com/ajax/libs/dragula/3.7.2/dragula.min.js"],
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div(id="main", children=[
    html.Div( className="container", children=[
        dbc.Row(id="drag_container",children=[
            
           dbc.Col(dbc.Card([
            dbc.CardHeader("Card 1"),
            dbc.CardBody(
                "Some content FIND1 " 
                "Some content FIND2 " 
                "Some content FIND3 " 
                
            ),

        ]),),

        dbc.Col(        dbc.Card([
            dbc.CardHeader("Card 2"),
            dbc.CardBody(
                "Some content FIND " 
                "Some content FIND " 
                "Some content FIND " 
            ),
        ]),),


        
        ]),
        

    ]),
        html.Div( className="container", children=[
            
        dbc.Row(id="drag_container1",children=[
            
           dbc.Col(dbc.Card([
            dbc.CardHeader("Card 3"),
            dbc.CardBody(
                "Some content FIND " 
                "Some content FIND " 
                "Some content FIND " 
                
            ),
 
        ]),),

            dbc.Col(        dbc.Card([
            dbc.CardHeader("Card 4"),
            dbc.CardBody(
                "Some content FIND " 
                "Some content FIND " 
                "Some content FIND " 
            ),
        ]),),


        
        ]),
        



    ]),
])

app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="make_draggable"),
    Output("drag_container", "data-drag"),
    [Input("drag_container", "id"),Input("drag_container1", "id")],
)

if __name__ == "__main__":
   app.run_server()