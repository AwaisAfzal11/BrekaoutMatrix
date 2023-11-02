from fastapi import FastAPI
from pydantic import BaseModel 
from fastapi.responses import FileResponse
from tradingview_ta import TA_Handler, Interval, Exchange
from mangum import Mangum

class ForexData(BaseModel):
    # data structure
    symbol: str
    screener: str 
    exchange: str



app = FastAPI()
handler = Mangum(app)

@app.get("/")
def read_root():
    return FileResponse("forex.html")

@app.get('/get_forex_analysis')
def get_forex_analysis():
    tesla = TA_Handler(
        symbol="GBPUSD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_5_MINUTES
    )
    analysis = tesla.get_analysis().summary
    return analysis

@app.post('/getforex/')
def getforexx(getforexdict: ForexData):
    tesla = TA_Handler(
        symbol = getforexdict.symbol,
        screener = getforexdict.screener,
        exchange = getforexdict.exchange,
        interval = Interval.INTERVAL_5_MINUTES
    )

    analysis = tesla.get_analysis().summary

    return analysis
