#!/bin/env python
from app import create_app

app = create_app(debug=True)
app.run()
