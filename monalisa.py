import turtle

def setup_turtle():
    turtle.tracer(400, 0)  
    turtle.bgcolor('#d6d6d6') 
    turtle.speed(0)  


def hex_to_bin(image_data, image_width, image_height):
    in_binary = bin(int(image_data, 16))[2:].rjust(image_width * image_height, '0')
    return in_binary


def draw_pixel(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    for _ in range(4):  
        turtle.forward(size)
        turtle.right(90)
    
    turtle.end_fill()

def draw_image(image_data, image_width, image_height, left, top, pixel_size):
    binary_data = hex_to_bin(image_data, image_width, image_height)
    
    for y in range(image_height):
        for x in range(image_width):
 
            pixel_x = left + (x * pixel_size)
            pixel_y = top - (y * pixel_size)

        
            if binary_data[y * image_width + x] == '1':
                color = get_color_for_pixel(x, y)  
                draw_pixel(pixel_x, pixel_y, pixel_size, color)


def get_color_for_pixel(x, y):
   
    r = int((x / 68) * 255) 
    g = int((y / 100) * 255)  
    b = 128  

    
    return f'#{r:02x}{g:02x}{b:02x}'

def main():
    monaLisaData = '0x54a9554ebaaab5555b776eeb56addebdb5db5b33fd9b6d5d6db55affcaeed576d559dd71576ab7a9a76ee32ceb59b556edd591df6b5aead5b265add256954aa52ad5aa55aa96ab55fd576d569d2b556affea992a955b4aa94effd4dd555496aa57f7feb45554a51534b9dfecb2aa36caa4a627ff14a49c254922d12ffd69345b54552c037f88a951423249a89ffe6905494892bc44bfda6689e74925a22bfd7125432a927800bff9d24bdeac83b5edfef6935fb7757fbbfff6d10adddd4ba9b5ffff4d5eeef37a913ff55255fabaff86aaffff92aafffd59103feafaadfb6fffc99fffe8ab5bff5ffc947ffffbdffd6f7f571ffffeeb6f7bfefe3d57eeffffffff77d9afbf7f5b7bbd7ffe5b7fff7efbff7fbff29fffafbffeffdebf97ffffdfedff6ffffdffffded7feffdd6fffffff7fd5fdb76ffedefffffffffffb7ff77fbb7dbbfef5b7feb57fdd6ddbf5efbdeb5bfffd6feeffdffe9afffdedefbb7fff8227fefafbfdfbefe5116bfcbbb7eeffde048fffe4dddfbbffca027ffbb6ff75f7fa090bf7fdd7bbabdfc0096fbee33ffdf7e2484ffbfbd1ddebff000170dffbef7fcfca910affffe9fb5ffe00897bffffdbdc7ff90017fffffefabffee805ffffeafefefefb757beefffb76ebf7fbfffffbffbf76ffbeedbfffffdffdbdffff7ffffffffffffffbbeff6bfefb76ffffdffffff7fbffb3fbfffffffbbfefd59efffdbefeffffbeafffffffffffffff7f7fefffffffffeedfbeffedfbffffffffeffffffbffeffffff7efdf7ffffffffff7fffefffffffffdfffeffffffbefffffbfbffdffffffff7bffff7ffffffffbfffffffbdfffbbdfffffffbdffebbffffffffffffff7efffffffffffff7feff5ffffff7f7ffbf76f05ffdffdfffff7bf892bffffffdfffffbe4a5fffffffefffffd50affffffffffffdf6a43fffffffffffffbb51f7fdfbfffffffd4baad57ffdfbfffd6b4f7ffffffffffff3ae7affffffffbff5be73f77effffeff7e8bbdffffffddffff5bfcefbf7ffffff7fd8def7fffefffffffeffffbfffffffffffb7fffffffffffffffefb77fffffffffffffffffffffffbffffffbfffffffffffffffffffffffffffffff7fffffffffffffffffffffff7ffffffffffffffffffffffff7ff7ffdfffffffeffffffffffffffffffffffff7fffffffffffffffffffffffffff'

    setup_turtle() 
    draw_image(monaLisaData, 68, 100, -272, 400, 8)  

    turtle.update()
    turtle.exitonclick()  

if __name__ == '__main__':
    main()
