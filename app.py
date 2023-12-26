from market import app

#ensures that the Flask development server starts only when the script is executed directly (not when imported as a module).
if __name__=='__main__':
    app.run(debug=True)