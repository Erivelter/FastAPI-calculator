from fastapi import FastAPI

app= FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World!"}

@app.post('/plus')
async def plus(num1, num2):
    result= int(num1)+int(num2)
    return {"result":result}

@app.post('/minus')
async def Minus(num1, num2):
    result = int(num1)-int(num2)
    return {"result":result}

@app.post('/multiply')
async def Multiply(num1, num2):
    result = int(num1)*int(num2)
    return {"result":result}

@app.post('/divide')
async def Divide(num1, num2):
    result = int(num1)/int(num2)
    return {"result":result}