from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

file_path = "RiderData.csv"

df = pd.read_csv(file_path)

df = df.drop_duplicates()
df.columns = df.columns.str.strip()

@app.route("/")
def home():
    # Convert dataframe to HTML
    table = df.to_html(
        classes="table",
        index=False
    )

    return f"""
    <html>
    <head>
        <title>Cleaned Data</title>
        <style>
            body {{
                font-family: Arial;
                margin: 40px;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
            }}

            th {{
                background-color: #eee;
            }}
        </style>
    </head>

    <body>
        <h1>Cleaned Dataset</h1>
        {table}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)


