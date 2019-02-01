with open("img.ppm","w+") as file:
    file.write("P3 500 500 255\n")
    for x in range(500):
        for y in range(500):
            R=(x*y)%256
            G=(x-y)*x%256
            B=(x+y)*x%256
            img=f"{R} {G} {B} "
            file.write(img)
            
