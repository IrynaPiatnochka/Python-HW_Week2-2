reviews = [ "This product is really good. I'm impressed with its quality.", 
                  "The performance of this product is excellent. Highly recommended!", 
                  "I had a bad experience with this product. It didn't meet my expectations.", 
                  "Poor quality product. Wouldn't recommend it to anyone.", 
                  "The product was average. Nothing extraordinary about it." ]  

#Implementing a script that takes the first 30 characters of a review and appends "…"

def cropped(reviews):
    cropped_r = []
    for review in reviews:
        cropped_r.append(review[:30] + "...") 
        print(review)
    print(cropped_r)
cropped(reviews)

