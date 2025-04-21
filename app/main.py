from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello CI/CD"}


@app.get("/hello")
def hello():
    return {"message": "Hello world"}


# Nuevo endpoint


@app.get("/products/{product_id}")
def get_product(product_id: int, category: str | None = None):
    return {"product_id": product_id, "category": category}
