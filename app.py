import base64
import os
from flask import Flask, redirect, url_for, request, render_template, session, flash
from functools import wraps
from Database import Database

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
