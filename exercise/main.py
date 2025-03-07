import pandas as pd
from fpdf import FPDF


df = pd.read_csv('articles.csv')

class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df[df['id'] == self.article_id]['name'].squeeze()
        self.price = df[df['id'] == self.article_id]['price'].squeeze()

    def in_stock(self):
        in_stock = df[df['id'] == self.article_id]['in stock'].squeeze()
        return in_stock

    def buy(self):
        value = df.loc[df['id'] == self.article_id]['in stock'].squeeze() - 1
        df.loc[df['id'] == self.article_id, 'in stock'] = value
        df.to_csv("articles.csv", index=False)

class Receipt:
    def __init__(self, article_object):
        self.article = article_object

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.article_id}", ln=1)
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)
        pdf.output("receipt.pdf")

print(df)
article_id = int(input("Enter the id of the article you want to purchase: "))
article = Article(article_id)
receipt = Receipt(article)
if article.in_stock():
    article.buy()
    receipt.generate()
else:
    print('Out of stock')