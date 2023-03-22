import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
ecom_sales = pd.read_csv(r'C:\Users\ADMIN\Desktop\Dash\dash_web_01\src\ecom_sales.csv')
ecom_bar = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
bar_graph = px.bar(data_frame=ecom_bar, x='Total Sales ($)', y='Country', orientation='h',title='Total Sales by Country')

# Create the DataTable
datatable = dash_table.DataTable(
    id='table',
    columns=[
        {'name': 'Description', 'id': 'Description', 'editable': True},
        {'name': 'Total Quantity', 'id': 'Total_Quantity', 'editable': True},
        {'name': 'Total Order Value', 'id': 'Total_OrderValue', 'editable': True}
    ],
    data=[
        {'Description': 'MINI PAINT SET VINTAGE', 'Total_Quantity': 1224, 'Total_OrderValue': 680.4},
        {'Description': 'ASSORTED COLOURS SILK FAN', 'Total_Quantity': 612, 'Total_OrderValue': 399},
        {'Description': 'PACK OF 12 CIRCUS PARADE TISSUES', 'Total_Quantity': 432, 'Total_OrderValue': 108},
        {'Description': 'WRAP ENGLISH ROSE', 'Total_Quantity': 425, 'Total_OrderValue': 146.5},
        {'Description': 'SET OF 6 TEA TIME BAKING CASES', 'Total_Quantity': 384, 'Total_OrderValue': 399.36}
    ],
    style_cell={'textAlign': 'left'},
    style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold'
    }
)
# Add a title to the DataTable
title = html.H3('Top 5 Selling Products', style={'color': 'blue'})

Customertable= dash_table.DataTable(
    id='table2',
    columns=[
        {'name': 'Customer ID', 'id': 'CustomerID', 'editable': True},
        {'name': 'Total Sales', 'id': 'Total_Sales', 'editable': True},
        {'name': 'Country', 'id': 'Country', 'editable': True}
    ],
    data=[
        {'CustomerID': 12415, 'Total_Sales': 5634.17999999999, 'Country': 'Australia'},
        {'Total_Sales': 1660.24, 'Country': 'Hong Kong'},
        {'Total_Sales': 662.78, 'Country': 'United Kingdom'},
        {'CustomerID': 12471, 'Total_Sales': 584.1, 'Country': 'Germany'},
        {'CustomerID': 12590, 'Total_Sales': 516, 'Country': 'Germany'}
    ],
    style_cell={'textAlign': 'left'},
    style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold'
    }
)

title2 = html.H3('Top 5 Customer VIP', style={'color': 'blue'})
title3 = html.H3('Overview', style={'color': 'blue'})
paragraph_text = 'The report presents the following key findings:\n\
The top 5 products with the highest sales volumes have been identified.\n\
The top 5 customers with the highest total order value have been identified, and they are considered to be potential VIP customers.\n\
The total revenue generated by the sale has been segmented by region.\n\
Moreover, the report highlights that the Australian market has the largest buyer segment compared to other markets. However, it has also been noted that customer IDs are missing in some locations, particularly in Hong Kong.'

Total = html.H4('Total revenue is 16918.64000000001 and total number of products sold is 11172', style={'color': 'red'})
# Create the Dash app

app = dash.Dash(__name__)
server = app.server

# Set up the layout using an overall div
app.layout = html.Div(
    children=[
        # Add a H1
        html.H1('Ecom Sales dashboard (ko)',style={'text-align': 'center'}),
        # Add styling to the overall div
        html.Div([
            html.Div(style={'width': '40%', 'display': 'inline-block', 'padding-right': '160px'},
                     children=[title, datatable]),
                     
            html.Div(style={'width': '40%', 'display': 'inline-block'},
                    children=[title2, Customertable]),
                html.Div(children=[Total]),
        # Add the graphs
                dcc.Graph(id='bar_graph', figure=bar_graph),
        # Add comment section
                html.Div(children=[title3]),
                html.Div(children=[html.P(paragraph_text)])    

        ])

    ])
if __name__ == '__main__':
    app.run_server(debug=True)