import os
def main():
    os.system(' steghide embed -cf n_cat_2.jpg -ef secret.txt -p "" ' )
    
if __name__ == "__main__":
    main()
    
    