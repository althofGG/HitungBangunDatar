# define a function for calculating
# the area of a shapes
def calculate_area(name):\
   
    # converting all characters
    # into lower cases
    name = name.lower()
    
    # check for the conditions
    if name == "1":
        l = int(input("Masukan panjang persegi panjang : "))
        b = int(input("Masukan lebar persegi panjang : "))
        
        # calculate area of rectangle
        luas = l * b
        keliling = 2 * (l+b)
        print(f"Luas persegi panjang adalah : {luas} \nKeliling persegi panjang adalah : {keliling}" )
    
   
    elif name == "2":
        s = int(input("Masukan panjang sisi persegi : "))
        
        # calculate area of square
        luas = s * s
        keliling = 4 * s
        print(f"Luas persegi adalah : {luas} \nKeliling persegi adalah : {keliling}" )
   
     
    else:
        print("Pilihan tidak tersedia, harap masukan angka dari 1-4")
        calculate_area(input("\n 1. Persegi Panjang \n 2. Persegi \n Masukan nomor bangun datar yang ingin anda hitung :"))
 
# driver code
if __name__ == "__main__" :
   
  print("Calculate Shape Area")
  shape_name = input("\n 1. Persegi Panjang \n 2. Persegi \n Masukan nomor bangun datar yang ingin anda hitung :")
   
  # function calling
  calculate_area(shape_name)