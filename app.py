# Original Flask imports (incorrect for FastAPI)
# from flask import Flask, jsonify

# Correct FastAPI imports
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create FastAPI app
app = FastAPI(debug=True)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

