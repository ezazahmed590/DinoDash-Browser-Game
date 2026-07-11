from graphics import Canvas
    
def create_scorecard(canvas,x,y, text, font_size, color):    
    text =canvas.create_text(
    x, 
    y, 
    text,
    "Space Mono", 
    font_size, 
    color
    )

    return text