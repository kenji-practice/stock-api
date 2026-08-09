from fastapi import FastAPI

app = FastAPI()

stock_data = {
    "ハンドメイド石鹸": 12,
    "アロマキャンドル": 0,
    "陶器のマグカップ": 5,
}

@app.get("/stock/{item_name}")
def get_stock(item_name: str):
    if item_name in stock_data:
        quantity = stock_data[item_name]
        if quantity > 0:
            return {"result": f"{item_name}は、現在{quantity}個在庫があります。"}
        else:
            return {"result": f"{item_name}という商品名は見つかりませんでした。"}
    else:
        return {"result": f"{item_name}という商品名は見つかりませんでした。"}
