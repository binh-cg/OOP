# Câu 1
def do_twice(f):
    f()
    f()

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def draw_beams():
    do_twice(print_beam)
    print('+')

def draw_posts():
    do_twice(print_post)
    print('|')

def draw_row():
    draw_beams()
    do_twice(draw_posts)
    do_twice(draw_posts)

def draw_grid():
    do_twice(draw_row)
    draw_beams()

draw_grid()

# Câu 2
def do_four(f):
    do_twice(f)
    do_twice(f)

def draw_beams_4():
    do_four(print_beam)
    print('+')

def draw_posts_4():
    do_four(print_post)
    print('|')