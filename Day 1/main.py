from fastapi import FastAPI
app = FastAPI()
device_status = {
    "name" : "Test Device 1",
    "model" : "T123",
    "time" : 23,
    "alive" : "yes"
}
@app.get("/device_status")
def status():
    return device_status

@app.get("/device_name")
def device_name():
    return device_status["name"]

@app.get("/")
def home():
    return "Welcome to the home page"